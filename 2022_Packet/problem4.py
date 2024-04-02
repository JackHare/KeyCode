
ERROR_MESSAGE = ("ERROR")

#BASE-16P to Base 16
base16_values = {'F': 0, 'E': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': "A", '4': "B", '3': "C", '2': "D", '1': "E", '0': "F"}

#Called when an error occurs
def error():
    print(ERROR_MESSAGE)
    quit()

#Collects and returns user input
def get_user_input():
    try:
        user_input = input()
        return user_input
    except:
        error()
        
def convert_base16_to_base10(input):
    result = []
    for num in input:
        result.append(str(base16_values[num]))
    return result

def convert_base10_to_ascii(input):
    format = [ x+y for x,y in zip(input[0::2], input[1::2]) ]
    string =  "".join(format)
    
    byte_string = bytes.fromhex(string)  
    ascii_string = byte_string.decode("ASCII")  
    print(ascii_string)  
    
if __name__ == "__main__":
    user_input = get_user_input()
    base10 = convert_base16_to_base10(user_input)
    print("result:", convert_base10_to_ascii(base10))