import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import random
import matplotlib.pyplot as plt


class Predictor:
    def __init__(self):
        # Initialize default array, which will be overridden as user completes tasks
        self.xVals = np.array([i for i in range(144)]).reshape(-1, 1)
        self.yVals = (1/275) * (self.xVals - 72)**2 + 2
        self.yPredict = np.array(float)

    def train(self):
        # Train data on Linear Regression model
        poly = PolynomialFeatures(degree=10)
        X_poly = poly.fit_transform(self.xVals)
        model = linear_model.LinearRegression()
        model.fit(X_poly, self.yVals)
        y_pred = model.predict(X_poly)
        self.yPredict = y_pred

    def addPair(self, xVal, yVal):
        # Add pair of X, Y values to appropriate indices
        self.xVals = np.insert(self.xVals, xVal, xVal).reshape(-1, 1)
        self.yVals = np.insert(self.yVals, xVal, yVal).reshape(-1, 1)
        self.train()

    def plot(self):
        # Plot graph for visualization purposes
        plt.scatter(self.xVals, self.yVals, color='blue')
        plt.plot(self.xVals, self.yPredict, color='red')
        plt.show()

    def addNoise(self, var):
        # Add noise to each plot with a given variance
        for i in self.xVals:
            if random.randint(0, 1) == 1:
                self.yVals[i] += abs(random.randrange(-var, var))

    def getYPred(self):
        # Get prediction array
        return list(self.yPredict)


# pred = Predictor()
# pred.train()
# pred.addNoise(10)
# pred.plot()
