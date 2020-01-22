import requests
import time
import busio
import adafruit_gps
import serial

from api_shared import post_status

uart = serial.Serial("/dev/cu.SLAB_USBtoUART", baudrate=9600, timeout=10)

# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)

# Turn on the basic GGA and RMC info
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to once a second (1hz)
gps.send_command(b'PMTK220,1000')

last_print = time.monotonic()
has_fix = False
while True:
    new_data = gps.update()

    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            has_fix = False
            post_status(category='GPS', status='Waiting for fix...')
            print('Waiting for fix...')
            continue

        if has_fix == False:
            has_fix = True
            post_status(category='GPS', status='Successful satellite fix')

        data = {
        'latitude': gps.altitude_m,
        'longitude': gps.latitude,
        'altitude': gps.altitude_m,
        'nauts': gps.speed_knots,
        'angle': gps.track_angle_deg,
        'satellites': gps.satellites,
        'timestamp': gps.timestamp_utc,
        'height': gps.height_geoid
        }

        try:
            requests.post('http://127.0.0.1/local/gps', json=data)
        except:
            print('Couldn\'t POST data to local. Throwing out data...')
