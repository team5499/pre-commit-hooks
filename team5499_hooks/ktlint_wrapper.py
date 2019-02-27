import os
from subprocess import Popen
try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve

DOWNLOAD_URL = "https://github.com/shyiko/ktlint/releases/download/0.29.0/ktlint"
CACHE_DIR=os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    print("0.3.15")
    args = os.sys.argv[1:]
    if(not os.path.exists(os.path.join(CACHE_DIR, "ktlint"))):
        print("downloading ktlint ...")
        urlretrieve(DOWNLOAD_URL, os.path.join(CACHE_DIR, "ktlint"))
    
    if(os.sys.platform == "win32"):
        p = Popen('C:\\Program Files\\Git\\bin\\sh.exe' + os.path.join(CACHE_DIR, "ktlint") + ' ' + ' '.join(args), shell=True)
        stdout, stderr = p.communicate()
        print(stdout)
        print(stderr)
        print('Finished')
        os.sys.exit(p.returncode)
    else:
        print("command")
        p = Popen('chmod a+x ' + os.path.join(CACHE_DIR, "ktlint") + ' && command ' + os.path.join(CACHE_DIR, "ktlint") + ' ' + ' '.join(args), shell=True)
        stdout, stderr = p.communicate()
        print(stdout)
        print(stderr)
        print('Finished')
        os.sys.exit(p.returncode)
    