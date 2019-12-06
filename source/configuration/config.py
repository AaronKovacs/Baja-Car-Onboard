import os

# General
PAGE_SIZE = 20

# Database
PROD_DB = '/home/pi/Onboard/database.db'

REMOTE = 'http://prod-env.bb389wsu7v.us-east-1.elasticbeanstalk.com'

def DB_URL():
    return PROD_DB
