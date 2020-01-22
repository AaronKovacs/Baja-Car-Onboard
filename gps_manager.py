import sh
from sh import git
import time
import os, sys
import subprocess as sp

extProc = None 

if __name__ == "__main__":

    if extProc is None:
        print("*********** Started GPS **************")                                                     
        extProc = sp.Popen(['python3', '/home/pi/Baja-Car-Onboard/gps.py'])

    if sp.Popen.poll(extProc) is not None:
        print("*********** Error! GPS Restarted **************")                                                     
        extProc = sp.Popen(['python3', '/home/pi/Baja-Car-Onboard/gps.py'])
                                                                                                                   
    time.sleep(10) # Check every 30 seconds