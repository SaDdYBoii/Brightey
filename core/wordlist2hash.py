import hashlib
from core import ccolors
import os
from threading import Thread


def string2hash(string):
    md = hashlib.md5()
    md.update(string.encode("utf-8"))
    hashes.append(md.hexdigest())


def start(path):
    global hashes
    hashes = []
    thr = []
    filename = path + str(input(ccolors.red + "[Filename]> " + ccolors.end))
    if os.path.exists(filename):
        try:
            with open(filename) as file:
                wordlist = file.readlines()
            wordlist = [x.strip() for x in wordlist]
            wordlist = list(set(wordlist))
            file.close()
        except:
            print(ccolors.warn + "<!> File format is invalid" + ccolors.end)
            return None
    else:
        print(ccolors.warn + "<!> Directory " + filename + " does not exists" + ccolors.end)
        return None

    pw_count = str(len(wordlist))
    hashed = 0
    for pw in wordlist:
        t = Thread(target=string2hash(pw), args=pw)
        thr.append(t)
    for pw in wordlist:
        hashed += 1
        thr[wordlist.index(pw)].start()
        os.system("clear")
        print(ccolors.blue + str(hashed) + " of " + pw_count + " passwords hashed" + ccolors.end)
        string2hash(pw)
    for pw in wordlist:
        thr[wordlist.index(pw)].join()

    print(ccolors.green + "Wordlist hashed successfully!" + ccolors.end)
    file = open(filename + "-hashed", 'w')
    for line in hashes:
        file.write("%s\n" % line)
    file.close()
