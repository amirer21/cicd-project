#!/usr/bin/env python3
# ToDo: Still Python2-compatible

import os
import platform
import sys

def ipcheck():
    
    ping_param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    
    resultado = os.popen("ping " + ping_param + " " + pop).read()
    
    if "TTL=" in resultado:
        print("System " + str(pop) + " is UP !")
    else:
        raise Exception('Server Down') 

if (__name__ == '__main__'):
    pop = sys.argv[1]
    ipcheck()
