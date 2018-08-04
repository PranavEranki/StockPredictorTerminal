import quandl
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

