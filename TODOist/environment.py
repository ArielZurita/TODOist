import yaml

global app_data
app_data = yaml.load(open("../settings/config.yml"))

def before_all (context):
    print("************************ BEFORE ALL *************************************************")
    context.host = app_data['host']
    context.root = app_data['root']
    context.version = app_data['version']
    context.token = app_data['token']
