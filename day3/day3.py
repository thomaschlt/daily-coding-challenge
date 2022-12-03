f = open("input.txt", "r")
lines = f.readlines()
f.close()

fcompartment = " "
scompartment = " "
common2 = " "
sumP = 0

for i in range(len(lines)):
    fcompartment = lines[i][:len(lines[i]) // 2]
    scompartment = lines[i][len(lines[i]) // 2:]

    common = set(fcompartment) & set(scompartment)
    k = next(iter(common))

    if k.isupper():
        sumP += ord(k) - 38
    else :
        sumP += ord(k) - 96

# ----- Part Two --------- #
sum2 = 0

for i in range(0,len(lines),3):
    felement = lines[i][:len(lines)-1]
    selement = lines[i+1][:len(lines)-1]
    telement = lines[i+2][:len(lines)-1]

    str =""
    for w in felement:
        if w in selement:
            if w in telement:
                str+=w
    k = str[0]
    print(k)

    if k.isupper():
        sum2 += ord(k) - 38
    else :
        sum2 += ord(k) - 96

print(sum2)
#Your puzzle answer was 2499.


