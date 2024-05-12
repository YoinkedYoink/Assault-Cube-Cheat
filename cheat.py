from pymem import Pymem
from pymem.ptypes import RemotePointer
import time
import sys
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
pm = None
print("╔════════════════════════════════════════════════════╗\n║  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄ ║\n║ █    █   █ █   █  █  █  █ █ █ ▐  ▄▀   ▐ █    █   █ ║\n║ ▐     ▀▄▀  ▐   █  ▐  ▐  █  ▀█   █▄▄▄▄▄  ▐     ▀▄▀  ║\n║      ▄▀ █      █       █   █    █    ▌       ▄▀ █  ║\n║     █  ▄▀   ▄▀▀▀▀▀▄  ▄▀   █    ▄▀▄▄▄▄       █  ▄▀  ║\n║   ▄▀  ▄▀   █       █ █    ▐    █    ▐     ▄▀  ▄▀   ║\n║  █    ▐    ▐       ▐ ▐         ▐         █    ▐    ║\n╚════════════════════════════════════════════════════╝\n\n")

while pm == None:
    try:
        pm = Pymem("ac_client.exe")
        cls()
        print("╔════════════════════════════════════════════════════╗\n║  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄ ║\n║ █    █   █ █   █  █  █  █ █ █ ▐  ▄▀   ▐ █    █   █ ║\n║ ▐     ▀▄▀  ▐   █  ▐  ▐  █  ▀█   █▄▄▄▄▄  ▐     ▀▄▀  ║\n║      ▄▀ █      █       █   █    █    ▌       ▄▀ █  ║\n║     █  ▄▀   ▄▀▀▀▀▀▄  ▄▀   █    ▄▀▄▄▄▄       █  ▄▀  ║\n║   ▄▀  ▄▀   █       █ █    ▐    █    ▐     ▄▀  ▄▀   ║\n║  █    ▐    ▐       ▐ ▐         ▐         █    ▐    ║\n╚════════════════════════════════════════════════════╝\n\n")
        print("                 !!! Attatched !!!                ")
        time.sleep(3)
    except:
        chars = "/—\|" 
        for char in chars:
            sys.stdout.write("\r                 "+ char +" Open Assault Cube "+char+"               ")
            time.sleep(0.25)
            sys.stdout.flush()

cls()

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset

playerbase = getPointerAddress(pm.base_address + 0x17E0A8, offsets=[0])
#entitylist = getPointerAddress(pm.base_address + 0x18AC04, offsets=[0])


def printStats(entityAddr):
    print("\n    "+str(entityAddr)+"    ")
    print("Name: " + str(pm.read_string(entityAddr + 0x205, 16)))
    print("Health: " + str(pm.read_int(entityAddr + 0xEC)))
    print("XYZ: "+ str(pm.read_float(entityAddr + 0x2C)) + " | " + str(pm.read_float(entityAddr + 0x30)) + " | " + str(pm.read_float(entityAddr + 0x28)))


while True:
    #Player Iterator following the txt file
    ecxAddr = getPointerAddress(pm.base_address + 0x18AC00, offsets=[0])
    maxPlayers = pm.read_int(pm.base_address + 0x18AC0C)
    entityList = getPointerAddress(pm.base_address + 0x18AC04, offsets=[0])

    for i in range(0x0, maxPlayers, 0x1):
        playerAddr = pm.read_int(entityList+(i*4))
        if not playerAddr == 0x0:
            if pm.read_int(playerAddr+0x76) != 0x2:
                if pm.read_int(playerAddr+0x76) != 0x5:
                    if pm.read_int(ecxAddr+0x76) == 0x5:
                        if pm.read_uint(ecxAddr+0x318) <= 0x0:
                            printStats(playerAddr)
                    else:
                        if pm.read_int(playerAddr+0x76) != 0x1:
                            printStats(playerAddr)
                        elif pm.read_uint(ecxAddr+0x318) <= 0x0:
                            printStats(playerAddr)
                        elif pm.read_uint(ecxAddr+0x318) <= 0x2:
                            printStats(playerAddr)
                        elif not pm.read_int(ecxAddr+0x31C) == i:
                            printStats(playerAddr)
                        else:
                            pass
                else:
                    pass
            else:
                pass
        else:
            pass
    cls()