# Advent of Code 2023
# Puzzle 1.2

# imports
import re
# It's not pretty.  It's O(N^2), but sod it.
# Honestly, it's embarrassing and would never end up in production code.
# The main issue is overlap of wordy digits  e.g.  eightwo is that 8 or 82

with open('C:\\Users\\steve\\Documents\\AdventOfCode2023\\1\\input.txt','r')  as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        lineout = ''
        for char in range(len(line)):
            if(line[char:char+1]>='0' and line[char:char+1]<='9'):
                lineout = lineout + line[char:char+1]
            if(line[char:char+3])=='one':
               lineout = lineout + '1'
            if(line[char:char+3])=='two':
               lineout = lineout + '2'
            if(line[char:char+5])=='three':
               lineout = lineout + '3'
            if(line[char:char+4])=='four':
               lineout = lineout + '4'
            if(line[char:char+4])=='five':
               lineout = lineout + '5'
            if(line[char:char+3])=='six':
               lineout = lineout + '6'
            if(line[char:char+5])=='seven':
               lineout = lineout + '7'
            if(line[char:char+5])=='eight':
               lineout = lineout + '8'
            if(line[char:char+4])=='nine':
               lineout = lineout + '9'
        #lineout = re.sub('[^0-9]','',lineout)
        sum = sum + int(lineout[:1] + lineout[-1:])
    print(sum)
