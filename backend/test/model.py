import torch.nn as nn
import torch.nn.functional as F
class Net(nn.Module):

	def __init__(self):
		super(Net, self).__init__()
		self.fc3 = nn.Linear(512, 128)

	def forward(self, x):
		x = self.fc3(x)
		x = F.relu(x)
		return x


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
    
