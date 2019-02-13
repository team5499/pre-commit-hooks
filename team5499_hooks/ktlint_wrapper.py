from os import sys
from subprocess import Popen

def main(argv=None):
    if(sys.platform == "win32"):
        newArgs = ' '.join(argv[1:])
        p = Popen('ktlint-wrapper.bat ' + newArgs)
        stdout, stderr = p.communicate()
    else:
        newArgs = ' '.join(argv[1:])
        p = Popen('ktlint-wrapper.sh ' + newArgs)
        stdout, stderr = p.communicate()

if __name__ == '__main__':
    sys.exit(main())
