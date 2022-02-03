import sys, os, zipfile, subprocess, traceback

print('_MEIPASS: ' + sys._MEIPASS)
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

try:
    tmpdir = sys._MEIPASS + '\\res\\'
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)

    zip_file = zipfile.ZipFile(resource_path('res\\python.zip'))
    zip_list = zip_file.namelist()

    for f in zip_list:
        zip_file.extract(f, tmpdir)
    
    zip_file.close()

    args = []
    for arg in sys.argv:
        args.append('"' + arg + '"')
    cmd = tmpdir + 'python ' +  tmpdir + 'main.py ' + ' '.join(args[1:])
    print(cmd)
    p = subprocess.Popen(cmd)
    p.wait()
except:
    traceback.print_exc()

# while True:
#     import time
#     time.sleep(999)
