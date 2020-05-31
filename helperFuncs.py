
from os import listdir


def getFiles(dir):
    filesList = listdir(dir)
    seperator = ","
    final_str = seperator.join(filesList)
    return final_str
