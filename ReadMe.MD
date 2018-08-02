# Stock Predictor

This is a simple linear regression stock predictor with built in command line functionality.

## How to use it
Install (View the installation notes further down), then navigate to the directory and run the TerminalCodeVersion.py Script.

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

3. If you do not have them already, install python and pip.

4. Do 'Pip install -r requirements.txt' to install the dependencies

5. Go to Quandl.com and sign up for an account.

6. Either save the quandl api key to an environmental variable or have the key ready to be entered

## Running the script

7. Run the script. You will need to enter:
  * key or environmental variable name for the key
  * Stock abbreviation for the desired stock
  * How many days into the future you want to predict

when prompted.


If you get any errors, please bring up an issue and I will look into it ASAP.

Thank you.
