def removeNum(input:str):
    filteredString = ""
    for char in input:
        if '0' < char < '9':
            continue
        else:
            filteredString += char
    return filteredString