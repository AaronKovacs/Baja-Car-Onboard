import time
import requests
import io
import socket
import os

while True:
    time.sleep(10)
    try: 
        gw = os.popen("ip -4 route show default").read().split()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((gw[2], 0))
        host_ip = s.getsockname()[0]
        gateway = gw[2]
        host_name = socket.gethostname()

        value_str = "[Baja-Car] Host: %s IP: %s" % (host_name, host_ip)
        try:
            requests.post('http://prod.ft7mz3prg3.us-east-1.elasticbeanstalk.com/misc/text', json={'text': value_str})
            print("Sent IP Address")
        except:
            print('Couldn\'t POST data to remote. Throwing out text...')
        except: 
            print("Unable to get Hostname and IP") 
    
