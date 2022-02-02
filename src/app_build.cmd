del bilibili-mp3.exe
del bilibili-mp3.exe.spec
pyinstaller -F -i favicon.ico main.py -n bilibili-mp3.exe
copy dist\bilibili-mp3.exe .
del bilibili-mp3.exe.spec
