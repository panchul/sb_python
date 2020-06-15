#!/usr/bin/env python
# coding: utf-8
# ## Binary Classification
# https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.nn import functional as F

wine_features = wine_data.drop('Class', axis = 1)
wine_features.sample(5)

wine_target = wine_data[['Class']]
wine_target.sample(5)

from sklearn.model_selection import train_test_split
X_train, x_test, Y_train, y_test = train_test_split(wine_features,
                                                    wine_target,
                                                    test_size=0.4,
                                                    random_state=0)
Xtrain_ = torch.from_numpy(X_train.values).float()
Xtest_ = torch.from_numpy(x_test.values).float()

Ytrain_ = torch.from_numpy(Y_train.values).view(1,-1)[0]
Ytest_ = torch.from_numpy(y_test.values).view(1,-1)[0]

input_size = 13
output_size = 3
hidden_size = 100

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, X):
        X = torch.sigmoid((self.fc1(X)))
        X = torch.sigmoid(self.fc2(X))
        X = self.fc3(X)

        return F.log_softmax(X, dim=-1)

model = Net()

import torch.optim as optim

optimizer = optim.Adam(model.parameters(), lr = 0.01)
loss_fn = nn.NLLLoss()

epochs = 1000

for epoch in range(epochs):

    optimizer.zero_grad()
    Ypred = model(Xtrain_)

    loss = loss_fn(Ypred , Ytrain_)
    loss.backward()

    optimizer.step()
        
    if epoch % 100 == 0:
        print ('Epoch', epoch, 'loss', loss.item())


#list(model.parameters())

torch.save(model, 'classifier.pt')

# Loading Model
new_model = torch.load('classifier.pt')

predict_out = new_model(Xtest_)
_, predict_y = torch.max(predict_out, 1)

from sklearn.metrics import accuracy_score, precision_score, recall_score

print ('prediction accuracy', accuracy_score(Ytest_.data, predict_y.data))
print ('micro precision', precision_score(Ytest_.data, predict_y.data, average='micro'))
print ('micro recall', recall_score(Ytest_.data, predict_y.data, average='micro'))
