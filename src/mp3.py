import subprocess, os
import mi

abr = 'abr'
cbr = 'cbr'
vbr = 'vbr'

def get_convert_fmt(path):
    br, br_mode = mi.get_audio_info(path)
    print('{br}kbps ({br_mode})'.format(br=br, br_mode=br_mode))
    
    br_tar = 192
    br_fmt = cbr
    if br >= 280:
        br_tar = 320
        br_fmt = cbr
    elif br >= 256 and br < 280:
        br_tar = 320
        br_fmt = abr
    elif br >= 216 and br < 256:
        br_tar = 256
        br_fmt = cbr
    elif br >= 192 and br < 216:
        br_tar = 256
        br_fmt = abr
    elif br >= 152 and br < 192:
        br_tar = 192
        br_fmt = cbr
    elif br >= 128 and br < 152:
        br_tar = 192
        br_fmt = abr
    elif br >= 88 and br < 128:
        br_tar = 128
        br_fmt = cbr
    elif br >= 64 and br < 88:
        br_tar = 128
        br_fmt = abr
    elif br >= 24 and br < 64:
        br_tar = 64
        br_fmt = cbr
    elif br >= 0 and br < 24:
        br_tar = 64
        br_fmt = abr
    return br_tar, br_fmt

def rm(path):
    try:
        os.remove(path)
    except:
        pass

def convert(path, output):
    br_tar, br_fmt = get_convert_fmt(path)
    cmd = 'ffmpeg -i {path} -vn -sn -v 0 -c:a pcm_s16le -f wav pipe: | lame -b {br_tar} --{br_fmt} -h - "{output}"'.format(path=path, br_tar=br_tar, br_fmt=br_fmt, output=output)
    print(cmd)
    output_bat = output + '.bat'
    rm(output_bat)
    with open(output_bat, 'w') as f:
        f.write(cmd)
    p = subprocess.Popen(output + '.bat')
    p.wait()
    rm(output_bat)

## test
# convert('BV1T44y1W7FY.aac', 'BV1T44y1W7FY.mp3')
