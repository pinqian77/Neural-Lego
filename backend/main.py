import torch.nn as nn
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

with open("hyper.json", 'r') as f:
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

X, y = readcsv("iri"+args['dataset'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = args['seed'])
X_train, y_train = torch.stack([torch.Tensor(i) for i in X_train]), torch.stack([torch.Tensor([i]) for i in y_train])
X_test, y_test = torch.stack([torch.Tensor(i) for i in X_test]), torch.stack([torch.Tensor([i]) for i in y_test])
y_train, y_test = y_train.squeeze().type(torch.LongTensor), y_test.squeeze().type(torch.LongTensor)
train_set = Data.TensorDataset(X_train, y_train)
test_set = Data.TensorDataset(X_test, y_test)
train_loader = Data.DataLoader(train_set, batch_size=args['batch_size'], shuffle=True)
test_loader = Data.DataLoader(test_set, batch_size=args['test_batch_size'], shuffle=True)

    
