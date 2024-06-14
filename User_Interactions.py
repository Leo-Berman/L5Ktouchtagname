import pandas as pd
import os
import easygui as eg

# Error bubble
def common_error(Reason = ""):    
    eg.msgbox(Reason+" Process cancelling...","Exiting...")
    exit()

def prompt_touchtag():
    output = eg.enterbox("Enter touch tag name","touchtagname")

    if output == None:
        common_error("No touchtag entered")
    else:
        for x in output:
            if x.isalnum() or x=="_":
                pass
            else:
                common_error("Invalid touch tag name, please use alphanumerics and _")
    return output
# Simple msg box wrapper to guide the user
def prompt(inmsg,intitle,okbtn="ok"):
    
    output = eg.msgbox(inmsg,intitle,okbtn)
    if output!=okbtn:
        common_error("Program Exited")


# Getting the L5K filepath to process
def prompt_input_filepath(filetype):

    prompt("Please enter a "+filetype+"file",filetype+" File selector")
    
    # Prompt the user
    input_path = eg.fileopenbox(title = "Select a file", default="*."+filetype)

    # If no path then abort
    if input_path == None:
        common_error("No "+filetype+" file selected")

    if not input_path.endswith("."+filetype):
        common_error("File selected is not an " + filetype + " file")
    
    # Otherwise return the path
    else:
        
        return input_path

