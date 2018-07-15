import re

def openAndFile(self, fileName):

    fileContent = []

    inputFile = open(fileName, "r")
    
    for line in inputFile:
        fileContent.append(line)

    inputFile.close()

    return fileContent
    

