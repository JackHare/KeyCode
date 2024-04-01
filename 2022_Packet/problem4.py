"""

    take input in Base-16P

"""

ERROR_MESSAGE = ("ERROR")

base16_values = {'F': 0, 'E': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13, '1': 14, '0': 15}

ascii_dict = dict()
ascii_in_number = range(0,256)
for i in ascii_in_number:
    ascii_dict[str(i)] = chr(i)

def error():
    print(ERROR_MESSAGE)
    quit()

def get_user_input():
    try:
        user_input = input()
        return user_input
    except:
        error()
        
def convert_base16_to_base10(input):
    result = []
    for num in input:
        result.append(base16_values[num])
    return result

def convert_base10_to_ascii(input):
    print(input)

if __name__ == "__main__":
    user_input = get_user_input()
    base10 = convert_base16_to_base10(user_input)
    print("result:", convert_base10_to_ascii(base10))