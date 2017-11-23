import requests
import json
from environment import *

#def perform_request(method, endpoint,body=None,headers=None):
    ##enpoint shoudl be already completed
#    if method=='GET':
#        requests.get(enpoint,headers)
#    elif method=='POST':
#        request.post(enpoint,payload=body,headers=headers)
#'''
#r = requests.get('https://beta.todoist.com/API/v8/projects?token=f50c6c99ce6a05edd52e71029dd0a320966b07a7')
#print ("Values \n", r.text)
#print ("Jason \n", r.json())
#print ("CONTENT \n", r.content)
#print ("CODE \n", r.status_code)

#'''
#payload = {"name": "Kate's Project"}
#r = requests.post("https://beta.todoist.com/API/v8/projects?token=f50c6c99ce6a05edd52e71029dd0a320966b07a7", data=payload)
#print (r.text)
#print (r.json)


#"https://beta.todoist.com/API/v8/projects/2168814383?token=$token"
#r = requests.get("https://beta.todoist.com/API/v8/projects/2168814383?token=f50c6c99ce6a05edd52e71029dd0a320966b07a7")

#print (r.text)
#print (r.json)

# def perform_get(endpoint):
#     url = create_url(endpoint)
#     return requests.get(url)

def perform_gets(endpoint, id=None):
    url = create_url(endpoint, id)
    return requests.get(url)

# def perform_get_by_id(endpoint, id=None):
#     url = create_url(endpoint, id)
#     return requests.get(url)

def perform_post(endpoint, id=None, body=None):
    url = create_url(endpoint, id)
    #try:
        #r = requests.post(url, data=json.dumps(body))
    r = requests.post(url, json = body)
    #except requests.exceptions.RequestException as e:
    #    print(e)
    return r

def perform_delete(endpoint, id):
    url = create_url(endpoint, id)
    return requests.delete(url)

def create_url(endpoint, id=None):
    url = app_data['app']['host'] + app_data['app']['root'] + app_data['app']['version'] + "/" + endpoint
    if id != None:
        url += "/" + str(id)
    url += "?token=" + app_data['user']['token']
    print(url)
    return url

def perform_request(method, endpoint, id=None, data=None):
    r = None
    if method.upper() == 'GET':
        r = perform_gets(endpoint, id)
        print(r.json())
    elif method.upper()=='DELETE':
        perform_delete(endpoint, id)
    elif method=='POST' or method.upper()=='UPDATE':
        r = perform_post(endpoint, id, data)
    else:
        print("Noy implemented method")

    return r

