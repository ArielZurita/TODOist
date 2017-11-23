import yaml
from utils.apiLib import *
import json

global app_data
app_data = yaml.load(open("../settings/config.yml"))
app_data2 = yaml.load(open("../data/data.yml"))

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

    if 'update_project' in scenario.tags:
        #Leyendo datos del file2
        data=app_data2['project']['project_name_new']
        id=app_data2['project']['project_id']
        response=perform_post("projects",id,data)

    if 'get_project' in scenario.tags:
        #Leyendo datos del file2
        id=app_data2['project']['project_id']
        response=perform_gets("projects",id)

    if ('get_label' in scenario.tags) or ('delete_label' in scenario.tags):
        #Before getting or deleting a label I have to create one
        data = app_data2['labels']['label_name']
        response = perform_post("labels", None, data)
        json_response = response.json()
        print(json_response['id'])
        context.id = json_response['id']


def after_scenario(context, scenario):
    if 'delete_tasks' in scenario.tags:
        print(context.id)
        response=perform_delete("tasks",context.id)
    if 'get_label' in scenario.tags:
        # After getting the label I have to remove it
        print(context.id)
        response = perform_delete("labels", context.id)

    #Commented in order to avoid delete a project
    # if 'delete_project' in scenario.tags:
    #     print(context.id)
    #     response=perform_delete("projects",context.id)

