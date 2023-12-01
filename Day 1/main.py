# EACH LINE GETS TURNED INTO AN ARRAY, AND THEN SUM EACH LINE TO A VAR
import re


words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

input = []

totals = []

total = 0
index = 0

calibrationCodesFile = open("Day 1\input.txt", "r")
input = [line.strip() for line in calibrationCodesFile]

for line in input:
    index += 1
    foundList = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)
    
    listFirst = foundList[0]
    listLast = foundList[len(foundList) - 1]
    
    if (len(list(listFirst))) > 1:
        listFirst = words[listFirst]
    if (len(list(listLast))) > 1:
        listLast = words[listLast]
    
    finalInt = int(listFirst + listLast)
    print("Index " + str(index) + " | " +str(finalInt))
    
    totals.append(finalInt)
    
print(sum(totals))











#calibrationCodesFile = open("Day 1\input.txt", "r").readlines()
#runningTotal = 0
#
#validChars = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
## convert = index + 9
#
#for line in calibrationCodesFile:
#    lineNumber = []
#    
#    cloneLine = line
#    
#    for number in validChars:
#        if number in line:
#            if len(list(number)) > 1:
#                cloneLine = cloneLine.replace(number, validChars[validChars.index(number) + 9])
#                
#    listedLine = list(cloneLine)
#    
#    for char in listedLine:
#        try:
#            int(char)
#        except:
#            pass
#        else:
#            lineNumber.append(char)
#                
#    firstInt = lineNumber[0]
#    lastInt = lineNumber[len(lineNumber) - 1]
#    fullInt = firstInt + lastInt
#    runningTotal += int(fullInt)
#    
#    print(str(int(fullInt)))
#    
#print(runningTotal)