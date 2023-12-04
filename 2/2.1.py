# Advent of Code 2023
# puzzle 2.1

#imports

max_red = 12
max_green = 13
max_blue = 14

with open('C:\\Users\\steve\\Documents\\AdventOfCode2023\\2\\input.txt') as f:
        lines = f.readlines()
        result = 0
        for line in lines:
            parts = line.split(':')
            header = parts[0]
            games = parts[1].split(';')
            score = 0
            #print(line)
            for game in games:
                gameparts=game.split()
                for count in range(int(len(gameparts)/2)):
                    if(gameparts[count*2+1][:3] == 'red' and int(gameparts[count*2]) > max_red):
                        score = score + 1
                    if(gameparts[count*2+1][:4] == 'blue' and int(gameparts[count*2]) > max_blue):
                        score = score + 1
                    if(gameparts[count*2+1][:5] == 'green' and int(gameparts[count*2]) > max_green):
                        score = score + 1
            if(score==0):
                result = result + int(header.split()[1])
        print(result)
