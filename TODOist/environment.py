import yaml

global app_data
app_data = yaml.load(open("../settings/config.yml"))

def before_all (context):
    print("************************ BEFORE ALL *************************************************")
    context.host = app_data['host']
    context.root = app_data['root']
    context.version = app_data['version']
    context.token = app_data['token']
    context.url=context.host+context.root+context.version


def before_scenario(context, scenario):
    if 'insert_tasks' in scenario.tags:
        data=app_data['task_name']
        url=context.url,"/task"
        response=performs_post(url,data)
        context.id=find_value(response, "id")
