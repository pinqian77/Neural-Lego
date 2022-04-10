import json
import os

with open(os.path.join('.','example.json'), 'r') as f:
    List = json.load(f)

nodeList = List['nodeDataArray']
linkList = List['linkDataArray']
start = 0
end = 0
for node in nodeList:
    if node['category'] == "Data":
        start = node['key']
    if node['category'] == "End":
        End = node['key']


