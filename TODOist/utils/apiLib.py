import requests
import json
from environment import *

def perform_gets(endpoint, id=None):
    url = create_url(endpoint, id)
    return requests.get(url)


def perform_post(endpoint, id=None, body=None):
    url = create_url(endpoint, id)
    r = requests.post(url, json = body)
    return r

def perform_close(endpoint, id):
    url= create_url_close(endpoint, id)
    return requests.post(url)

def perform_reopen(endpoint, id):
    url= create_url_reopen(endpoint, id)
    return requests.post(url)

def perform_delete(endpoint, id):
    url = create_url(endpoint, id)
    return requests.delete(url)

def create_url(endpoint, id=None):
    url = app_data['app']['host'] + app_data['app']['root'] + app_data['app']['version'] + "/" + endpoint
    if id != None:
        url += "/" + str(id)
    url += "?token=" + app_data['user']['token']
    return url

def create_url_close(endpoint, id):
    url = app_data['app']['host'] + app_data['app']['root'] + app_data['app']['version'] + "/" + endpoint+ "/" + str(id)+"/close"
    url += "?token=" + app_data['user']['token']
    return url

def create_url_reopen(endpoint, id):
    url = app_data['app']['host'] + app_data['app']['root'] + app_data['app']['version'] + "/" + endpoint+ "/" + str(id)+"/reopen"
    url += "?token=" + app_data['user']['token']
    return url

def perform_request(method, endpoint, id=None, data=None):
    r = None
    if method.upper() == 'GET':
        r = perform_gets(endpoint, id)
    elif method.upper()=='DELETE':
        r = perform_delete(endpoint, id)
    elif method=='POST' or method.upper()=='UPDATE':
        r = perform_post(endpoint, id, data)
    elif method.upper() == 'CLOSE':
        r = perform_close(endpoint, id)
    elif method.upper() == 'REOPEN':
        r = perform_reopen(endpoint, id)
    else:
        print("Not implemented method")

    return r

