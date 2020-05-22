# 
# A simple linear regression sample.
#
# This is y=w*x+b with one scalar input and one scalar output 
# model = nn.Linear(in_features=1, out_features=1)
# print("weight :", model.weight)
# print("bias: ", model.bias)
# 

import torch
import torch.nn as nn  # we'll use this a lot going forward!
import numpy as np
import matplotlib.pyplot as plt

# torch.manual_seed(123)

X = torch.linspace(1,50,50).reshape(-1,1)
e = torch.randint(-8,9,(50,1), dtype=torch.float)
y = 2*X + 1 + e

#plt.scatter(X.numpy(), y.numpy())
#plt.ylabel('y')
#plt.xlabel('x');
#plt.show()

class Model(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)

    def forward(self, x):
        # y_pred = self.linear(x)
        # return y_pred
        return self.linear(x)

model = Model(1, 1)
print("The model: ", model)
#print("Initial weight: ", model.linear.weight.item())
#print("Initial bias:  ", model.linear.bias.item())

print("Initial parameters:")
for name, param in model.named_parameters():
    print(name, '\t', param.item())

# mean square error
criterion = nn.MSELoss()

# stochastic gradient descent
optimizer = torch.optim.SGD(model.parameters(), lr = 0.001)

epochs = 20
losses = []

for i in range(epochs):
    i+=1
    y_pred = model.forward(X)
    loss = criterion(y_pred, y)
    losses.append(loss)
    print(f'epoch: {i:2}  loss: {loss.item():10.8f} \
weight: {model.linear.weight.item():10.8f} bias: {model.linear.bias.item():10.8f}')
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

plt.plot(range(epochs), losses)
plt.ylabel('Loss')
plt.xlabel('epoch');
plt.show()

w1,b1 = model.linear.weight.item(), model.linear.bias.item()
print(f"Final weight: {w1:.8f}, Final bias: {b1:.8f}")
print()

x1 = np.array([X.min(),X.max()])
y1 = x1*w1 + b1
print("x axis range(the initial values, really): ", x1)
print("y axis range(what we got via y1=x1*w1+b1 the final weight and bias): ", y1)

plt.scatter(X.numpy(), y.numpy())
plt.plot(x1,y1,'r')
plt.title("Current Model")
plt.ylabel('y')
plt.xlabel('x');
plt.show()
#plt.savefig('example_figure.png')
