# Advent of Code 2023
# puzzle 2.1

#imports



with open('C:\\Users\\steve\\Documents\\AdventOfCode2023\\2\\input.txt') as f:
        lines = f.readlines()
        result = 0
        for line in lines:
            max_red = 0
            max_green = 0
            max_blue = 0
            parts = line.split(':')
            header = parts[0]
            games = parts[1].split(';')
            #print(line)
            for game in games:
                gameparts=game.split()
                for count in range(int(len(gameparts)/2)):
                    if(gameparts[count*2+1][:3] == 'red'):
                        max_red = max(max_red,int(gameparts[count*2]))
                    if(gameparts[count*2+1][:4] == 'blue'):
                        max_blue = max(max_blue,int(gameparts[count*2]))
                    if(gameparts[count*2+1][:5] == 'green'):
                        max_green = max(max_green,int(gameparts[count*2]))
            result = result + max_red*max_blue*max_green
        print(result)
