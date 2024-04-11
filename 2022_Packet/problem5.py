FILE_NOT_FOUND_MESSSAGE = ("File not found")

COMMAND_NAMES = ("UPPER", "LOWER", "REDACT", "REVERSE", "SPACE")

class Command:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.age = 0

"""
Returns the text of a file from a give filepath
"""
def get_file(filepath):
    #Attempt to open the file, but if file couldn't be found FileNotFoundError is thrown 
    try:
        #Open thef file and return its contents
        with open(filepath, "r") as input_file:
            return input_file.read()
    except FileNotFoundError:
        #Terminate the program
        print(FILE_NOT_FOUND_MESSSAGE)
        quit()
"""
Parses over the input marky file as a string, and returns the correct output
"""
def parse_input_text(input_text):
    
    #The name and length of all commands waiting to be preformed
    #They will start executing on the next valid charcter
    
    queued_commands = []
    
    seen_a_bracket = False
    seen_an_underscore_in_a_bracket = False
    
    possible_command_name = ""
    possible_command_length = ""
    
    pos = -1
    output_pos = -1
    
    input_text = list(input_text)
    output_text = [""]
    
    for letter in input_text:
        pos += 1
        #If we should begin collecting command information
        if letter == "{":
            seen_a_bracket = True
            continue
        
        #If command information has not ended, continue appending the info
        if not letter == "}":
            
            #Test to see if we switched from command name to command length 
            if seen_a_bracket and letter == "_":
                seen_an_underscore_in_a_bracket = True
                continue
        
            #If we are still in command name
            if seen_a_bracket and not seen_an_underscore_in_a_bracket:
                possible_command_name += letter
                continue
        
            #If we are in command length
            if seen_a_bracket and seen_an_underscore_in_a_bracket:
                possible_command_length += letter
        
        #If the command has ended
        else:
            
            #If the command has a valid name appened it to the command queue
            if possible_command_name in COMMAND_NAMES:
                queued_commands.append(Command(possible_command_name, int(possible_command_length)))          
                
            #Then reset command info and continue
            seen_an_underscore_in_a_bracket = False
            seen_a_bracket = False
            possible_command_name = ""
            possible_command_length = ""
            continue
            
        #If we are not in command info, run all queued commands
        if not seen_a_bracket:
            command_pos = -1
            output_pos += 1
            
            output_text.insert(output_pos, letter)
            for command in queued_commands:
                command_pos += 1       
                command.age += 1
                
                #Make sure this command has not expired
                if command.age > command.length and command.name != "REVERSE":
                    queued_commands.pop(command_pos)
                    continue
                elif command.age-1 > command.length:
                    queued_commands.pop(command_pos)
                    continue
                if command.name == "UPPER":
                    output_text[output_pos] = letter.upper()
                
                if command.name == "LOWER":
                    output_text[output_pos] = letter.lower()
                    
                if command.name == "REDACT":
                    output_text[output_pos] = "#"    
                    
                if command.name == "SPACE":
                    spaces = ""
                    for space in range(command.length): spaces += " "
                    output_text[output_pos] = spaces + letter
                    #output_pos += command.length
                    command.age = command.length    
                    
                if command.name == "REVERSE":

                    print(pos + (command.length - command.age*2))
                    print(command.age, ": ", input_text[pos + (command.length+1 - command.age*2) ] )
                    output_text[output_pos] = input_text[pos + (command.length+1 - command.age*2)]
                    
    print("".join(output_text))
    
if __name__ == "__main__":
    #Get the input text
    input_text = get_file("input_file.marky")
    output_text = parse_input_text(input_text)