ERROR_MESSAGE= ("File Doesn't Exist")

#Handles if the file is not found
def error():
    print(ERROR_MESSAGE)
    quit()

#Gets the file from the input, if not found it calls error()
def get_input_file(input_file_name):
    try:
        with open(input_file_name, "r") as input_file:
            return input_file.read()
    except FileNotFoundError:
        error()
        
def write_to_output_file(text, file_name):
    with open(file_name, "w") as file:
        file.write(text)
        
#Gets a list of every commands and returns it in the following format:
#[ [COMMAND_NAME, COMMAND_LENGTH, STARTING_POSITION ]]
def parse_commands(input_text):    

    #stores if the parser is currently inside a command description
    in_brackets = False
    
    #A list of every command
    #[ [COMMAND_NAME, COMMAND_LENGTH, STARTING_POSITION ]]
    commands = []
    
    #Stores the live command info as it is parsed 
    command_name = ""
    count = ""
    in_count = False
    
    #Stores the position where the parser is at
    position = -1
    
    #Loop over each letter
    for letter in input_text:

        #Add the to the position counter every tick
        position += 1

        #If a command is reached
        if letter == "{":
            in_brackets = True
            continue
        
        #If the counter portion of a command is reached
        if letter == "_" and in_brackets:
            in_count = True
            continue
        
        #When the command is closed
        #append and than reset command info, after bracket is closed
        if in_brackets and letter == "}":
            
            commands.append([ command_name, count, position+1 ])
            
            in_brackets = False
            command_name = ""
            count = ""
            in_count = False
            continue
        
        #If all those tests passed, and we have reached this point of the for loop
        #Append all relevant information
        
        #If we are in the number section of the command
        #Append to count
        if in_brackets and in_count:
            count += letter
        
        #If we are in the command name section
        #If not in count and in brackets, add to command name
        if in_brackets and not in_count:
            command_name += letter
            continue
        
    #Parses for the THEN and removes it
    #Than sets the previous commands starting position, to the starting position of the next command
    command_num = 0
    for command in commands:
        
        #Append to command number counter
        command_num += 1
        
        #If we are not at the very edges of the command list
        if command_num > 1 and command_num < len(commands):
            
            #If the command is THEN
            if command[0] == "THEN":
                
                #Set the previous commands, starting position equal to the command after THEN's starting position
                commands[command_num-2][2] = commands[command_num][2]
                
                #Remove this THEN command
                commands.pop(command_num-1)

    #Return the remaining commands        
    return commands

#Runs the commands from the input and command list
def run_commands(input_text, commands):
    
    #Converts the input into a list and a tuple duplicate
    input_list = list(input_text)
    
    #Parse over each command
    for command in commands:
        
        #If the command is UPPER
        if command[0] == "UPPER":
            
            #Run a for loop equal to the length of the command
            for letter in range(int(command[1])):
                
                #For each letter, set the text [ STARTING POSITION OF THE COMMAND + the current progress ] = to that.upper
                input_list[command[2] + letter] = input_list[command[2] + letter].upper()   
        
        #If the command is LOWER     
        if command[0] == "LOWER":
            
            #Run a for loop equal to the length of the command 
            for letter in range(int(command[1])):
                #For each letter, set the text [ STARTING POSITION OF THE COMMAND + the current progress ] = to that.upper
                input_list[command[2] + letter] = input_list[command[2] + letter].lower()   
        
        #If the command is REDACT
        if command[0] == "REDACT":
            
            #Run a for loop equal to the lenght of the command
            for letter in range(int(command[1])):
                
                #Replace the letter that is being parsed, with #
                input_list[command[2] + letter] = "#"
    
    #run the reverse command seperetely
    
    #Create a backup of the list so we don't lose any data as we reverse
    input_list_const = list(input_text)
    for command in commands:        
        #If the command is REVERSE
        if command[0] == "REVERSE":
            
            #Parse over every letter in the input text that is going to be modified by the command
            for letter in range(int(command[1])):
                print("letter", input_list[command[2] + letter])
                #The letter being parsed              the letter from the copy of the input, at the end of the section
                #We use the copy because, we are modify the data and when you reach the end of the string being reversed, the data at the start will already be lost
                input_list[command[2] + letter] = input_list_const[command[2]+int(command[1]) -1 - letter]
                        
    #run the space command last
    for command in commands:
        
        if command[0] == "SPACE":
            for letter in range(int(command[1])):
                input_list.insert(command[2]+letter, " ")


    #Remove the commands from the string
    removing = False
    output = ""
    
    #Parse over each letter of the input, if and remove all {} and anything inside of them
    for letter in input_list:
        if letter == "{":
            removing = True
            continue 
        
        if letter == "}":
            removing = False
            continue
            
        if not removing:
            output += letter
        
    #return the output as a string
    return output
    
if __name__ == "__main__":
    input_text = get_input_file("input_file.marky")
    commands = parse_commands(input_text)
    output = run_commands(input_text, commands)
    print(commands)
    write_to_output_file(output, "output_file.txt")