from core import ccolors
import glob
import os
import hashlib


def integer2hash(integer):
        md = hashlib.md5()
        md.update(chr(integer).encode("utf-8"))
        return md.hexdigest()


def encrypt_file(filename, pw):
    try:
        with open(filename) as f:
            file = f.readlines()
            file = [x.strip() for x in file]
            f.close()
            if file[0] == "True":
                print(ccolors.warn + "<!> This file is already encrypted" + ccolors.end)
                return None
            to_file = open(filename, 'w')
            to_file.write("%s\n" % "True")
            to_file.write("%s\n" % integer2hash(pw))
            print(ccolors.blue + "Encrypting file " + filename + ccolors.end)
            for i in file:
                c = [chr(ord(ch) + pw) for ch in i]
                char = ""
                for x in c:
                    char = char + x
                to_file.write("%s\n" % char)
            to_file.close()
    except:
        print(ccolors.warn + "<!> File " + filename + " has invalid format" + ccolors.end)


def encrypt(path, ppath):
    not_answered = True
    while not_answered:
        if path != ppath and path != ppath + "core/":
            print(ccolors.green + "You can decrypt your files only using this software!" + ccolors.end)
            ask = str(input(ccolors.red + "[Do you want to encrypt " + path + " ? {Yes/no}]> " + ccolors.end))
            if ask == "Yes":
                not_answered = False
                try:
                    password = int(input(ccolors.red + "[Password]> " + ccolors.end))
                    if len(str(password)) > 6:
                        print(ccolors.warn + "<!> Password length cant be more than 6" + ccolors.end)
                        return None
                except:
                    print(ccolors.warn + "<!> Password must be numbers only" + ccolors.end)
                    return None
                for fpath in glob.iglob(path + "**/", recursive=True):
                        files = glob.glob(fpath + "*")
                        for x in files:
                            if os.path.isfile(x):
                                encrypt_file(x, password)
                print(ccolors.green + "Files has been encrypted" + ccolors.end)
            elif ask == "no":
                return None
        else:
            not_answered = False
            print(ccolors.warn + "<!> You cant encrypt Brightey directory")


def decrypt(path):
    try:
        pw = int(input(ccolors.red + "[Password]> " + ccolors.end))
    except:
        print(ccolors.warn + "<!> Password must be numbers only" + ccolors.end)
        return None
    for fpath in glob.iglob(path + "**/", recursive=True):
        files = glob.glob(fpath + "*")
        for filename in files:
            try:
                with open(filename) as c:
                    df = c.readlines()
                    df = [x.strip() for x in df]
                    c.close()
                    if df[0] != "True":
                        print(ccolors.warn + "<!> This file is not encrypted" + ccolors.end)
                    else:
                        if df[1] != integer2hash(pw):
                            print(ccolors.warn + "<!> Wrong password" + ccolors.end)
                            return None
                        print(ccolors.blue + "Decrypting file " + filename + ccolors.end)
                        df.remove("True")
                        df.remove(integer2hash(pw))
                        to_file = open(filename, 'w')
                        for i in df:
                            line = [chr(ord(ch) - pw) for ch in i]
                            char = ""
                            for x in line:
                                char = char + x
                            to_file.write("%s\n" % char)
                        to_file.close()
            except:
                if os.path.isfile(fpath):
                    print(ccolors.warn + "<!> File " + filename + " has invalid format" + ccolors.end)
