#!/usr/bin/python
import time

def procedure():
    time.sleep(1)

# measure process time
t = time.clock()
procedure()
print (time.clock() - t, "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t, "seconds wall time")