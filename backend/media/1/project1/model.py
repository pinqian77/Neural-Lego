import torch.nn.functional as F
import torch.nn as nn

class Net(nn.Module):
    
	def __init__(self):
		super(Net, self).__init__()
		self.fc3 = nn.Linear(4, 32)
		self.fc5 = nn.Linear(32, 3)

	def forward(self, x):
		x = self.fc3(x)
		x = F.relu(x)
		x = self.fc5(x)
		return x

