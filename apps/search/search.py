# Python code to search filenames in current
# folder (We can change file type/name and path
# according to the requirements.
import os

count = 0
hdcnt = 0
insrc = input("Search filename: ")
# This is to get the directory that the program 
# is currently running in.
# dir_path = os.path.dirname(os.path.realpath(__file__))
 
for root, dirs, files in os.walk("."):
    for file in files: 
 
        # change the extension from '.mp3' to 
        # the one of your choice.
        if file.startswith(insrc) and root.startswith("./.") or root.startswith(".\\."):
            print ("\033[33m"+root+'/'+str(file))
            hdcnt += 1
        elif file.startswith(insrc) and root.startswith("./") or root.startswith(".\\"):
            print("\033[32m"+root+"/"+str(file))
            count += 1
print("\033[0mVisible: " + str(count) + ", Hide: " + str(hdcnt))
print("Total " + str(count + hdcnt) + " Files founded")
