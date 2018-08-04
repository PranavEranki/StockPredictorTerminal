# Stock Predictor

This is a simple linear regression stock predictor with built in command line functionality.
To view how it works, go to the [explanation](https://github.com/PranavEranki/StockPredictorTerminal/blob/master/Explanation.MD).

## How to use it
__Install__ (View the installation notes further down), then __navigate to the directory__ and __run__ the TerminalCodeVersion.py Script by typing 'TerminalCodeVersion.py' into your terminal

Plots the expected closing value of the stock for the next *n* days.

Finally, it will plot the growth of the stock from about a year ago up till the next *n* days.

## Installation

1. __Download__ the repository.

2. __Unzip__ it and move it to a new directory or folder of your choice.

3. If you do not have them already, __install python and pip__.

4. Do 'Pip install -r requirements.txt' to __install the dependencies__.

5. Go to Quandl.com and __sign up for a quandl account__.

6. Either save the quandl API key to an environmental variable or __have the key ready to be entered__.

## Running the script

7. Run the script. You will need to enter:
  *   API key or environmental variable name for the key
  *   Stock abbreviation for the desired stock
  *   How many days into the future you want to predict
when prompted.


If you get any errors, please bring up an issue and I will look into it ASAP.

Thank you.



## Screenshots

Screenshot for the gathering of the data:

![data](https://github.com/PranavEranki/StockPredictorTerminal/blob/master/images/prePredictions.PNG)

Screenshot for the first two plots with test data gathered above ^.

![firstTwo](https://github.com/PranavEranki/StockPredictorTerminal/blob/master/images/firstTwoPlots.PNG)

Screenshot for the last overall plot with test data gathered above ^^.

![final](https://github.com/PranavEranki/StockPredictorTerminal/blob/master/images/finalPlot.PNG)
