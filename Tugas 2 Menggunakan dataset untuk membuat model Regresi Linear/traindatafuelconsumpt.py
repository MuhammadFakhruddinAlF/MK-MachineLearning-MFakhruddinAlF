import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("FuelConsumptionCo2.csv")
print(df.head())

cdf = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]
print(cdf.head())

#split data into train and test
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

#create and train regression model
regr = LinearRegression()
train_x = np.asanyarray(train[["ENGINESIZE"]])
train_y = np.asanyarray(train[["CO2EMISSIONS"]])

regr.fit(train_x, train_y)

#print
print("Coefficients: ", regr.coef_)
print("Intercept: ", regr.intercept_)

#training data
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color="blue")

#create prediction line
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], "-r")
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()