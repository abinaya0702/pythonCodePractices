#importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_boston
#understanding the dataset
boston = load_boston
print(boston_DESCR)
#access the data attributes
dataset = boston.data
for name, index in enumerate(boston.feature_names):
    print(index,name)
#reshaping data
data = dataset[:,12].reshape(-1,1)
#shape of the data
np.shape(dataset)
#target values
target = boston.target.reshape(-1,1)
#shape of target
np.shape(target)
#ensuring that matplotlib is working inside the notebook
%matplotlib inline
plt.scatter(data, target, color='green')
plt.xlabel('Per capita crime rate')
plt.ylabel('Cost of the house')
plt.show()

#regression
from sklearn.linear_model import LinearRegression
#creating a regression model
reg = LinearRegression()
#fit the model
reg.fit(data, target)
#prediction
pred = reg.predict(data)
#ensuring that matplotlib is working inside the notebook
%matplotlib inline
plt.scatter(data, target, color='red')
plt.plot(data, pred, color='green')
plt.xlabel('Per capita crime rate')
plt.ylabel('Cost of the house')
plt.show()

#circumventing curve issue using polynomial model
from sklearn.preprocessing import PolynomialFeatures
#to allow merging of models
from sklearn.pipeline import make_pipeline
model = make_pipeline(PolynomialFeatues(3), reg)
model.fit(data, regret)
pred = model.predict(data)
#ensuring that matplotlib is working inside the notebook
%matplotlib inline
plt.scatter(data, target, color='red')
plt.plot(data, pred, color='green')
plt.xlabel('Per capita crime rate')
plt.ylabel('Cost of the house')
plt.show()

#r_2 metric
from sklearn.metrics import r2_score
#predict
r2_score(pred,target)






