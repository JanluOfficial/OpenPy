import data.apps.apppck.shell_api as shell_api
import os
import platform
from os.path import exists

# Do not eat cheese at 69:42066AM

curdir = os.getcwd()

if not platform.system() == "Windows":
    appdir = curdir + "/data/apps"
    gamedir = curdir + "/data/games"
    apppckdir = curdir + "/data/apps/apppck"
    gamepckdir = curdir + "/data/apps/gamepck"
else:
    appdir = curdir + "\\data\\apps"
    gamedir = curdir + "\\data\\games"
    apppckdir = curdir + "\\data\\apps\\apppck"
    gamepckdir = curdir + "\\data\\apps\\gamepck"
applist = os.listdir(appdir)
apppcklist = os.listdir(apppckdir)

env = shell_api.getdata("env")
shell_api.bigprint("OpenPy", "c")
print(env)

while 1:
    print()
    cmd = input("open_py> ") 
    print()
    
    if cmd == "help":
        print("Help Menu!")
        print("----------------------------------------")
        print("search <app/game> (package) [name] - Searches Apps and Games!")
        print("quit - I think it explains itself, but it basically is for closing OpenPy!")
        print("run <app/game> [name] - Used to open Apps and Games.")
        print("clear - Clears the Console.")
        print("----------------------------------------")
        
    
    if "search " in cmd:
        if "search app package " in cmd:
            search =  cmd.replace("search app package ","")
            print("Results:")
            print("----------------------------------------")
            for item in apppcklist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        apppck = item.replace(".py","")
                        print(apppck + " (" + item + ")")
            print("----------------------------------------")

        elif "search app " in cmd:
            search =  cmd.replace("search app ","")
            print("Results:")
            print("----------------------------------------")
            for item in applist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        app = item.replace(".py","")
                        print(app + " (" + item + ")")
            print("----------------------------------------")

        else:
            print("Invalid Search Type!")

    elif cmd == "quit":
        exit()

    elif "run " in cmd:
        app = cmd.replace("run app ","")
        appfile = app + '.py'
        if exists('data/apps' + appfile):
            exec(open('data/apps/' + appfile + '').read())
        else:
            print("This app seems to not be installed. Don't worry about it, happens to the best of us.")

    elif cmd == "clear":
        shell_api.clear()

    else:
        print("Oh no, that command doesn't seem to be valid. :(")

