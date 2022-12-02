f = open("input.txt", "r")
lines = f.readlines()
f.close()

sum = 0
list=[]

for k in range(len(lines)):
    if(lines[k] == "\n"):
        list.append(sum)
        sum=0
    else :
        sum+=int(lines[k])
list.sort()
print(str(list[-1]))


#Puzzle answer : 70296

# -------- Part Two ----------

############## Instruction ##############
#By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
#
#To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
#
#In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.
#
#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

topThree = list[-1] + list[-2] + list[-3]
print(str(topThree))