import os, subprocess, json, traceback

def get_info_json(url):
    j = {}
    cookie = ''
    cookies_txt = 'cookies.txt'
    if os.path.exists(cookies_txt):
        cookie = '--cookies ' + cookies_txt
    p = subprocess.Popen('you-get {cookie} --json "{url}"'.format(cookie=cookie, url=url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = p.stdout.read()
    outstr = out.decode()
    outstr = outstr.replace('you-get: This is a multipart video. (use --playlist to download all parts.)', '')
    try:
        j = json.loads(outstr)
    except:
        print(out)
        traceback.print_exc()
    return j
