import random, sys, argparse, math

# Memory that will be manipulated
tape = bytearray(1000)

# Current element on tape
current_tick = 0

# Used as loop and if conditions
target = 0

# Each word length corresponds to specific element in command list
#   note: command list can be changed by user
command_list = [
    'FILL',        # Length -> 0
    'INCR',        # Length -> 1
    'DECR',        # Length -> 2
    'CHAR',        # Length -> 3
    'SLIDE_RIGHT', # Length -> 4
    'SLIDE_LEFT',  # Length -> 5
    'RAND',        # Length -> 6
    'PRINT',       # Length -> 7
    'LOOP_START',  # Length -> 8
    'LOOP_END'     # Length -> 9
]

def execute_command(command):
    global current_tick

    if (command == '+'): # Length -> 1
        tape[current_tick] += 1
    elif (command == '-'): # Length -> 2
        tape[current_tick] -= 1
    elif (command == '.'):
        print(str(chr(tape[current_tick])))
    elif (command == '>'):
        current_tick += 1
    elif (command == '<'):
        current_tick -= 1
    

def main():

    #####################
    # Handle File Parsing
    #####################
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    # Split file into command list
    with open(args.filename) as f:
        script = f.read().replace('\n', ' ')
        script_data = list(script)
        for w in script_data:
            if (w == ' '):
                script_data.remove(w)
        print(script_data)

        # Iterate through commands and call primary command function
        current_command_index = 0

        # Push/Pop loops
        loops = []

        # TODO: Possibly do if/else on either word length or symbols
        while (current_command_index < len(script_data)):
            command = script_data[current_command_index]
            

            if (command == '[' or command == ']'):
                if (command == '['):
                    if (tape[current_tick] != 0):
                        loops.append(current_command_index)
                        current_command_index += 1
                    else:
                        nested = 1
                        while(script_data[current_command_index] != ']' or nested != 0):
                            current_command_index += 1
                            if (script_data[current_command_index] == '['):
                                nested += 1 
                            elif (script_data[current_command_index] == ']'):
                                nested -= 1
                        current_command_index += 1
                elif (command == ']'):
                    current_command_index = loops.pop()

            else:
                execute_command(script_data[current_command_index])
                current_command_index += 1

if __name__ == "__main__":
    main()




# Prints Hello World!
# ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.