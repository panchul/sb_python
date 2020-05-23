#!/usr/bin/env python
#
# A script to run the classic PyTorch classifier on popular iris dataset.
#
# $ python3 basic_classifier.py
# Getting data into the dataframe
# Preparing train data and test data, defining criterion and optimizer
# Training
# epoch:  1  loss: 1.12554717
# epoch: 11  loss: 0.96018577
# epoch: 21  loss: 0.77037913
# epoch: 31  loss: 0.59916538
# epoch: 41  loss: 0.48244980
# epoch: 51  loss: 0.39875236
# epoch: 61  loss: 0.32560092
# epoch: 71  loss: 0.26164362
# epoch: 81  loss: 0.21018130
# epoch: 91  loss: 0.17085433
# 0.16611052
# run on X_test data one by one:
#  1. tensor([-1.6397,  3.8199,  1.5429])     1
#  2. tensor([-1.4796,  3.7650,  1.3616])     1
#  3. tensor([ 3.7558,  1.0011, -4.1398])     0
#  4. tensor([-2.8836,  4.2461,  2.9518])     1
#  5. tensor([-6.0396,  5.3276,  6.5264])     2
#  6. tensor([-9.9196,  6.9639, 10.9114])     2
#  7. tensor([ 3.7558,  1.0011, -4.1398])     0
#  8. tensor([ 3.7558,  1.0011, -4.1398])     0
#  9. tensor([-6.4862,  5.4806,  7.0323])     2
# 10. tensor([-8.3384,  6.1160,  9.1293])     2
# 11. tensor([-8.8636,  6.3916,  9.7217])     2
# 12. tensor([ 3.7558,  1.0011, -4.1398])     0
# 13. tensor([-8.6955,  6.3005,  9.5323])     2
# 14. tensor([-3.1098,  4.3237,  3.2081])     1
# 15. tensor([-6.6442,  5.5348,  7.2113])     2
# 16. tensor([-1.2739,  3.6945,  1.1286])     1
# 17. tensor([-4.8715,  4.9273,  5.2034])     2
# 18. tensor([ 3.7558,  1.0011, -4.1398])     0
# 19. tensor([-3.3060,  4.3909,  3.4302])     1
# 20. tensor([-7.1282,  5.7006,  7.7594])     2
# 21. tensor([ 3.7558,  1.0011, -4.1398])     0
# 22. tensor([ 3.7558,  1.0011, -4.1398])     0
# 23. tensor([-8.7098,  6.3083,  9.5485])     2
# 24. tensor([ 3.7558,  1.0011, -4.1398])     0
# 25. tensor([-5.0584,  4.9914,  5.4151])     2
# 26. tensor([-4.8533,  4.9211,  5.1828])     2
# 27. tensor([-2.7273,  4.1926,  2.7747])     1
# 28. tensor([-0.7525,  3.5159,  0.5381])     1
# 29. tensor([-6.3139,  5.4216,  6.8371])     2
# 30. tensor([-5.8572,  5.2651,  6.3198])     2
# 
# 30 out of 30 = 100.00% correct
# Individual test:
# tensor([ 3.7558,  1.0011, -4.1398])
# 
# Iris setosa

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt
# for Jupyter notebooks might want this
#get_ipython().run_line_magic('matplotlib', 'inline')

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
model = Model()

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

X_train = torch.FloatTensor(X_train)
X_test = torch.FloatTensor(X_test)
# y_train = F.one_hot(torch.LongTensor(y_train))  # not needed with Cross Entropy Loss
# y_test = F.one_hot(torch.LongTensor(y_test))
y_train = torch.LongTensor(y_train)
y_test = torch.LongTensor(y_test)

trainloader = DataLoader(X_train, batch_size=60, shuffle=True)
testloader = DataLoader(X_test, batch_size=60, shuffle=False)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

print(f'Training')
epochs = 100
losses = []

for i in range(epochs):
    i+=1
    y_pred = model.forward(X_train)
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
    y_val = model.forward(X_test)
    loss = criterion(y_val, y_test)
print(f'{loss:.8f}')

print(f'Run on X_test data one by one:')
correct = 0
with torch.no_grad():
    for i,data in enumerate(X_test):
        y_val = model.forward(data)
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
    print(model(mystery_iris))
    print()
    print(labels[model(mystery_iris).argmax()])
