from os import sys
from subprocess import Popen

def main(argv=[]):
    print("0.3.11")
    if(sys.platform == "win32"):
        newArgs = ' '.join(argv)
        p = Popen('detekt-wrapper.bat ' + newArgs)
        stdout, stderr = p.communicate()
        print(stdout)
        print()
        print(stderr)
    else:
        newArgs = ' '.join(argv)
        p = Popen('detekt-wrapper.sh ' + newArgs)
        stdout, stderr = p.communicate()
        print(stdout)
        print()
        print(stderr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
