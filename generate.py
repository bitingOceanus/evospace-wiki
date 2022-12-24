import subprocess
import shutil
import os
import os.path
import sys

our_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(our_path)

for dirpath, dirnames, filenames in os.walk(our_path + "/../gen"):
  for filename in [f for f in filenames if f.endswith(".py")]:
    fullname = os.path.join(dirpath, filename)
    print(fullname + " is runned")
    popen = subprocess.Popen(["python3", fullname])
    popen.wait()
    print("Done")
