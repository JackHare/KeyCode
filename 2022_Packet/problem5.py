"""
    get file "input_file.marky"
    create a file named input_file.marky
    parse commands
    {UPPER_X}: uppercase next charcters
    {LOWER_X}: lowers next charcters
    {REDACT_X} replaces charcters with #, affects all chars
    {SPACE_X} inserts X spaces
    {THEN} combines two commands
"""
def error():
    print("File Doesn't Exist")
    quit()

def get_input_file(input_file_name):
    try:
        with open(input_file_name, "r") as input_file:
            return input_file.read()
    except FileNotFoundError:
        error()
        
def parse_commands(input_text):    
    in_brackets = False
    
    commands = []
    
    command_name = ""
    count = ""
    in_count = False
    position = -1
    
    #Loop over each letter
    for letter in input_text:
        position += 1
        if letter == "{":
            in_brackets = True
            continue
        
        if letter == "_" and in_brackets:
            in_count = True
            continue
        
        #append and than reset command info, after bracket is closed
        if in_brackets and letter == "}":
            
            commands.append([ command_name, count, position+1 ])
            
            in_brackets = False
            command_name = ""
            count = ""
            in_count = False
            continue
        
        #Append to count
        if in_brackets and in_count:
            count += letter
        
        #If not in count and in brackets, add to command name
        if in_brackets and not in_count:
            command_name += letter
            continue
        
    #Parse out then and correct it
    command_num = 0
    for command in commands:
        command_num += 1
        if command_num > 1 and command_num < len(commands):
            if command[0] == "THEN":
                commands[command_num-2][2] = commands[command_num][2]
                commands.pop(command_num-1)
        
    return commands

def run_commands(input_text, commands):
    
    input_list = list(input_text)
    input_list_const = tuple(input_text)
    
    
    for command in commands:
        
        if command[0] == "UPPER":
            for letter in range(int(command[1])):
                input_list[command[2] + letter] = input_list[command[2] + letter].upper()   
                
        if command[0] == "LOWER":
            for letter in range(int(command[1])):
                input_list[command[2] + letter] = input_list[command[2] + letter].lower()   
        if command[0] == "REDACT":
            for letter in range(int(command[1])):
                input_list[command[2] + letter] = "#"
                
        if command[0] == "REVERSE":
            for letter in range(int(command[1])):
                input_list[command[2] + letter] = input_list_const[command[2]+int(command[1]) - letter]
                
    #run the space command last
    for command in commands:
        
        if command[0] == "SPACE":
            for letter in range(int(command[1])):
                input_list.insert(command[2]+letter, " ")


    #Remove the commands from the string
    removing = False
    output = ""
    for letter in input_list:
        if letter == "{":
            removing = True
            continue 
        
        if letter == "}":
            removing = False
            continue
            
        if not removing:
            output += letter
    return output
    
if __name__ == "__main__":
    input_text = get_input_file("input_file.marky")
    commands = parse_commands(input_text)
    print(run_commands(input_text, commands))