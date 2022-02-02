import midll

stream_video = 1
stream_audio = 2

def get_audio_info(path):
	MI = midll.MediaInfo()
	MI.Open(path)
	br = MI.Get(stream_audio, 0, 'BitRate')
	br_mode = MI.Get(stream_audio, 0, 'BitRate_Mode')
	br_max = MI.Get(stream_audio, 0, 'BitRate_Maximum')
	MI.Close()

	if br != '':
		br = round(int(br) / 1000.0)
	if br_max != '':
		br_max = round(int(br_max) / 1000.0)
	else:
		br_max = 0
	br = max(br, br_max)
	
	if br_mode == 'VBR' or br_mode == 'Variable':
		br_mode = 'vbr'
	else:
		br_mode = 'cbr'
	return br, br_mode
