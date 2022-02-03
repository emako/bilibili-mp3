rd /s /q .\you-get\
git clone https://github.com/soimort/you-get.git
cd /d you-get
copy ..\you-get.ico you-get.ico
pyinstaller -F -i you-get.ico --path=src you-get --hidden-import=you_get.extractors --hidden-import=you_get.cli_wrapper
copy /y .\dist\you-get.exe ..
