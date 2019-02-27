import os
from subprocess import Popen
import urllib

DOWNLOAD_URL = "https://github.com/arturbosch/detekt/releases/download/RC10/detekt-cli-1.0.0-RC10-all.jar"
CACHE_DIR=os.path.dirname(os.path.abspath(__file__))

# def runWindows(files, extras):
#     if(not os.path.exists(os.path.join(CACHE_DIR, "detekt.jar"))):
#         print("downloading detekt.jar ...")
#         urllib.urlretrieve(DOWNLOAD_URL, os.path.join(CACHE_DIR, "detekt.jar"))
    
#     p = Popen('java -jar ' + os.path.join(CACHE_DIR, "detekt.jar") + ' ' + ' '.join(extras) + ' -i ' + files)
#     stdout, stderr = p.communicate()
#     print(stdout)
#     print()
#     print(stderr)

# def runNix(files, extras):
#     if(not os.path.exists(os.path.join(CACHE_DIR, "detekt.jar"))):
#         print("downloading detekt.jar ...")
#         urllib.urlretrieve(DOWNLOAD_URL, os.path.join(CACHE_DIR, "detekt.jar"))
    
    

# def main(files, extras):
#     print("0.3.15")
#     if(os.sys.platform == "win32"):
#         # newArgs = ' '.join(argv)
#         # executable = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'detekt-wrapper.bat')
#         # p = Popen(executable + ' ' + newArgs)
#         # stdout, stderr = p.communicate()
#         # print(stdout)
#         # print()
#         # print(stderr)
#         runWindows(files, extras)
#     else:
#         # newArgs = ' '.join(argv)
#         # executable = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'detekt-wrapper.sh')
#         # p = Popen('/bin/bash ' + executable + ' ' + newArgs)
#         # stdout, stderr = p.communicate()
#         # print(stdout)
#         # print()
#         # print(stderr)
#         runNix(files, extras)

if __name__ == '__main__':
    print("0.3.15")
    args = os.sys.argv[1:]
    files = ''
    extras = []
    for i in args:
        if(os.path.exists(i)):
            files = files + ',' + i
        else:
            extras.append(i)
    
    if(not os.path.exists(os.path.join(CACHE_DIR, "detekt.jar"))):
        print("downloading detekt.jar ...")
        urllib.urlretrieve(DOWNLOAD_URL, os.path.join(CACHE_DIR, "detekt.jar"))
    
    p = Popen('java -jar ' + os.path.join(CACHE_DIR, "detekt.jar") + ' ' + ' '.join(extras) + ' -i ' + files[1:], shell=True)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)
    print('Finished')
    os.sys.exit(p.returncode)