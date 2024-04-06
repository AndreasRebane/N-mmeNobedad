filename = 'map/saveFile.txt'


def readFromFile(line):

    with open(filename, 'r') as file: 
        data = file.readlines()

    if (data):
        text = data[line] 
        return str(text)
    else:
        raise ValueError("Cannot read lines - file is empty!") # raises an error when trying to read an empty file



def writeToFile(text, line):

    with open(filename, 'r') as file: 
        data = file.readlines() 
    
    if (not data):
        with open(filename, 'a') as file:
            file.write(text) 

    else: # if the file is empty then - instead of replacing a line - it appends to the beginning
        data[line] = str(text) +"\n"
        
        with open(filename, 'w') as file: 
            file.writelines(data) 

