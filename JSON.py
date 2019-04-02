import json
from pprint import pprint as pp
from var_dump import var_dump

file_name = "D:\\WORK\\_projects\\Python_projects\\Convertor\\Trello_blackboard.json"

with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f)
var_dump(data)
# for list in data['root']['cards']['items']['item']:
# var_dump(list)
# with open('json_var_dump.txt','w') as v:
# v.write((vd(data)))
