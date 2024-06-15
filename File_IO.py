import User_Interactions as UI
import pandas as pd
import easygui as eg
# Load the file into memory
def load_file(input_filepath):

    # Read the file in with proper encoding
    file = open(input_filepath,"r",encoding='UTF8')
    content = file.readlines()
    file.close()
    
    # If file was empty, abort Otherwise return the contents of the file
    if content == None:
         UI.common_error("File was Empty")
    else:
        return content

def load_file_list(input_filepath):

    # Read the file in with proper encoding
    file = open(input_filepath,"r",encoding='UTF8')
    content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i].strip()
    file.close()
    
    # If file was empty, abort Otherwise return the contents of the file
    if content == None:
         UI.common_error("File was Empty")
    else:
        return content

def write_lines(input_filepath,content):
     file = open(input_filepath,"w",encoding='UTF8')
     for i,x in enumerate(content):
         if type(x) != str:
             content[i] = ""
             print(i)
     file.writelines(content)
     
     file.close()
     eg.msgbox("File written to :",input_filepath)
