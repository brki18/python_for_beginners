import json
import yaml

# with open('sample.json') as json_file:
#     text = json.load(json_file)
#
#     print(text['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
#
# with open('created_json.json', 'x') as new_json:
#     content = {1: 'Welcome', 2: 'to',
#                3: 'Geeks', 4: 'for',
#                5: 'Geeks'}
#     json.dump(content, new_json)

# with open('example.yaml') as yaml_file:
#     content = yaml.safe_load(yaml_file)
#
#     print(type(content))
#     print(content['users']['marko']['job_title'])

with open('new_file.yaml', 'x') as new_yaml:
    document = {'name': 'Marko', 'age': 36}
    yaml.dump(document, new_yaml)
