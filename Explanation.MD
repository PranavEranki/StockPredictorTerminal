# Explanation of code

The code starts off with gathering your API Key. It gathers it from an environmental variable if you have it stored in one, or if you don't, it asks you to copy/paste it into the terminal so you have the key in the program.

Then, the code asks you for the stock abbreviation of the stock you wish to predict. Once it takes in the abbreviation, it uses a try/except loop to ensure that the abbreviation is for an actual stock registered in the quandl API - this prevents the user from encountering any errors.

Once the code gathers the abbreviation and validates it, it then asks for how many days into the future you want to predict. This is simply stored to a variable and returned along with the abbreviation.

Once this is done, it begins the prediction process. Once it has an array of values for the stock and days entered, it begins the plotting.

The plotting consists of three phases, and uses matplotlib.

First, the old closing values of the stock are displayed.

Once that is done, the predicted values for the next *n* are plotted on another graph.

Finally, both the graphs are joined together, with the old values in one color and the new values in a new color, and displayed. For this, the program then asks the user to give them an integer value of how many days into the past they would like the data for that stock to be concatenated to the beginning of the predicted data. *This is confusing, here is an example*

Let's say the user enters Amazon as their stock, 30 days into the future, and 50 for the value in the final plot. The program will then take the predicted values for 30 days into the future, and paste them to the end of the closing stock data for 50 days ago.

If the user entered 10 instead of 50, then 10 days of stock data into the past would be prefixed to the 30 days of predicted values for that stock.

I hope that clears up any confusion, and gives you some insight into how the program works.


__Thank you__


# Features to add
A piece of code which will validate if your API key is a real key or not. Could not find documentation for this, so I was unable to implement it.

# Current Bugs
Sometimes, you get the error 'no module named quandl' if you run it from your terminal. The only fix I was able to find that worked for me was to run it from a code editor. I used Spyder from conda, and it worked fine for me.

Other than that, there are none right now! Yay!
