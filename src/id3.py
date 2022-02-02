import eyed3, subprocess

def save_tag(path, tags):
    audiofile = eyed3.load(path)
    audiofile.initTag()
    save_image = False
    save_commnet = False
    for tag in tags:
        if tag == 'title' and tags['title'] != None:
            audiofile.tag.title = tags['title']
        if tag == 'artist' and tags['artist'] != None:
            audiofile.tag.artist = tags['artist']
        if tag == 'album' and tags['album'] != None:
            audiofile.tag.album = tags['album']
        if tag == 'album_artist' and tags['album_artist'] != None:
            audiofile.tag.album_artist = tags['album_artist']
        if tag == 'track_num' and tags['track_num'] != None:
            audiofile.tag.track_num = tags['track_num']
        if tag == 'comment' and tags['comment'] != None:
            save_commnet = True
        if tag == 'image' and tags['image'] != None:
            save_image = True
    audiofile.tag.save()
    
    # https://github.com/otaviobp/eyeD3
    if save_image or save_commnet:
        opt_image = ''
        opt_commnet = ''
        if save_image:
            opt_image = '--add-image="{image}":FRONT_COVER'.format(image=tags['image'])
        if save_commnet:
            # --comment=[LANGUAGE]:[DESCRIPTION]:COMMENT
            opt_commnet = '--comment="{comment}"'.format(comment=tags['comment'])
        
        cmd = 'eyed3 {opt_image} {opt_commnet} "{path}"'.format(opt_image=opt_image, opt_commnet=opt_commnet, path=path)
        p = subprocess.Popen(cmd)
        p.wait()

## test
# save_tag('BV1T44y1W7FY.mp3', {
#     'title': 'BV1T44y1W7FY',
#     'image': 'BV1T44y1W7FY.jpg',
# })
