import os, sys, json, datetime
import api, wget, uget
import osex
import mp3, id3

## get params
if len(sys.argv) <= 1:
    print('Usage: program <url|bvid>')
    exit(0)
url = sys.argv[1]
bvid = api.get_bvid(url)
partid = api.get_part_id(url)
if partid != 1:
    bvid = bvid + '_' + str(partid)

## get json
use_cache_json = False
json_uget = {}
if os.path.exists(bvid + '.json'):
    mtime_json = os.stat(bvid + '.json').st_mtime
    time_now = datetime.datetime.now().timestamp()
    time_offset = time_now - mtime_json # unit is sec
    if time_offset <= 1200: # less than 20min
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
id3.save_tag(bvid + '.mp3', {
    'title': stream['title'],
    'artist': api.get_owner_name(url),
    'image': bvid + '.jpg',
    'comment': api.get_url(url),
})

## rename mp3
title = json_uget['title'].replace('\\', u'＼') \
                          .replace('/', u'／') \
                          .replace(':', u'：') \
                          .replace('*', u'＊') \
                          .replace('?', u'？') \
                          .replace('"', u'＂') \
                          .replace('<', u'＜') \
                          .replace('>', u'＞') \
                          .replace('|', u'｜')
osex.remove(title + '.mp3')
if not osex.rename(bvid + '.mp3', title + '.mp3'):
    exit(0)

## delete cache
osex.remove(bvid + '.mp3.bat')
osex.remove(bvid + '.mp3')
osex.remove(bvid + '.aac')
osex.remove(bvid + '.jpg')
osex.remove(bvid + '.json')
