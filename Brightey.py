from core import banner
import os
import atexit
from core import ccolors
from core.main import modules
from time import sleep
from core.brightey_dir import get_dir


@atexit.register
def on_exit():
    os.system("clear")
    sleep(0.1)
    print(ccolors.gold + "\n <!> Exiting" + ccolors.end)
    exit(1)


def console():
    command = str(input(ccolors.blue + "[" + path + "/] " + ccolors.end + ccolors.red + "[Brightey]> " + ccolors.end))
    return command


brightey_path = get_dir()
path = os.getcwd()
os.system("clear")
banner.prnt()

while True:
    cmd = console()
    if cmd != "":
        cmd = cmd.split(" ")
        while "" in cmd:
            cmd.remove("")
        if cmd[0] == "cd":
            if len(cmd) == 1:
                path = "/root"
            elif os.path.exists(path + "/" + cmd[1]):
                path = path + "/" + cmd[1]
            else:
                print(ccolors.warn + "<!> Directory " + path + "/" + cmd[1] + " does not exists" + ccolors.end)
        elif cmd[0] == "ls":
            os.system("ls " + path)
            pass
        else:
            modules(cmd[0], path + "/", brightey_path + "/")
