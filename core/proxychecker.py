import os
from core import ccolors
try:
    import urllib3
except:
    os.system("pip install urllib3")
import socket


def start(path):
    global proxy_list, working
    working = 0
    filename = path + str(input(ccolors.red + "[Filename]> " + ccolors.end))
    socket.setdefaulttimeout(0.5)
    if os.path.exists(filename):
        try:
            with open(filename) as file:
                proxy_list = file.readlines()
            proxy_list = [x.strip() for x in proxy_list]
            file.close()
        except:
            print(ccolors.warn + "<!> File format is invalid" + ccolors.end)
            return None
    else:
        print(ccolors.warn + "<!> Directory " + filename + " does not exists" + ccolors.end)
        return None

    def check_proxy(proxy):
        global working
        try:
            proxy_handler = urllib3.ProxyManager("http://" + proxy)
            proxy_handler.request('GET', 'http://google.com')
            working += 1
            print(ccolors.blue + str(working) + " of " + str(len(proxy_list)) + " proxies are working" + ccolors.end)
        except:
            print(ccolors.blue + str(working) + " of " + str(len(proxy_list)) + " proxies are working" + ccolors.end)
            proxy_list.remove(proxy)
            return True

    for px in proxy_list:
        check_proxy(px)

    while True:
        answer = str(input(ccolors.green + "[Do you wanna overwrite your current proxy list with working proxies only? {Yes/no}]> " + ccolors.end))
        if answer == "Yes":
            file = open(filename, 'w')
            for line in proxy_list:
                file.write("%s\n" % line)
            file.close()
            return None
        elif answer == "no":
            return None
