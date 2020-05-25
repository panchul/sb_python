#!/usr/bin/env python
#
# A script to run the classic PyTorch classifier on popular iris dataset.
#
# $ python3 basic_classifier_GPU.py
# 

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt
# for Jupyter notebooks might want this
# %matplotlib inline
## it translates into
## get_ipython().run_line_magic('matplotlib', 'inline')

class Model(nn.Module):
    def __init__(self, in_features=4, h1=8, h2=9, out_features=3):
        super().__init__()
        self.fc1 = nn.Linear(in_features,h1)    # input layer
        self.fc2 = nn.Linear(h1, h2)            # hidden layer
        self.out = nn.Linear(h2, out_features)  # output layer

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)
        return x

#torch.manual_seed(123)
non_gpu_model = Model()

# From the discussions here: discuss.pytorch.org/t/how-to-check-if-model-is-on-cuda
# next(model.parameters()).is_cuda
# False

gpumodel = non_gpu_model.cuda()

# next(gpumodel.parameters()).is_cuda
# True

print(f'Getting data into the dataframe')

df = pd.read_csv('iris.csv')

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,7))
fig.tight_layout()

plots = [(0,1),(2,3),(0,2),(1,3)]
colors = ['b', 'r', 'g']
labels = ['Iris setosa','Iris virginica','Iris versicolor']

for i, ax in enumerate(axes.flat):
    for j in range(3):
        x = df.columns[plots[i][0]]
        y = df.columns[plots[i][1]]
        ax.scatter(df[df['target']==j][x], df[df['target']==j][y], color=colors[j])
        ax.set(xlabel=x, ylabel=y)

fig.legend(labels=labels, loc=3, bbox_to_anchor=(1.0,0.85))
plt.show()

print(f'Preparing train data and test data, defining criterion and optimizer')

X = df.drop('target',axis=1).values
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=33)

# CUDA case, adding .cuda() all over:
# this:
#X_train = torch.FloatTensor(X_train)
#X_test = torch.FloatTensor(X_test)
## y_train = F.one_hot(torch.LongTensor(y_train))  # not needed with Cross Entropy Loss
## y_test = F.one_hot(torch.LongTensor(y_test))
#y_train = torch.LongTensor(y_train)
#y_test = torch.LongTensor(y_test)
# becomes this:
X_train = torch.FloatTensor(X_train).cuda()
X_test = torch.FloatTensor(X_test).cuda()
y_train = torch.LongTensor(y_train).cuda()
y_test = torch.LongTensor(y_test).cuda()


trainloader = DataLoader(X_train, batch_size=60, shuffle=True)
testloader = DataLoader(X_test, batch_size=60, shuffle=False)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(gpumodel.parameters(), lr=0.01)

print(f'Training')
epochs = 100
losses = []

for i in range(epochs):
    i+=1
    y_pred = gpumodel.forward(X_train)
    loss = criterion(y_pred, y_train)
    losses.append(loss)

    # a neat trick to save screen space:
    if i%10 == 1:
        print(f'epoch: {i:2}  loss: {loss.item():10.8f}')

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


plt.plot(range(epochs), losses)
plt.ylabel('Loss')
plt.xlabel('epoch')
plt.show()

with torch.no_grad():
    y_val = gpumodel.forward(X_test)
    loss = criterion(y_val, y_test)
print(f'{loss:.8f}')

print(f'Run on X_test data one by one:')
correct = 0
with torch.no_grad():
    for i,data in enumerate(X_test):
        y_val = gpumodel.forward(data)
        print(f'{i+1:2}. {str(y_val):38}  {y_test[i]}')
        if y_val.argmax().item() == y_test[i]:
            correct += 1
print(f'\n{correct} out of {len(y_test)} = {100*correct/len(y_test):.2f}% correct')

# torch.save(model.state_dict(), 'IrisDatasetModel.pt')
## if we did not have the Model defined, we could user pickle, and run the serializer for the whole thing:
## torch.save(model, 'IrisDatasetModel.pt')
#
# new_model = Model()
# new_model.load_state_dict(torch.load('IrisDatasetModel.pt'))
# new_model.eval()
#
#with torch.no_grad():
#    y_val = new_model.forward(X_test)
#    loss = criterion(y_val, y_test)
# print(f'{loss:.8f}')

print(f'Individual test:')
mystery_iris = torch.tensor([5.6,3.7,2.2,0.5])

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,7))
fig.tight_layout()

plots = [(0,1),(2,3),(0,2),(1,3)]
colors = ['b', 'r', 'g']
labels = ['Iris setosa','Iris virginica','Iris versicolor','Mystery iris']

for i, ax in enumerate(axes.flat):
    for j in range(3):
        x = df.columns[plots[i][0]]
        y = df.columns[plots[i][1]]
        ax.scatter(df[df['target']==j][x], df[df['target']==j][y], color=colors[j])
        ax.set(xlabel=x, ylabel=y)

    # Add a plot for our mystery iris:
    ax.scatter(mystery_iris[plots[i][0]],mystery_iris[plots[i][1]], color='y')

fig.legend(labels=labels, loc=3, bbox_to_anchor=(1.0,0.85))
plt.show()

with torch.no_grad():
    print(gpumodel(mystery_iris))
    print()
    print(labels[gpumodel(mystery_iris).argmax()])
