# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import warnings
import printHelper
warnings.filterwarnings("ignore")


def oldPlot(y,name):
    printHelper.makeSpace()
    plt.figure()
    plt.title("Old Data for " + name)
    plt.plot(y, color = 'red')
    plt.ylabel('Price')
    plt.xlabel('Days since founded')
    plt.show()
    plt.show(block=True)
    printHelper.makeSpace()


def newPlot(y,name):
    plt.figure()
    plt.title("Predicted values for " + name)
    plt.plot(y, color = 'blue')
    plt.ylabel('Price')
    plt.xlabel('Days into the future')
    plt.show()
    plt.show(block=True)
    printHelper.makeSpace()


def allPlot(y,yhat,backset,name):
    plt.figure()
    y = y[(y.shape[0]-backset):,:]
    ally = np.concatenate((y,yhat))
    plt.title("Expected rise of " + name + ". Graph starts " + str(backset) + " days into the past, and ends with the predicted values for " + name + ".")
    plt.plot(ally,color='purple')
    plt.ylabel('Price')
    plt.xlabel('Days')
    plt.show()
    plt.show(block=True)
    printHelper.makeSpace()

def gatherHowFar():
    print("An overall plot will now be generated.")
    howfar = int(input("How many days into the past would you like your overall graph to go? "))
    return howfar