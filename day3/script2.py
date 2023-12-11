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

    number_1 = ''
    number_2 = ''
    temp = ''

    for j in range(len(line_middle)):
        # print(line_middle[j])

        if line_middle[j] == '*':
            number_1 = ''
            number_2 = ''
            if line_middle[j-1].isnumeric():
                index = 1
                while True:
                    if j-index < 0 or not line_middle[j-index].isnumeric():
                        length_str = len(temp)
                        temp = temp[length_str::-1]

                        if number_1 == '':
                            number_1 = temp
                            temp = ''
                            break
                        elif number_2 == '':
                            number_2 = temp
                            temp = ''
                            break

                    else:
                        temp = str(temp) + str(line_middle[j-index])

                    index = index + 1

            if line_middle[j+1].isnumeric():
                index = 1
                while True:
                    if j+index > len(line_middle)-2 or not line_middle[j+index].isnumeric():
                        if number_1 == '':
                            number_1 = temp
                            temp = ''
                            break
                        elif number_2 == '':
                            number_2 = temp
                            temp = ''
                            break

                    else:
                        temp = str(temp) + str(line_middle[j+index])

                    index = index + 1
            
            if line_before != '':
                if line_before[j-1].isnumeric():
                    index = 1
                    while True:
                        if j-index < 0 or not line_before[j-index].isnumeric():
                            length_str = len(temp)
                            temp = temp[length_str::-1]
                            if temp != '' and number_1 == '' and not line_before[j].isnumeric():
                                number_1 = temp
                                temp = ''
                            elif temp != '' and number_2 == '' and not line_before[j].isnumeric():
                                number_2 = temp
                                temp = ''
                            break
                        else:
                            temp = str(temp) + str(line_before[j-index])

                        index = index + 1

                    if line_before[j].isnumeric():
                        index = 0
                        while True:
                            if j+index > len(line_before)-2 or not line_before[j+index].isnumeric():
                                if temp != '' and number_1 == '':
                                    number_1 = temp
                                    temp = ''
                                elif temp != '' and number_2 == '':
                                    number_2 = temp
                                    temp = ''
                                break
                            else:
                                temp = str(temp) + str(line_before[j+index])

                            index = index + 1
                    
                elif line_before[j].isnumeric():
                    index = 0
                    while True:
                        if j+index > len(line_before)-2 or not line_before[j+index].isnumeric():
                            if temp != '' and number_1 == '':
                                number_1 = temp
                                temp = ''
                            elif temp != '' and number_2 == '':
                                number_2 = temp
                                temp = ''
                            break
                        else:
                            temp = str(temp) + str(line_before[j+index])

                        index = index + 1
                if line_before[j+1].isnumeric() and not line_before[j].isnumeric():
                    index = 1
                    while True:
                        if j+index > len(line_before)-2 or not line_before[j+index].isnumeric():
                            if temp != '' and number_1 == '':
                                number_1 = temp
                                temp = ''
                            elif temp != '' and number_2 == '':
                                number_2 = temp
                                temp = ''
                            break
                        else:
                            temp = str(temp) + str(line_before[j+index])

                        index = index + 1

            if line_after != '':
                if line_after[j-1].isnumeric():
                    index = 1
                    while True:
                        if j-index < 0 or not line_after[j-index].isnumeric():
                            length_str = len(temp)
                            temp = temp[length_str::-1]
                            if temp != '' and number_1 == '' and not line_after[j].isnumeric():
                                number_1 = temp
                                temp = ''
                            elif temp != '' and number_2 == '' and not line_after[j].isnumeric():
                                number_2 = temp
                                temp = ''
                            break
                        else:
                            temp = str(temp) + str(line_after[j-index])

                        index = index + 1

                    if line_after[j].isnumeric():
                        index = 0
                        while True:
                            if j+index > len(line_after)-2 or not line_after[j+index].isnumeric():
                                if temp != '' and number_1 == '':
                                    number_1 = temp
                                    temp = ''
                                elif temp != '' and number_2 == '':
                                    number_2 = temp
                                    temp = ''
                                break
                            else:
                                temp = str(temp) + str(line_after[j+index])

                            index = index + 1
                    
                elif line_after[j].isnumeric():
                    index = 0
                    while True:
                        if j+index > len(line_after)-2 or not line_after[j+index].isnumeric():
                            if temp != '' and number_1 == '':
                                number_1 = temp
                                temp = ''
                            elif temp != '' and number_2 == '':
                                number_2 = temp
                                temp = ''
                            break
                        else:
                            temp = str(temp) + str(line_after[j+index])

                        index = index + 1
                if line_after[j+1].isnumeric() and not line_after[j].isnumeric():
                    index = 1
                    while True:
                        if j+index > len(line_after)-2 or not line_after[j+index].isnumeric():
                            if temp != '' and number_1 == '':
                                number_1 = temp
                                temp = ''
                            elif temp != '' and number_2 == '':
                                number_2 = temp
                                temp = ''
                            break
                        else:
                            temp = str(temp) + str(line_after[j+index])

                        index = index + 1

            if number_1 != '' and number_2 != '':
                total = total + (int(number_1) * int(number_2))
                # print('number 1', number_1, ' - number 2', number_2, '*', int(number_1) * int(number_2))
                number_1 = ''
                number_2 = ''

        

    line_before = line_middle
    line_middle = line_after
    line_after = ''

    if line_middle == '':
        break

print(total)
        