"""
    Enter a potential IPv6 Address and validate
        -Contains only hexadecimal, 0s can be dropped
"""

PROMPT = ("Enter An IPv6 Address:\n")

HEX = ["A", "B", "C", "D", "E", "F"]

#If an error occurs
ERROR_MESSAGE = ("WRONG")
def error():
    print( ERROR_MESSAGE )
    quit()
    
def validateAddress(address):
    
    #Split blocks into a list, and remove any empty elements
    addressBrokenUp = address.split(":")
    while addressBrokenUp.count("") > 0:
        addressBrokenUp.remove('')
    
    #Loop over each block
    isValid = True
    for block in addressBrokenUp:
        for letter in block:
            print("LETTER", letter)
            print(letter.isnumeric())
            if HEX.count(letter) == 0 or (not letter.isnumeric()): isValid = False

    return isValid

#Get user input
def getUserInput():
    try: 
        address = input(PROMPT)
        return address
    except Exception:
        error()
        
address = getUserInput()
if validateAddress(address):
    print("yay")
else: error()
    