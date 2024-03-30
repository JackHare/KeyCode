PROMPT = ("Enter An IPv6 Address:\n")

HEX = ["A", "B", "C", "D", "E", "F"]

VALID_ADDRESS = ("CORRECT")

ERROR_MESSAGE = ("WRONG")

#If an error occurs
def error():
    print( ERROR_MESSAGE )
    quit()

#Get user input
def getUserInput():
    try: 
        address = input(PROMPT)
        return address
    except Exception:
        error()

#Returns if address is valid IPv6    
def validateAddress(address):
    
    #Split blocks into a list
    addressBrokenUp = address.split(":")
    
    #Test to make sure there is 8 blocks
    if len(addressBrokenUp) != 8:
        return False
    
    #Remove blocks with no data
    while addressBrokenUp.count("") > 0:
        addressBrokenUp.remove('')
    
    #Loop over each remaining block
    isValid = True
    for block in addressBrokenUp:
        
        #Loop over each letter
        for letter in block:
            
            #Test if letter is valid hex code
            if letter in HEX == True and not letter.isnumeric():
                isValid = False

    return isValid

if __name__ == "__main__":
    address = getUserInput()
    if validateAddress(address):
        print(VALID_ADDRESS)
    else: error()