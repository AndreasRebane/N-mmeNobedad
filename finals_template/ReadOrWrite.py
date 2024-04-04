

def readFromFile(line):

    with open('saveFile.txt', 'r') as file: 
        data = file.readlines()

    text = data[line] 

    file.close()
    return str(data)
    


def WriteToFile(text, line):

    with open('saveFile.txt', 'r') as file: 
        data = file.readlines() 
    
    data[line] = (str(text) +"\n")
    
    with open('saveFile.txt', 'w') as file: 
        file.writelines(data) 

    file.close()
