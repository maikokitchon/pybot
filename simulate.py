import os
from loader import Loader

def catch_event(raw_message):
    print(f"Bot replied: OK. Please wait...")
    loaderObj = Loader(raw_message)
    response = loaderObj.get_response()
    if len(response) != 0:
        print(f"{response}")
    else:
        print(f"I could not get any response from the back end. Please contact bot admin.")

message = input('Please enter your command: ')
catch_event(message)