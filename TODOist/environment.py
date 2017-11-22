import yaml
from utils.apiLib import *

global app_data
app_data = yaml.load(open("../settings/config.yml"))

def before_all (context):
    print("************************ BEFORE ALL *************************************************")
    context.host = app_data['app']['host']
    context.root = app_data['app']['root']
    context.version = app_data['app']['version']
    context.token = app_data['user']['token']
    context.url=context.host+context.root+context.version
    ### Moved here otherwise being in steps definitions
    ### it will override the data sent by hooks
    context.id = None
    context.data = None
    context.method = None


def before_scenario(context, scenario):
    if 'insert_tasks' in scenario.tags:
        #Enviando directamente el json
        data={"content": "PreTest"}
        response=perform_post("tasks", None, data)
        json_response = response.json()
        print(json_response['id'])
        context.id=json_response['id']

def after_scenario(context, scenario):
    if 'delete_tasks' in scenario.tags:
        print(context.id)
        response=perform_delete("tasks",context.id)