# Advent of Code 2023
# Puzzle 1.1

# imports
import re
# because, regex :)


with open('C:\\Users\\steve\\Documents\\AdventOfCode2023\\1\\input.txt','r')  as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        line = re.sub('[^0-9]','',line)
        sum = sum + int(line[:1] + line[-1:])
    print(sum)
