# testTwillio.py
from twilio.rest import Client
import emoji

# TWILLIO SENDER INFORMATION
ACCOUNT_SID = '<your-account-sid>'
AUTH_TOKEN = '<your-account-authToken>'
SENDER_PHONE_NUMBER = '<your-sender-phone-number>'

def main():
    phone_numbers = get_phone_numbers()

    twilioCli = Client(ACCOUNT_SID, AUTH_TOKEN)

    msg = get_message()

    for i in range(len(phone_numbers)):
        try:
            # Send message
            message = twilioCli.messages.create(
                body=msg,
                from_=SENDER_PHONE_NUMBER,
                to=phone_numbers[i])
        except:
            print('Error, returning')
            break
        
        # Log the msg send
        print('Sent message #' + str(i+1) + ' sid = ' + str(message.sid) + '; message sent to ' + str(message.to))

def normalize(el):
    return el.replace(' ','').replace('(','').replace(')','').replace('-','').replace('+1','')

def get_phone_numbers():
    phone_numbers = [
        '+1(123)-456-7890',
        '+1(123)-456-7890',
        '+1(123)-456-7890',
        '+1 (123) 456-7890',
        '+1(123)-456-7890',
        '123)456-7890',
    ]
    phone_numbers = list(set(list(map(normalize, phone_numbers))))
    return phone_numbers

def get_message():
    
    # Adding emoji's to text messages
    msgTop = \
            str(chr(int('1F334', 16)))*10 + '\n' + \
            str(chr(int('1F48E', 16))) + \
            '  MESSAGE TITLE  ' + \
            str(chr(int('1F48E', 16))) + '\n' + \
            str(emoji.emojize(":palm_tree:"))*10

    msg = msgTop + """

Insert
Your 
Multiline
Message

Or maybe a link: https://bit.ly/3shY6wt 

""" + str(chr(int('1F3A9', 16)))

    return msg

if __name__ == '__main__':
    print('BEGIN')
    main()
    print('END PROGRAM')
