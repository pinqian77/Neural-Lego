import json
import subprocess, time
import os
def model(project_path: str , pid: str):
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
    
    with open(os.path.join(project_path,pid+'.json'), 'r') as f:
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
    if len(linkList) == 0 or end == 0:
        return
    
    #if start == 0 or end == 0:
    #    raise 
    
    ################################################## model date
    pointer = linkdict[start]
    with open(os.path.join(project_path, "model.py"), 'w') as f:
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
def main(project_path, data_path, pid):
    with open(os.path.join(project_path, 'main.py'), 'w') as f:
        head = '''import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as Data
import torch.optim as optim
import torchvision
import csv
import pandas as pd
from torchvision import transforms
import time
import json
from model import Net

project_path = "%s"
with open("hyperparameter.json", 'r') as f:
    args = json.load(f)
#use_cuda = not args.no_cuda and torch.cuda.is_available()
#device = torch.device("cuda" if use_cuda else "cpu")
device = torch.device("cpu")

torch.manual_seed(args['seed'])
#kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}
kwargs = {}

def readcsv(files):
    csvfile = pd.read_csv(files)
    columns = csvfile.columns
    label = csvfile[columns[-1]].unique()
    map = {}
    for index, item in enumerate(label):
        map[item] = index
    csvfile[columns[-1]] = csvfile[columns[-1]].map(map)
    x = csvfile.drop(columns[-1], axis=1).values
    y = csvfile[columns[-1]].values
    return x, y

X, y = readcsv("%s")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = args['seed'])
X_train, y_train = torch.stack([torch.Tensor(i) for i in X_train]), torch.stack([torch.Tensor([i]) for i in y_train])
X_test, y_test = torch.stack([torch.Tensor(i) for i in X_test]), torch.stack([torch.Tensor([i]) for i in y_test])
y_train, y_test = y_train.squeeze().type(torch.LongTensor), y_test.squeeze().type(torch.LongTensor)
train_set = Data.TensorDataset(X_train, y_train)
test_set = Data.TensorDataset(X_test, y_test)
train_loader = Data.DataLoader(train_set, batch_size=args['batch_size'], shuffle=True)
test_loader = Data.DataLoader(test_set, batch_size=args['test_batch_size'], shuffle=True)

    '''%(project_path, data_path)
        f.write(head+"\n")

        endfile = '''def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
#        target = target.squeeze().type(torch.LongTensor)
        
        optimizer.zero_grad()
        
        loss = nn.CrossEntropyLoss()(model(data), target)
        
        loss.backward()
        optimizer.step()
def writeAuc(target_list, pred_list, path):
    for i in pred_list:
        print(i.shape)
    pred_all, target_all = torch.cat([i for i in pred_list], dim=0), torch.cat([i for i in target_list], dim=0)
    print(pred_all.shape)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(3):
        fpr[i], tpr[i], _ = roc_curve(pred_all[:, i], target_all[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(pred.ravel(), target.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    
    plt.figure()
    lw = 2
    plt.plot(fpr[2], tpr[2], color='darkorange',
            lw=lw, label='ROC curve (area = {:.2f}%)'.format(roc_auc[2]))
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.savefig(path)

def writeLossAcc(loss, acc, path):
    plt.subplot(1, 2, 1)
    plt.plot(acc, label = "Training Accuracy")
    plt.title("Accuracy")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(loss, label = "Training Loss")
    plt.title("Loss")
    plt.legend()
    plt.savefig(path)


def eval_test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    target_list = []
    pred_list = []
    with torch.no_grad():
        for data, target in test_loader:
#            target = target.squeeze().type(torch.LongTensor)
            output = model(data)
            test_loss += nn.CrossEntropyLoss()(output, target).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
            target = nn.functional.one_hot(target, num_classes = 3)
            pred = nn.functional.one_hot(pred, num_classes=3).squeeze()
            target_list.append(target)
            pred_list.append(pred)

    writeAuc(target_list, pred_list, os.path.join(project_path, "auc.png"))
    test_loss /= len(test_loader.dataset)
    test_accuracy = correct / len(test_loader.dataset)
    return test_loss, test_accuracy

def train_model():
    model = Net().to(device)
    
    optimizer = optim.SGD(model.parameters(), lr=args['lr'])
    
    trnlossList, trnaccList = [], []
    for epoch in range(1, args['epoch'] + 1):
        start_time = time.time()
        
        train(args, model, device, train_loader, optimizer, epoch)
        
        trnloss, trnacc = eval_test(model, device, train_loader)
        trnlossList.append(trnloss)
        trnaccList.append(trnacc)
        writeAcc(trnlossList, trnaccList, os.path.join(project_path, "acc.png"))
        print('Epoch '+str(epoch)+': '+str(int(time.time()-start_time))+'s', end=', ')
        print('trn_loss: {:.4f}, trn_acc: {:.2f}%'.format(trnloss, 100. * trnacc), end=', ')
        with open(os.path.join(project_path, "output"), 'w'):
            f.write(str(epoch))
        
    return model
model = train_model()
'''
        f.write(endfile)
        print(head)
        print(endfile)

from subprocess import PIPE
def cmd(command):
    print(command)
    subprocess.Popen(["ls -la"], shell = True)
    subp = subprocess.Popen(command, shell = True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = subp.communicate()
    print(subp)
