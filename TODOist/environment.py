import yaml

global app_data
app_data = yaml.load(open("../settings/config.yml"))
app_data2 = yaml.load(open("../data/data.yml"))

def before_all (context):
    print("************************ BEFORE ALL ************************ ")
    context.host = app_data['app']['host']
    context.root = app_data['app']['root']
    context.version = app_data['app']['version']
    context.token = app_data['user']['token']
    context.url=context.host+context.root+context.version

def before_scenario(context, scenario):
    print("************************ BEFORE SCENARIO ************************ ")
    if 'get_project' in scenario.tags:
        data=app_data2['project']['project_id']
        url=context.url,"/projects"

    if 'update_project' in scenario.tags:
        data=app_data2['project']['project_name_new']
        url=context.url,"/projects"

    if 'delete_project' in scenario.tags:
        data=app_data2['project']['project_id']
        url=context.url,"/projects"
