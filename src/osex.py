import os, traceback

def remove(path):
    try:
        os.remove(path)
    except:
        pass

def rename(src, dst):
    try:
        os.rename(src, dst)
    except:
        traceback.print_exc()
        return False
    return True
