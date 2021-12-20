import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### LINEAR REGRESSION ###


# x=np.arange(10)
# y=(x-5)**2
#
# plt.style.use("seaborn")
# plt.plot(x , y)
# plt.ylabel("Y")
# plt.xlabel("X")
# #plt.show()
#
# x2=0
# lr=0.1
# error=[]
# for i in range(50):
#     grad = 2*(x2-5)
#     x2=x2-lr*grad
#     e=(x2-5)**2
#     error.append(e)
#     plt.scatter(x2, e)
# #plt.plot(error)
# plt.show()

### GRADIENT DESCENT FOR LOCAL MINIMA FINDING   ###


x=pd.read_csv("Linear_X_Train.csv")
y=pd.read_csv("Linear_Y_Train.csv")

u=x.mean()
std = x.std()
# print("Mean is "+str(u))
# print("std is "+str(std))

plt.style.use("seaborn")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
plt.show()
