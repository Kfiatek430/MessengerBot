import configparser
import os
import time


config = configparser.ConfigParser()

option = input('Do you want to enter a new configuration or load the previous one? N(ew) / P(revious) ')

if option == "N":
    user = input('Enter email / phone number used on Facebook: ')
    password = input('Enter the password used on Facebook: ')
    message = input('Enter the text of the message you want to send: ')
    receiver = input('Enter the EXACT name of the chat which has to receive the message: ')
    time = str(input('Enter the time of sending the message (HOUR: MINUTE) (15:03): '))

    config.add_section('MainData')
    config.set('MainData', 'user', user)
    config.set('MainData', 'password', password)
    config.set('MainData', 'message', message)
    config.set('MainData', 'receiver', receiver)
    config.set('MainData', 'time', time)

    with open(r"D:\Programs\MessengerBot\config.ini", "w") as configfile:
        config.write(configfile)

elif option == "P":
    os.system('python D:\\Programs\MessengerBot\mainv2.py')

else:
    print("You've selected wrong option. Restart the program and select N or P")
    time.sleep(5)
    exit()