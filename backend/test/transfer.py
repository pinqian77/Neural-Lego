import json
import os

def FC(input_size, output_size):
    return "FC\n"
def ReLU():
    return "RELU\n"

with open(os.path.join('.','example.json'), 'r') as f:
    List = json.load(f)

nodeList = List['nodeDataArray']
linkList = List['linkDataArray']

nodedict = {}
linkdict = {}
start = 0
end = 0
for node in nodeList:
    nodedict[node['key']] = {'category':node['category'], 'para':node['reasonsList']}
    if node['category'] == "Data":
        start = node['key']
    if node['category'] == "End":
        end = node['key']

for link in linkList:
    linkdict[link['from']] =  link['to']

#if start == 0 or end == 0:
#    raise 

pointer = linkdict[start]
with open('model.py', 'w') as f:
    f.write("import torch \n
import torch.nn as nn \n
import torch.nn.functional as F \n
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import torchvision
from torchvision import transforms
import time
import json
")
    while pointer != end:
        if nodedict[pointer]['category'] == 'FC':
            f.write(FC(nodedict[pointer]['para'][0]['text1'], nodedict[pointer]['para'][0]['text3']))
        elif nodedict[pointer]['category'] == 'ReLU':
            f.write(ReLU())
        pointer = linkdict[pointer]
