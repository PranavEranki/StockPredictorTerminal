# Stock Predictor

This is a simple linear regression stock predictor with built in command line functionality.

## How to use it
Install (View the installation notes further down), then navigate to the directory and run the script.

Simply give it your:

* Quandl API Key, either through an environmental variable or manually typing it in.
* The stock abbreviation of your desired stock
* The number of days into the future you wish to predict

And then the predictor will predict *n* number of days into the future.

It will plot the growth of the stock up till the current day using up-to-date data gathered from Quandl.

Then, it will plot the expected closing value of the stock for the next *n* days.

Finally, it will plot the growth of the stock from about a year ago up till the next *n* days.

## Installation

1. Download the repository.

2. Unzip it and move it to a new directory or folder of your choice.
