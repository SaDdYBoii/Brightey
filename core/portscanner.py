import socket
import threading
from core import ccolors
import os


listening = ""


def check_port(host_ip, host_port):
    global listening
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(1)
    try:
        s.connect((host_ip, host_port))
        listening = listening + " " + str(host_port)
    except:
        pass


def scan_ports(host):

    threads = []

    for i in range(1000):
        t = threading.Thread(target=check_port, args=(host, i))
        threads.append(t)

    for i in range(1000):
        threads[i].start()
        os.system("clear")

    for i in range(1000):
        threads[i].join()
    print(ccolors.green + "Listening Ports: " + listening + ccolors.end)


def main():
    host_ip = input(ccolors.red + "[Host]> " + ccolors.end)
    scan_ports(host_ip)
