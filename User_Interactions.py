import re
import pandas as pd
import os
import easygui as eg

def custom_error(reason = ""):    
    eg.msgbox(reason+" Process cancelling...","Exiting...")
    exit()

def prompt_touch_tag():

    touch_tag = eg.enterbox("Enter touch tag name","touch tag name")

    # check if tag is only alpha numerics and underscore character
    if touch_tag == None:
        custom_error("No touchtag entered")
    elif not bool(re.match('[A-Za-z0-9_]+$', touch_tag)):
        custom_error("Invalid touch tag name, please use alphanumerics and _")

    return touch_tag

def message_user(input_msg,input_title):
    
    output = eg.msgbox(input_msg,input_title)
    if output != "OK":
        custom_error("Program Exiting")


# Getting the L5K filepath to process
def prompt_file(filetype):

    message_user("Please enter a "+filetype+"file",filetype+" File selector")
    
    input_filepath = eg.fileopenbox(title = "Select a file",
                                    default="*."+filetype)
    
    if input_filepath == None:
        custom_error("No "+filetype+" file selected")
    else:
        return input_filepath

