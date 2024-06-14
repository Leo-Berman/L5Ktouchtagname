from ProgramClass import *
from File_IO import *
from User_Interactions import *
import re

def main():
    pass

def test_main():

    # for testing purposes, this will eventually be read in via .txt
    controller_tags_of_interest = load_file_list(prompt_input_filepath("txt"))

    # touch tag
    touchtag = prompt_touchtag()
    print(touchtag)
    # also for testing, the file will eventually be dynamic
    lines = load_file(prompt_input_filepath("L5K"))

    # to keep track of first line of program
    begin_program = 0

    # keep track if this is first or 2nd program
    first_pass = True

    # hold the program class that contains the ability to calculate tags in the program
    program_class = None

    # list for holding aliases
    aliases = []

    # list for holding ofs (things are aliased of)
    ofs = []
    
    # iterate through the lines
    i = 0
    while i < len(lines):

        # search the line for the beginning of a program
        tmp_program = re.search(r"^\tPROGRAM \w+",lines[i])

        # look for an alias in the line
        tmp_alias =  re.search(r"(^\t\t\t\w+ OF [^ ]+)",lines[i])

        # if it is the beginning of a new program, note the beginning of the program
        # and create a new instance of the program class
        if tmp_program != None:
            begin_program = i
            program_class = program()

        # if it's the end of the program, check to see if it's the first or second time through
        # if it's the first time through, calculate the connections for the aliases
        # if it's the second time through, reset

        elif lines[i].__contains__("END_PROGRAM"):
            if first_pass == True:
                program_class.calculate_tags_in_program(aliases,ofs)
                program_class.calculate_tags_of_interest(controller_tags_of_interest)
                i = begin_program
                first_pass = False
            else:
                first_pass = True
        elif tmp_alias != None and first_pass == True:

            # split alias into actual IO point, and what the alias is of that IO point
            tmp_alias=tmp_alias.group().strip().split(" OF ")
            aliases.append(tmp_alias[0])
            ofs.append(tmp_alias[1])

        # Check for logic rung if it already has target tags
        elif first_pass == False and lines[i].startswith("\t\t\t\tN: "):
            # update the line
            lines[i] = program_class.update_line(lines[i],touchtag)
        i+=1
if __name__ == "__main__":
    test_main()
