from wifi_class import Wifi
import time
import sys

def add_net(cmd):
    """ add name="net_ssid" """
    r = []
    for i in range(len(cmd)):
        if cmd[i] == '"':
            r.append(i)
    return Wifi(cmd[r[0] + 1:r[1]], '00000000')

def connect_net(cmd,nets):
    """ connect id="net_id" """
    if len(nets) != 0:
        Wifi.disconnect()
        r=[]
        for i in range(len(cmd)):
            if cmd[i]=='"':
                r.append(i)
        id = int(cmd[r[0]+1:r[1]])
        while not (1 <= id <= len(nets)):
            id = int(input("input CORRECT net id:"))

        nets[id-1].connect()

        if Wifi.is_connected():
            print("sucsessuly connected to",nets[id-1].ssid)
        else:
            print("name or key is invalid")
    else:
        print("there is no avilable networks. add a single one.")


def show_nets(nets):
    """ avilable """
    if len(nets)!=0:
        print("Avilable networks")
        for i in range(len(nets)):
            if nets[i].valid==1:
                state='correct'
            else:
                state='incorrect'
            print('id=', i + 1, ' name=', nets[i].ssid, ' pass=', nets[i].key,' current pass is ',state, sep='')
    else:
        print("there is no avilable networks. add a single one.")










