import os, sys, json, datetime, win32clipboard, subprocess
import api, wget, uget
import osex, version
import mp3, id3

version.print_version()
if os.path.exists('cookies.txt'):
    print('cookies file detected.')
else:
    print('cookies file not detected.')
    print("copy the 'cookies.txt' file to the same path when necessary.")

## get params
if len(sys.argv) == 1:
    # try parse url from clipboard
    win32clipboard.OpenClipboard()     
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)     
    win32clipboard.CloseClipboard() 
    if data.startswith('http'):
        url = data
    else:
        print('Usage: program <url|bvid>')
        exit(0)
elif len(sys.argv) < 1:
    print('Usage: program <url|bvid>')
    exit(0)
else:
    url = sys.argv[1]
bvid = api.get_bvid(url)
partid = api.get_part_id(url)
print(url)
print(bvid)
if partid != 1:
    bvid = bvid + '_' + str(partid)
print('partid: ' + str(partid))

## get json
use_cache_json = False
json_uget = {}
if os.path.exists(bvid + '.json'):
    mtime_json = os.stat(bvid + '.json').st_mtime
    time_now = datetime.datetime.now().timestamp()
    time_offset = time_now - mtime_json
    # less than 20min will redo get json
    if time_offset <= 1200:
        use_cache_json = True
if use_cache_json:
    with open(bvid + '.json', 'r', encoding='utf8') as f:
        json_uget = json.load(f)
else:
    json_uget = uget.get_info_json(url)
print(str(json_uget['url']))
print(str(json_uget['title']))

## save json
with open(bvid + '.json', 'w') as f:
    f.write(json.dumps(json_uget, indent=4))

## parse json
stream = api.parse_uget_json(json_uget)

## download audio
wget.download_adv(stream, bvid + '.aac')

## download cover
cover_url = api.get_cover_url(url)
wget.download(cover_url, '{bvid}.jpg'.format(bvid=bvid))

## convert audio to mp3
mp3.convert(bvid + '.aac', bvid + '.mp3')

## save cover to mp3
artist = api.get_owner_name(url)
id3.save_tag(bvid + '.mp3', {
    'title': stream['title'],
    'artist': artist,
    'image': bvid + '.jpg',
    'comment': api.get_url(url),
})

## rename mp3
title = (artist + ' - ' + json_uget['title']).replace('\\', u'???') \
                          .replace('/', u'???') \
                          .replace(':', u'???') \
                          .replace('*', u'???') \
                          .replace('?', u'???') \
                          .replace('"', u'???') \
                          .replace('<', u'???') \
                          .replace('>', u'???') \
                          .replace('|', u'???')
osex.remove(title + '.mp3')
if not osex.rename(bvid + '.mp3', title + '.mp3'):
    exit(0)

## download lrc
if os.path.exists('zlrc.exe'):
    cmd = 'zlrc "{path}"'.format(path=title + '.mp3')
    p = subprocess.Popen(cmd)
    p.wait()

## delete cache
osex.remove(bvid + '.mp3.bat')
osex.remove(bvid + '.mp3')
osex.remove(bvid + '.aac')
osex.remove(bvid + '.jpg')
osex.remove(bvid + '.json')
