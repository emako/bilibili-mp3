import requests, json

def get(bvid):
    if bvid.startswith('http'):
        bvid = get_bvid(bvid)
        return get(bvid)
    if bvid.lower().startswith('av'):
        res = requests.get('https://api.bilibili.com/x/web-interface/view?aid=' + bvid[2:]).text
    else:
        res = requests.get('https://api.bilibili.com/x/web-interface/view?bvid=' + bvid).text
    resj = json.loads(res)
    return resj

def get_url(url):
    if url.startswith('http'):
        return url.split('?')[0]
    else:
        return 'https://www.bilibili.com/video/' + get_bvid(url)

def get_bvid(url):
    url_splited = url.split('?')[0]
    if url_splited.endswith('/'):
        url_splited = url_splited[0:-1]
    bvid = url_splited.split('/')[-1]
    return bvid

def get_part_id(url):
    p = ''
    if '?p=' in url:
        start_index = url.find('?p=') + 2
        curr_index = 0
        for u in url:
            if curr_index > start_index:
                try:
                    n = int(u)
                    p += str(n)
                except:
                    break
            curr_index += 1
        p = int(p)
    else:
        p = 1
    return p

def get_cover_url(url):
    return get(url)['data']['pic']

def get_owner_name(url):
    return get(url)['data']['owner']['name']

def parse_uget_json(input):
    output = {}
    output['size'] = 0
    for stream_name in input['streams']:
        stream = input['streams'][stream_name]

        if stream['size'] > output['size']:
            output = stream
            output['name'] = stream_name
        print('[{stream_name}] {quality} {size}MB'.format(stream_name=stream_name, quality=stream['quality'], size=int(stream['size']) / 1024 / 1024))
    output['referer'] = input['extra']['referer']
    output['ua'] = input['extra']['ua']
    output['title'] = input['title']
    return output
