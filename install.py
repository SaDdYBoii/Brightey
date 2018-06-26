import os
import sys
red = '\33[31m'
blue = '\33[34m'
green = '\33[92m'
gold = '\33[93m'
warn = '\33[41m'
end = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'
print(gold + """    ____       _       __    __            
   / __ )_____(_)___ _/ /_  / /____  __  __
  / __  / ___/ / __ `/ __ \/ __/ _ \/ / / /
 / /_/ / /  / / /_/ / / / / /_/  __/ /_/ / 
/_____/_/  /_/\__, /_/ /_/\__/\___/\__, /  
             /____/               /____/      """ + end)
version = open("core/version.txt")
vs = version.readline()
pversion = sys.version_info[0]
print(blue + "Version: " + vs + end)
print(blue + "Python Version: " + str(pversion) + end)
if not os.getuid() == 0:
    print(warn + "<!> Script needs to be run as root!" + end)
    exit(1)
path = os.getcwd()
print("Please do not move folder containing Brightey after installation")
print(bold + "Developers assume no liability and are not responsible for any misuse or damage caused by this program!" + end)
if pversion >= 3:
    not_answered = True
    while not_answered:
        ask = str(input(red + "\n\n[Are you sure that you want to install Brightey on your computer? {Yes/no}]> " + end))
        if ask == "Yes":
            not_answered = False
        elif ask == "no":
            exit(1)
else:
    not_answered = True
    while not_answered:
        ask = str(
            raw_input(red + "\n\n[Are you sure that you want to install Brightey on your computer? {Yes}]> " + end))
        if ask == "Yes":
            not_answered = False
os.system("sudo apt-get install python3")
os.system("pip install urllib3")
alias = r"alias brightey='" + "python3 " + path + r"/Brightey.py'"
homefolder = os.path.expanduser('~')
bashrc = os.path.abspath('%s/.bashrc' % homefolder)
with open(bashrc, 'r') as f:
  lines = f.readlines()
  if alias not in lines:
    out = open(bashrc, 'a')
    out.write(alias)
    out.close()

brightey_path = os.getcwd()
file = open("core/brightey_dir.py", 'w')
file.write("def get_dir():")
file.write("\n   return " + r"'" + brightey_path + r"'")
file.close()
print(gold + "Brightey successfully installed. Open new terminal and type brightey to run program!" + end)
