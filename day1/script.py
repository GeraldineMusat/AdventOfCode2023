file = open('text.txt', 'r')

total = 0

while True:
    line = file.readline()
    if not line:
        break
    #print(line)

    firstNum = 0
    lastNum = 0

    for c in line:
        # print(c)
        if c.isnumeric():
            # print(c)
            firstNum = c
            break
    
    length_str = len(line)
    sliced_str = line[length_str::-1]

    for c in sliced_str:
        # print(c)
        if c.isnumeric():
            # print(c)
            lastNum = c
            break

    #print('line: ', line)
    #print('first num', firstNum)
    #print('last num', lastNum)

    num_str = str(firstNum) + str(lastNum)
    num_int = int(num_str)

    total = total + num_int

print(total)
        