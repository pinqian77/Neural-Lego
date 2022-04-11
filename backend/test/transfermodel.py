import json
import os

def FC(input_size, output_size, init, forward, pointer):

    string = "self.fc"+str(-1*pointer)+" = nn.Linear("+str(input_size)+", "+str(output_size)+")"
    string = "\t\t"+string + "\n"
    init += string
    string = "x = self.fc" + str(-1*pointer) + "(x)"
    string = "\t\t" + string + "\n"
    forward += string
    return init, forward
def ReLU(forward):
    forward += "\t\tx = F.relu(x)\n"
    return forward

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

################################################## model date
pointer = linkdict[start]
with open('model.py', 'w') as f:
    head = '''import torch.nn.functional as F
import torch.nn as nn
import torch.nn.functional as F
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
'''
    f.write(head+"\n")
    init, forward = "\tdef __init__(self):\n\t\tsuper(Net, self).__init__()\n", "\tdef forward(self, x):\n"
    while pointer != end:
        if nodedict[pointer]['category'] == 'FC':
            init, forward = FC(nodedict[pointer]['para'][0]['text1'], nodedict[pointer]['para'][0]['text3'], init, forward, pointer)
        elif nodedict[pointer]['category'] == 'ReLU':
            forward = ReLU(forward)
        pointer = linkdict[pointer]
    forward += "\t\treturn x\n"
    f.write(init+"\n")
    f.write(forward+"\n")
    f.close()
