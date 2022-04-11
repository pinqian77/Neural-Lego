import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import torchvision
from torchvision import transforms
import time
import json
from model import Net
# setup training parameters
#parser = argparse.ArgumentParser(description='PyTorch MNIST Training')
#parser.add_argument('--batch-size', type=int, default=128, metavar='N',
#                    help='input batch size for training (default: 128)')
#parser.add_argument('--test-batch-size', type=int, default=128, metavar='N',
#                    help='input batch size for testing (default: 128)')
#parser.add_argument('--epochs', type=int, default=10, metavar='N',
#                    help='number of epochs to train')
#parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
#                    help='learning rate')
#parser.add_argument('--no-cuda', action='store_true', default=False,
#                    help='disables CUDA training')
#parser.add_argument('--seed', type=int, default=1, metavar='S',
#                    help='random seed (default: 1)')
#
#
#args = parser.parse_args(args=[]) 
with open("hyper.json", 'r') as f:
    args = json.load(f)

# judge cuda is available or not
use_cuda = not args.no_cuda and torch.cuda.is_available()
#device = torch.device("cuda" if use_cuda else "cpu")
device = torch.device("cpu")

torch.manual_seed(args.seed)
kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}

############################################################################
################    don't change the below code    #####################
############################################################################
train_set = torchvision.datasets.FashionMNIST(root='data', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True)

test_set = torchvision.datasets.FashionMNIST(root='data', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))
test_loader = DataLoader(test_set, batch_size=args.batch_size, shuffle=True)

##############################################################################
#############    end of "don't change the below code"   ######################
##############################################################################

#train function, you can use adversarial training
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



################################################################################################
## Note: below is for testing/debugging purpose, please comment them out in the submission file
################################################################################################
model = train_model()

