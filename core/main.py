from core import portscanner
from core import ccolors
from core import dos
from core import proxychecker
from core import massmailer
from time import sleep
from core import wordlist2hash
from core import dencrypt


def modules(name, path, ppath):
    if name == "pscan":
        portscanner.main()
    elif name == "exit":
        exit(1)
    elif name == "dos":
        dos.start()
    elif name == "proxy-checker":
        proxychecker.start(path)
    elif name == "help":
        with open(ppath + "core/" + "help.txt") as file:
            file = file.readlines()
            h = [x.strip() for x in file]
            for x in range(len(h)):
                sleep(0.03)
                print(ccolors.green + h[x] + ccolors.end)
    elif name == "mass-mailer":
        massmailer.start(path)
    elif name == "hash-wordlist":
        wordlist2hash.start(path)
    elif name == "encrypt":
        dencrypt.encrypt(path, ppath)
    elif name == "decrypt":
        dencrypt.decrypt(path)
    else:
        print(ccolors.warn + "<!> Invalid command: " + name + ccolors.end)
