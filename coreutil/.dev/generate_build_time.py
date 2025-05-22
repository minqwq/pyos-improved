import time
import datetime
import os
import platform
import curses
import uuid
import sys

if os.environ.get("SBI_ENABLED") == "true" or True or "True":
    pass
else:
    print("you forgot something.")
    sys.exit()
dt = datetime.datetime.now()
writeme = open("../buildtime_styled.txt", "w+", encoding="utf-8")
writeme.write("PY OS Improved SBI\n" +
              "Time at        - " + str(dt.strftime("%A, %d. %B %Y %H:%M:%S")) + "\n" +
              "Architecture   - " + platform.machine() + "\n" +
              "System/Kernel  - " + platform.system() + "\n" +
              "S/K, Version   - " + platform.release() + "\n" +
              "uuid           - " + str(uuid.uuid4()) + "\n\n" +
              "hope you beloved by god. --minqwq")
print("success, see ../buildtime_styled.txt please")
