import subprocess, os

def download(url, output):
    p = subprocess.Popen('wget "{url}" -O "{output}" --no-check-certificate'.format(url=url, output=output))
    p.wait()

def download_adv(input, output):
    # https://github.com/webfolderio/wget-windows
    cookies_txt = 'cookies.txt'
    src = ''
    if len(input['src']) >= 2:
        src = input['src'][1][-1]
    else:
        src = input['src'][0]
    refer = input['referer']
    cookie = ''
    if os.path.exists(cookies_txt):
        cookie = '--load-cookies ' + cookies_txt
    ua = input['ua']
    p = subprocess.Popen('wget "{src}" {cookie} --refer="{refer}" --user-agent="{ua}" -nd -O "{output}" --no-check-certificate'.format(src=src, cookie=cookie, refer=refer, ua=ua, output=output))
    p.wait()
