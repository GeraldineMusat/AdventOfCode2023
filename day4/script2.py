file = open('text.txt', 'r')

total = 0
index = 1
total_winning_cards = {}

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

    total_matching_cards = 0

    for c in my_cards:
        if c in winner_cards:
            # print('card', index, 'winner', c)
            total_matching_cards = total_matching_cards + 1
    # print('card', index, 'total matching', total_matching_cards)
    
    # print('card', index)
    if index in total_winning_cards:
        total_winning_cards[index] += 1
    else:
        total_winning_cards[index] = 1
    
    # print('range', total_matching_cards)
    for j in range(1, total_matching_cards+1):
        # print('j',index+j)
        if index+j in total_winning_cards:
            # print('index', total_winning_cards[index])
            # print('index + 1', total_winning_cards[index+j])
            total_winning_cards[index+j] = total_winning_cards[index+j] + total_winning_cards[index]
        else:
            total_winning_cards[index+j] = total_winning_cards[index]
    # print(total_winning_cards)
    
    index += 1

for k in total_winning_cards:
    total += total_winning_cards[k]

# print(total_winning_cards)

    


print(total)
        