monthNames = {
    "JAN": "January",
    "FEB": "Febuary",
    "MAR": "March",
    "APR": "April",
    "MAY": "May",
    "JUN": "June",
    "JUL": "July",
    "AUG": "Aug",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December"
}

ERROR_MESSAGE = ("Wrong Date Format")

#Parses user input into a list of: day, month,  andyear
def parseUserInput(input):
    date = []
    date.append((input[0] + input[1]))
    date.append(input[2] + input[3] + input[4])
    date.append(input[5] + input[6])
    return date

#Tests if input and data is correct
#Returns false if a test failed, and true if all tests passed
def validateInput(date):
    #Test if the day is all numbers and less than 31
    if (not str(date[0]).isnumeric()) or int(date[0]) > 31: return False
    
    #Test if year is all numbers and between 0 and 99
    if (not str(date[2].isnumeric())) or int(date[2]) > 99 or int(date[2]) < 0: return False
    
    #Test to see if the month is a valid abbreviation
    if date[1] in monthNames.keys(): return True
    else: return False

def error():
    print(ERROR_MESSAGE)
    quit()

#Get user input
def getUserInput():
    try: 
        userInput = input("Enter Date:\n")
        if len(userInput) != 7: error()
        return userInput
    except Exception: error()
    return userInput

if __name__ == "__main__":
    userInput = getUserInput()
    date = parseUserInput(userInput)

    #If the user data is valid, print it    
    if validateInput(date): 
        print("Day: " + date[0])
        print("Month: " + monthNames[date[1]])
        print("Year: 20" + date[2])
    else: error()