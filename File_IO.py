import User_Interactions as UI
import pandas as pd
import easygui as eg

def load_file(input_filepath):

    file = open(input_filepath,"r",encoding='UTF8')
    content = file.readlines()
    file.close()
    
    if content == None:
        UI.custom_error("File was Empty")
    else:
        return content

def load_tags(input_filepath):

    # remove new line characters
    content = [x.strip() for x in load_file(input_filepath)]    
    return content

def write_L5K(input_filepath,content):
    
    file = open(input_filepath,"w",encoding='UTF8')

    # replace NoneTypes with blank lines
    content = list(map(lambda x: "" if type(x) == None else x, content))

    file.writelines(content)
    file.close()
    
    eg.msgbox("File written to :"+input_filepath)
