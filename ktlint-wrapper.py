from os import sys
from subprocess import Popen

if(sys.platform == "win32"):
    newArgs = ' '.join(sys.argv[1:])
    p = Popen('ktlint-wrapper.bat ' + newArgs)
    stdout, stderr = p.communicate()
else:
    newArgs = ' '.join(sys.argv[1:])
    p = Popen('ktlint-wrapper.sh ' + newArgs)
    stdout, stderr = p.communicate()
