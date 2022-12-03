f = open("input.txt", "r")
lines = f.readlines()
f.close()

myScore = 0

for i in range(len(lines)):
    if(lines[i][2] == 'X'): #Loose@
        myScore += 0
        if (lines[i][0] == 'A'): #Rock
            myScore+=3
        elif (lines[i][0] == 'B'):#Paper
            myScore +=1
        else: #Scissors
            myScore+=2

    elif(lines[i][2] == 'Y'):#Draw
        myScore+=3
        if (lines[i][0] == 'A'): #Rock
            myScore+=1
        elif (lines[i][0] == 'B'):#Paper
            myScore +=2
        else: #Scissors
            myScore+=3
    else : #Cas où Win
        myScore+=6
        if (lines[i][0] == 'A'): #Rock
            myScore+=2
        elif (lines[i][0] == 'B'):#Paper
            myScore += 3
        else: #Scissors
            myScore+=1

print(str(myScore))

#--- Part Two ---

