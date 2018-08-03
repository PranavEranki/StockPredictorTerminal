# -*- coding: utf-8 -*-
import quandl
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation
import matplotlib.pyplot as plt

def getData(name):
    data = quandl.get("WIKI/" + name)
    return data


def preprocess(data, forecast):

    data = data[['Adj. Close']]
    data['Prediction'] = data[['Adj. Close']].shift(-forecast)

    X = np.array(data.drop(['Prediction'], 1))
    X = preprocessing.scale(X)

    X_forecast = X[-forecast:] # set X_forecast equal to last forecast days
    X = X[:-forecast]

    y = np.array(data['Prediction'])
    y = y[:-forecast]

    X_train = X
    y_train = y.reshape((y.shape[0],1))

    return X_forecast,X_train,y_train


def predict(name,forecast):
    data = getData(name)
    X_forecast,X_train,y_train = preprocess(data,forecast)

    regressor = LinearRegression()
    regressor.fit(X_train,y_train)

    forecast_prediction = regressor.predict(X_forecast)
    forecast_prediction = forecast_prediction.reshape((forecast,1))
    #Visualizing trends in data. My Prediction is at the end
    
    return forecast_prediction
