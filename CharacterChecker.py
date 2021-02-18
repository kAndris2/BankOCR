#Map of the characters
characters = {
    0 : [[" ","_"," "], ["|"," ","|"], ["|","_","|"]],
    1 : [[" "," "," "], [" "," ", "|"], [" "," ","|"]],
    2 : [[" ","_"," "], [" ","_","|"], ["|","_"," "]],
    3 : [[" ","_"," "], [" ","_","|"], [" ","_","|"]],
    4 : [[" "," "," "], ["|","_","|"], [" "," ","|"]],
    5 : [[" ","_"," "], ["|","_"," "], [" ","_","|"]],
    6 : [[" ","_"," "], ["|","_"," "], ["|","_","|"]],
    7 : [[" ","_"," "], [" "," ","|"], [" "," ","|"]],
    8 : [[" ","_"," "], ["|","_","|"], ["|","_","|"]],
    9 : [[" ","_"," "], ["|","_","|"], [" ","_","|"]]
}

def getNumber(numMap):
    """
    - Checks if the number map exists in the 'characters' dictionary.
    - If yes it will returns the key as string. Anyway with a question mark.
    """
    for key in characters:
        if characters[key] == numMap:
            return str(key)
    return "?"

def getAccountNumber(numberMap):
    """
    - Return the account number as string based on account number map.
    """
    accountNumber = ""
    for number in numberMap:
        accountNumber += getNumber(number)
    return accountNumber

def countDifference(illNum, orNum):
    """
    - Counts the difference between two character map.
    """
    count = 0
    for row in range(len(illNum)):
        for i in range(len(illNum[row])):
            if illNum[row][i] != orNum[row][i]:
                count += 1
    return count


def getPossibleNumbers(numMap, indexes):
    """
    - Gets a character map and (maybe bad) indexes where it can replace the number with other possible numbers.
    - Returns an array with possible numbers based on the indexes.
    """
    possible_numbers = []
    for i in indexes:
        temp = []
        for key in characters:
            if countDifference(numMap[i], characters[key]) == 1:
                temp.append(key)
        possible_numbers.append(temp)
    return possible_numbers

def containsIllegalCharacter(accountNumber):
    """
    - If the number as str contains illegible character(s) returns True.
    """
    return "?" in accountNumber