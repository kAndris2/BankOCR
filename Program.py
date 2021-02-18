import DataHandler as data
import CharacterChecker as checker

TASK_3 = "number_status(task_3).txt"
TASK_4 = "number_status(task_4).txt"

STATUS_VALID = ""
STATUS_INVALID = "ERR"
STATUS_ILLEGIBLE = "ILL"
STATUS_AMB = "AMB"

#User Story 1
def getNumbers():
    """
    - Returns a dictionary based on scanned entries.
    - The key will be the number and the value will be the account number map.
    """
    numbers = {}
    for accountNumber in data.readNumbers():
       numbers[checker.getAccountNumber(accountNumber)] = accountNumber
    return numbers

#User Story 2
def checksum_calculation(numbers):
    return (
       numbers["d1"]+2 * 
       numbers["d2"]+3 * 
       numbers["d3"]+4 * 
       numbers["d4"]+5 * 
       numbers["d5"]+6 * 
       numbers["d6"]+7 * 
       numbers["d7"]+8 * 
       numbers["d8"]+9 * 
       numbers["d9"]
       ) % 11 == 0

def getNumbersWithPositions(accountNumber):
    """
    - Creates a dictionary for the checksum_calculation.
    """
    numbers = {}
    for i,number in enumerate(accountNumber):
        numbers[f"d{len(accountNumber)-i}"] = int(number)
    return numbers

def getNumberStatus(accountNumber):
    """
    - It returns the status of the number.
    """
    status = STATUS_VALID

    if checker.containsIllegalCharacter(accountNumber):
        status = STATUS_ILLEGIBLE
    else:
        num_with_pos = getNumbersWithPositions(accountNumber)

        if checksum_calculation(num_with_pos) == False:
            status = STATUS_INVALID
    return status

#User Story 3
def writeNumberWithStatus(accountNumber, status):
    """
    - Writes the result to file. 
    """
    data.writeToFile(TASK_3, f"{accountNumber} {status}")

def getInvalidNumbers():
    """
    - Gets the numbers with ILL or ERR status.
    - Returns a dictioanry.
    """
    numMap = getNumbers()
    numbers = {}
    for number in numMap:
        if getNumberStatus(number) != STATUS_VALID:
            numbers[number] = numMap[number]
    return numbers

def getInvalidNumbersIndex(accountNumber, status):
    """
    - Return a list with the account number's invalid indexis.
    """
    indexes = []
    if status == STATUS_ILLEGIBLE: #Find all question mark in the account number and append it's index to the list.
        for i,character in enumerate(accountNumber):
            if character == "?":
                indexes.append(i)
        return indexes
    elif status == STATUS_INVALID: #In this case, all of indexes added to the list.
        for i in range(len(accountNumber)):
            indexes.append(i)
        return indexes

def tryToValidate(accountNumber, bad_indexes, possible_numbers):
    """
    - It try to validate the account number based on the recieved datas.
    - After this operation, it writes the resul to a file.
    """
    def getStatus(count):
        """
        - Returns a state based on the count of possible numbers.
        """
        if count == 0: return STATUS_ILLEGIBLE
        elif count == 1: return STATUS_VALID
        elif count >= 2: return STATUS_AMB

    charMap = list(accountNumber)
    count = 0
    tempNumber = ""

    for i,index in enumerate(bad_indexes):
        for n,numbers in enumerate(possible_numbers):
            if (i == n):
                for number in numbers:
                    temp = charMap[index]
                    charMap[index] = str(number)
                    newNumber = "".join(charMap)
                    num_with_pos = getNumbersWithPositions(newNumber)

                    if checksum_calculation(num_with_pos) == True:
                        count += 1
                        tempNumber = newNumber
                    charMap[index] = temp

    data.writeToFile(TASK_4, f"{tempNumber if count == 1 else accountNumber} {getStatus(count)}")

#User Story 4
def validateIllegalNumbers():
    """
    - Collects all bad indexes and possible numbers for the bad indexes and sends it to the validator definition.
    """
    numbers = getInvalidNumbers()
    for accNumber in numbers:
        bad_indexes = getInvalidNumbersIndex(accNumber, getNumberStatus(accNumber))
        possible_numbers = checker.getPossibleNumbers(numbers[accNumber], bad_indexes)
        tryToValidate(accNumber, bad_indexes, possible_numbers)

def start():
    for number in getNumbers():
        writeNumberWithStatus(number, getNumberStatus(number))
    validateIllegalNumbers()

start()