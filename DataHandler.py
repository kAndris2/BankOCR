RAW_NUMBERS = "raw_numbers.txt"
MAX_NUM_IN_ACCOUNT = 9
STEP = 3 #Each number is a 3x3 list.

def writeToFile(filename, data):
    """
    - Writes the data to the file.
    """
    with open(filename, "a") as file:
        file.writelines(f"{data}\n") 

def readNumbers():
    """
    - Reads the entries and returns with account number map.
    """
    numbersStr = ""
    with open(RAW_NUMBERS, "r") as file:
        for row in file:
            if len(row) == 1:
                numbersStr += "&" #New line marking
            else:
                numbersStr += row
    return getNumbersFromString(numbersStr.split("&"))

def getNumbersFromString(rawData):
    """
    - Creates an account number map from the scanned data and returns it as result.
    """
    rawData.pop(-1)
    numbers = []
    
    for i in range(len(rawData)):
        start = 0 - STEP #First start position for the first number.
        end = (STEP - 1) - STEP #First end position for the first number.
        dataMap = rawData[i].split("\n")
        dataMap.pop(-1)
        acc_num = []
        for n in range(0, MAX_NUM_IN_ACCOUNT):
            start += STEP #Sets the next number's position.
            end += STEP
            acc_num.append(createNumber(dataMap, start, end))
        numbers.append(acc_num)
    return numbers

def createNumber(data, start, end):
    """
    - Returns a list with 3 inner list as rows in the current number map.
    """
    number = []
    temp = ""
    for row in data:
        for i,character in enumerate(row):
            if i >= start and i <= end:
                temp += character
            if i == end:
                number.append(list(temp))
                temp = ""
    return number