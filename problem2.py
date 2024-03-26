#CONSTRAINTS

"""

1. Prompt user to enter a date
    2. Accept this input on the next line 
    3. Should be <DDMMMYYY>
            DD == 00 - 31
            MMM == ALL CAPS:  JAN, FEB
            YY - 00- 99
            
    4. If incorrect state, "Wrong Data Format"
    5. Print: 
            Day: <Day>
            Month: <Correctly Spelled Full Month Name>  
            Year: <Four Digit Year>
            
"""

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

#Parses user input into a list
def parseUserInput(input):
    date = []
    date.append[int(input[0] + input[1])]
    date.append[input[2] + input[3] + input[4]]
    date.append[input[5] + input[6]]
    return date

def validateInput(date):
    if not str(date[1]).isnumeric() or date[1] > 31: return False

    monthDateIsRight = False
    
    for month in monthNames:
        if date[2] == month: monthDateIsRight = True    
    
    if not monthDateIsRight: return False
    return True

#Get user input
try: 
    userInput = input("Enter Date:\n")
except Exception:
    print("Wrong Date Format")
    
#Make sure input is 7 charcers
if len(userInput) == 7:

    date = parseUserInput(userInput)
    
    if validateInput(date): None
    else: print("Wrong Date")
    
else:
    print("Wrong Date Format")
