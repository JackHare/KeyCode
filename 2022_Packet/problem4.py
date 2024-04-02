ERROR_MESSAGE = ("Invalid Input")
USER_PROMPT = ("Proprietary Scheme:\n")

#BASE-16P to Base 16
base16_values = {'F': 0, 'E': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': "A", '4': "B", '3': "C", '2': "D", '1': "E", '0': "F"}

#Called when an error occurs
def error():
    print(ERROR_MESSAGE)
    quit()

#Collects and returns user input
def get_user_input():
    try:
        user_input = input(USER_PROMPT)
        return user_input
    except:
        error()
        
#Takes a base16P string and returns another string of regular base16
def convert_base16P_to_base16(input):
    result = ""
    for num in input:
        result += str(base16_values.get(num))
    return result

#Takes a string of base16 numbers and returns ascii
def convert_base16_to_ascii(input):
    try:
        #Convert base16 to byte
        byte_string = bytes.fromhex(input)
    
        #Convert byte to ASCII and return it  
        ascii = byte_string.decode("ASCII")  
        return ascii
    except:
        return ERROR_MESSAGE
    
if __name__ == "__main__":
    
    user_input = get_user_input()
    
    #Convert user input to base16, and print the conversion from base16 to ascii
    base16 = convert_base16P_to_base16(user_input)
    print(convert_base16_to_ascii(base16))