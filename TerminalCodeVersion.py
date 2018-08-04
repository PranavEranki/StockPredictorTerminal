import quandl
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation
import matplotlib.pyplot as plt
import os

e_prompt = 'Is You API Key saved in an environmental variable? Please enter Yes Or No: '
key_e_prompt = "What is the environmental variable name for your key? "
key_prompt = "Please enter your API key for Quandl: "


def getKey():
    saved = input(e_prompt)
    while (saved.lower()!='yes' and saved.lower()!='no'):
        print("Invalid response")
        saved = input(e_prompt)

    if saved.lower == 'yes':
        environ_name = input(key_e_prompt)
        quandl.ApiConfig.api_key = os.environ.get(str(environ_name))
    else:
        quandl.ApiConfig.api_key = input(key_prompt)

def StockCodeWorks(name):
    try:
        data = quandl.get("WIKI/" + name)
    except:
        return False;
    return True;

def getNameAndForecast():
    while(True):
        name = input("What is the abbreviation for the Stock you wish to view? ")
        if (StockCodeWorks(name)):
            break
        else:
            print("The stock code you entered does not exist in the Quandl Api. Please Try Again.")
            
    data = quandl.get("WIKI/" + name)
    
    forecast = input("How many days into the future would you like to predict? ")
    forecast = int(forecast)
    
    return name,forecast


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


def makeSpace():
    print()
    print()
    print()


def oldPlot(y,name):
    makeSpace()
    plt.figure()
    plt.title("Old Data for " + name)
    plt.plot(y, color = 'red')
    plt.ylabel('Price')
    plt.xlabel('Days since founded')
    plt.show()
    plt.show(block=True)
    makeSpace()


def newPlot(y,name):
    plt.figure()
    plt.title("Predicted values for " + name)
    plt.plot(y, color = 'blue')
    plt.ylabel('Price')
    plt.xlabel('Days into the future')
    plt.show()
    plt.show(block=True)
    makeSpace()


def allPlot(y,yhat,backset,name):
    plt.figure()
    y = y[(y.shape[0]-backset):,:]
    plt.title("Expected rise of " + name + ". Graph starts " + str(backset) + " days into the past, and ends with the predicted values for " + name + ".")
    plt.plot(y, color = 'red',label='Old Closing Prices')
    plt.plot(yhat,color='blue', label = 'Predicted Closing Prices')
    plt.ylabel('Price')
    plt.xlabel('Days since founded')
    plt.show()
    plt.show(block=True)
    makeSpace()

def predict(name,forecast):
    data = getData(name)
    X_forecast,X_train,y_train = preprocess(data,forecast)

    regressor = LinearRegression()
    regressor.fit(X_train,y_train)

    forecast_prediction = regressor.predict(X_forecast)
    forecast_prediction = forecast_prediction.reshape((forecast,1))
    #Visualizing trends in data. My Prediction is at the end

    oldPlot(y_train,name)
    newPlot(forecast_prediction,name)
    allPlot(y_train,forecast_prediction,500,name)


def printWorking():
    makeSpace()
    print("Working...")
    makeSpace()

def main():
    getKey()
    name,forecast = getNameAndForecast()
    printWorking()
    predict(name,forecast)

if __name__ == "__main__":
    main()
