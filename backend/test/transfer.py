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
    head = '''import torch.nn as nn
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
    end = '''
def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        data = data.view(data.size(0),28*28)
        
        #use adverserial data to train the defense model
        #adv_data = adv_attack(model, data, target, device=device)
        
        #clear gradients
        optimizer.zero_grad()
        
        #compute loss
        #loss = F.nll_loss(model(adv_data), target)
        loss = F.nll_loss(model(data), target)
        
        #get gradients and update
        loss.backward()
        optimizer.step()
        


#predict function
def eval_test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            data = data.view(data.size(0),28*28)
            output = model(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy

#main function, train the dataset and print train loss, test loss for each epoch
def train_model():
    model = Net().to(device)
    
    ################################################################################################
    ## Note: below is the place you need to edit to implement your own training algorithm
    ##       You can also edit the functions such as train(...). 
    ################################################################################################
    
    optimizer = optim.SGD(model.parameters(), lr=args.lr)
    for epoch in range(1, args.epochs + 1):
        start_time = time.time()
        
        #training
        train(args, model, device, train_loader, optimizer, epoch)
        
        #get trnloss and testloss
        trnloss, trnacc = eval_test(model, device, train_loader)
        
        #print trnloss and testloss
        print('Epoch '+str(epoch)+': '+str(int(time.time()-start_time))+'s', end=', ')
        print('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trnloss, 100. * trnacc), end=', ')
        
    return model
    '''
    f.write(end)
