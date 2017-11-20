import requests

def perform_request(method, endpoint,body=None,headers=None):
    ##enpoint shoudl be already completed
    if method=='GET':
        requests.get(enpoint,headers)
    elif method=='POST':
        request.post(enpoint,payload=body,headers=headers)
'''
r = requests.get('https://beta.todoist.com/API/v8/projects?token=f50c6c99ce6a05edd52e71029dd0a320966b07a7')
print ("Values \n", r.text)
print ("Jason \n", r.json())
print ("CONTENT \n", r.content)
print ("CODE \n", r.status_code)

'''
payload = {"name": "Kate's Project"}
r = requests.post("https://beta.todoist.com/API/v8/projects?token=f50c6c99ce6a05edd52e71029dd0a320966b07a7", data=payload)
print (r.text)
print (r.json)


#"https://beta.todoist.com/API/v8/projects/2168814383?token=$token"
r = requests.get("https://beta.todoist.com/API/v8/projects/2168814383?token=f50c6c99ce6a05edd52e71029dd0a320966b07a7")

print (r.text)
print (r.json)
