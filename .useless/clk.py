import time
startup = time.time()
time.sleep(1)
endstartup = time.time()
print("Startup took %ss" % ((startup - endstartup)+2))
