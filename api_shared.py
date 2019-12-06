import requests

REMOTE = 'http://prod-env.bb389wsu7v.us-east-1.elasticbeanstalk.com'

def post_status(category, status):
    try:
        requests.post(REMOTE + '/car/status', json={'category': category, 'status': status})
    except:
        print('Couldn\'t POST data to remote. Throwing out status...')
