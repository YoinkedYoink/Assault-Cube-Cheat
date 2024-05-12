import time
import sys

while True:
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write("\r"+ char +" loading "+char)
        time.sleep(0.25)
        sys.stdout.flush() 
print()