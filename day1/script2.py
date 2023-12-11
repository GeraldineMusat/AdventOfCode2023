file = open('text.txt', 'r')

total = 0
patterns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
switch={
      'one':'1',
      'two':'2',
      'three':'3',
      'four':'4',
      'five':'5',
      'six':'6',
      'seven':'7',
      'eight':'8',
      'nine':'9'
      }

while True:
    line = file.readline()
    if not line:
        break
    # print(line)
    # print(len(line) - 1)

    firstNum = 0
    lastNum = 0

    # index = line.find('8')
    # index = line.find('five')
    # index = line.find("7")
    # print(index)
    # index = line.rfind("7")
    # print(index)

    index_first_num = len(line) - 1
    index_last_num = -1

    first_str = ''
    last_str = ''

    for p in patterns:
        index_first = line.find(p)
        # print(p, '  ', index_first)
        # print('index_first ', index_first)
        # print('index_first_num ', index_first_num)
        if index_first != -1 and index_first < index_first_num:
            index_first_num = index_first
            first_str = p 
            # print('first', first_str)

        index_last = line.rfind(p)
        if index_last > index_last_num:
            index_last_num = index_last
            last_str = p
            # print('last ', last_str)
    
    if first_str.isnumeric():
        first_num = first_str
    else:
        first_num = switch.get(first_str,"Invalid input")

    if last_str.isnumeric():
        last_num = last_str
    else:
        last_num = switch.get(last_str,"Invalid input")


    # print('line: ', line)
    # print('first num', first_num)
    # print('last num', last_num)

    num_str = str(first_num) + str(last_num)
    num_int = int(num_str)
    # print(num_int)

    total = total + num_int

print(total)
        