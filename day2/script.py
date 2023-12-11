file = open('text.txt', 'r')

total = 0

max_red = 12
max_green = 13
max_blue = 14

while True:
    line = file.readline()
    if not line:
        break
    # print(line)

    line_split = line.split(': ')
    id_game = line_split[0].split()[1]
    # print('id game: ', id_game)

    games_set = line_split[1].split('; ')
    
    try:
        for g in games_set:
            # print(g)
            colors = g.split(', ')
            for c in colors:
                # print(c)
                c_split = c.split()
                color = c_split[1]
                total_cube = c_split[0]

                if color == 'red':
                    if int(total_cube) > max_red:
                        # print('Game: ', id_game, ' - max red: ', max_red, ' total red cube ', total_cube)
                        raise StopIteration
                elif color == 'green':
                    if int(total_cube) > max_green:
                        # print('Game: ', id_game, ' - max green: ', max_green, ' total green cube ', total_cube)
                        raise StopIteration
                elif color == 'blue':
                    if int(total_cube) > max_blue:
                        # print('Game: ', id_game, ' - max blue: ', max_blue, ' total blue cube ', total_cube)
                        raise StopIteration
                

        # print('id game: ', id_game)
        total = total + int(id_game)

    except StopIteration:
        pass

print(total)
        