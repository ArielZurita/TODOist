import yaml
from utils.apiLib import *
from utils.utilGetJson import *
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
    context.id = None
    context.data = None
    context.method = None

def before_scenario(context, scenario):

    if 'insert_tasks' in scenario.tags:
        context.data = app_data2['task1']['task_name']
        response=perform_post("tasks", None, context.data)
        json_response = response.json()
        print(json_response['id'])
        context.id=json_response['id']

    if 'close_tasks' in scenario.tags:
        data = app_data2['task1']['task_name']
        response = perform_post("tasks", None, data)
        json_response1 = response.json()
        context.id = json_response1['id']
        response2 = perform_close("tasks", context.id)


    if ('update_project' in scenario.tags) or ('get_project' in scenario.tags) or ('delete_project' in scenario.tags):
        #Before getting a Project I have to create one to be dinamic
        #Creating a new Project
        #Gathering data from file2
        data=app_data2['project']['project_name_new']
        response=perform_post("projects",None,data)
        json_response = response.json()
        print("_____________________________________________________________________________________")
        #Getting the id of new Project
        context.id=json_response['id']

    if 'get_all_projects' in scenario.tags:
        response = perform_gets("projects")
        context.data = getJson()

    if ('get_label' in scenario.tags) or ('delete_label' in scenario.tags) or ('update_label' in scenario.tags):
        #Before getting or deleting a label I have to create one
        data = app_data2['labels']['label_name']
        response = perform_post("labels", None, data)
        json_response = response.json()
        print(json_response['id'])
        context.id = json_response['id']

def after_scenario(context, scenario):
    if 'delete_tasks' in scenario.tags:
        response=perform_delete("tasks",context.id)

    if ('create_label'in scenario.tags) or ('get_label' in scenario.tags) or ('update_label' in scenario.tags):
        # After getting the label I have to remove it
        response = perform_delete("labels", context.id)

    if 'delete_project' in scenario.tags:
        # After getting, updating the Project I have to remove it
        response=perform_delete("projects",context.id)

