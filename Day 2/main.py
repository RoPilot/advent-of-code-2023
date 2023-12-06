# ONLY 12 RED CUBES
# ONLY 13 GREEN CUBES
# ONLY 14 BLUE CUBES

import re


limits = {"red": 12, "green": 13, "blue": 14}

input = []

totalIds = 0

calibrationCodesFile = open("Day 2\input.txt", "r")
input = [line.strip() for line in calibrationCodesFile]

for line in input:
    
    #totals = {"red": 0, "green": 0, "blue": 0}
    
    gameNum_Cols = line.split(":")
    gameNum = gameNum_Cols[0].split(" ")[1]
    
    bags = gameNum_Cols[1].split(";")
    
    tooHigh = False
    
    print(bags)

    for bag in bags:
        #print(bag)
        
        cubes = bag.split(",")
        for cube in cubes:
            print(cube)
        
            num_col = cube.split(" ")
            num_col.pop(0)
            print(num_col)
            num = num_col[0]
            col = num_col[1]

            if int(num) > limits[col]:
                tooHigh = True
    
    
    if tooHigh:
        totalIds += int(gameNum)
        print(gameNum)
    
    print("--------")
    
#print(sum(totals))

print(totalIds)