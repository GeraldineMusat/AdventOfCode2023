file = open('text.txt', 'r')

total = 0

line_before = ''
line_middle = ''
line_after = ''

i = 0

while True:
    line_after = file.readline()
    if not line_after:
        line_after = ''

    if line_middle == '':
        pass
    
    # print(line_middle[0])
    # print('before', line_before)
    # print('middle', line_middle)
    # print('after', line_after)
    
    index_start = -1
    index_end = -1

    number = ''

    for j in range(len(line_middle)):
        # print(line_middle[j])
        if line_middle[j].isnumeric():
            if number == '':
                index_start = j

            number = str(number) + str(line_middle[j])

            if j == len(line_middle) - 1 or not line_middle[j+1].isnumeric():
                index_end = j

                # print(number)

                # print(line_after)

                if index_start > 0 and line_middle[index_start-1] != '.':
                    total = total + int(number)
                    # print(int(number))
                    number = ''
                elif index_end < (len(line_middle)-2) and line_middle[index_end+1] != '.':
                    # print(len(line_middle))
                    total = total + int(number)
                    # print(int(number))
                    number = ''
                if line_before != '' and number != '':
                    for k in range(index_start-1, index_end+2):
                        if not line_before[k].isnumeric() and line_before[k] != '.' and k > 0 and k < len(line_middle)-2:
                            total = total + int(number)
                            # print(int(number))
                            number = ''
                            break
                if line_after != '' and number != '':
                    for l in range(index_start-1, index_end+2):
                        if not line_after[l].isnumeric() and line_after[l] != '.' and l > 0 and l < len(line_middle)-2:
                            total = total + int(number)
                            # print(int(number))
                            number = ''
                            break
                
                if number != '':
                    # print('this number does not count', number)
                    number = ''
                    
    line_before = line_middle
    line_middle = line_after
    line_after = ''

    if line_middle == '':
        break



print(total)
        