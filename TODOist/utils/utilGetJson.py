import json
def getJson():
    with open('../data/allProjects.json') as json_data:
        data = json.load(json_data)
        json_data.close()
        return data