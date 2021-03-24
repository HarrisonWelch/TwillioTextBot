# TwillioTextBot

## Description
* This project was made to send text messages very easily if given a simple list of phone numbers using [Twillio](https://www.twilio.com/messaging)

## Install & Run
* First you must have a Twillio premium account in order to send messages to phone numbers other than yours.
* Run `pip install -r requirements.txt` on the command line in the repo folder to install
  * `twillio` - a python helper library
  * `emoji` - a quick way of putting emojis in text. Adds flare to message sending
* Insert your list of phone numbers into the `get_phone_numbers()` function as a comma seperate string array
  * TODO: make this a seperate file that can be interpreted more easily
* Place your account info in a the top
  * `ACCOUNT_SID` - holds your account sid from the twillio dashboard
  * `AUTH_TOKEN` - holds your private auth key for from the twillio dashboard
  * `SENDER_PHONE_NUMBER` - holds the phone number you "rented" from twillio
* Run the program.
* Note: long lists of 200+ numbers may take several minutes to send all

## Links:
* Tutorial: https://www.twilio.com/docs/libraries/python
