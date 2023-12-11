file = open('text.txt', 'r')

total = 0

while True:
    line = file.readline()
    if not line:
        break
    # print(line)

    line_tab = line.split()

    winner_cards = []
    my_cards = []

    are_my_cards = False

    for i in range(2, len(line_tab)):
        # print(line_tab[i])
        e = line_tab[i]

        if e == '|':
            are_my_cards = True

        if not are_my_cards and e.isnumeric():
            winner_cards.append(e)
        elif are_my_cards and e.isnumeric():
            my_cards.append(e)

    # print('my cards', my_cards)
    # print('winner cards', winner_cards)

    last_added_n = 0
    index = 0

    for c in my_cards:
        if c in winner_cards:
            index = index + 1
            # print('winner', c)
            # print('last added', last_added_n)
            # print(last_added_n)
            if index == 1:
                last_added_n = 1
            else:
                last_added_n = last_added_n*2
    

    total = total + last_added_n


print(total)
        