import ProgramClass as PC
import File_IO as FI
import User_Interactions as UI
import re

def main():

    # Read in a list of tags the user is interested in
    input_tags = FI.load_tags(UI.prompt_file("txt"))

    # Get tag user wants to use for cross reference
    touch_tag = UI.prompt_touch_tag()

    # Load the L5K file
    L5K_path = UI.prompt_file("L5K")
    L5K_lines = FI.load_file(L5K_path)

    first_pass = True
    line_index = 0
    while line_index < len(L5K_lines):

        # Search for beginning of a program
        tmp_program = re.search(r"^\tPROGRAM \w+",L5K_lines[line_index])

        # Search for alias
        tmp_alias =  re.search(r"(^\t\t\t\w+ OF [^ ]+)",L5K_lines[line_index])

        # If beginning of a program found, initialize variables
        if tmp_program != None:

            # Keep track of line where program begins
            program_start = line_index
          
            # Ofs     : tag name literals
            # Aliases : index correlated list of corresponding aliases
            ofs = []
            aliases = []
              
            first_pass = True

        # If end of a program found
        elif L5K_lines[line_index].__contains__("END_PROGRAM"):

            if first_pass == True:

                # create new instance of program
                # this also calculates the program tags of interest
                program_class = PC.L5KProgram(input_tags, aliases, ofs)
                first_pass = False
                
            else:
                first_pass = True

        
        # If an alias is found during the first_pass
        elif tmp_alias != None and first_pass == True:

            # Split alias into tag literal and alias
            tmp_alias=tmp_alias.group().strip().split(" OF ")

            # Get the base tag of the tag literal
            if tmp_alias[1].__contains__("."):
                tmp_alias[1] = tmp_alias[1].split('.')[0]
            
            aliases.append(tmp_alias[0])
            ofs.append(tmp_alias[1])

            
        # If a logic rung is found during the second pass,
        elif (first_pass == False and
              L5K_lines[line_index].startswith("\t\t\t\tN: ")):

            # Add the touchtag to the rung
            L5K_lines[line_index] = program_class.update_line(
                L5K_lines[line_index], touch_tag)

        # Check for beginning of controller tags
        elif L5K_lines[line_index].startswith("\tTAG"):

            # Keep track of the first line of the controller tags
            beginning_of_controller_tags = line_index

            # Boolean to see if the touch tag already exists
            found_touch_tag = False

            # Iterate through until the end of the controller tags
            while not L5K_lines[line_index].startswith("\tEND_TAG"):

                # If the tag is there, note it
                if L5K_lines[line_index].startswith("\t\t" + touch_tag+" :"):
                    found_touch_tag = True

                line_index += 1

            # If the tag isn't there, insert it
            if found_touch_tag == False:
                L5K_lines.insert(beginning_of_controller_tags + 1,
                                 "\t\t" + touch_tag
                                 + " : BOOL (RADIX := Decimal) := 0;\n")
            
        line_index += 1

    
    FI.write_L5K(L5K_path,L5K_lines)
    
if __name__ == "__main__":
    main()
