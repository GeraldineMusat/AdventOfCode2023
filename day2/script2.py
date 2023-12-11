file = open('text.txt', 'r')

total = 0

while True:
    line = file.readline()
    if not line:
        break
    # print(line)

    line_split = line.split(': ')
    id_game = line_split[0].split()[1]
    # print('id game: ', id_game)

    games_set = line_split[1].split('; ')

    max_red = 0
    max_green = 0
    max_blue = 0

    for g in games_set:
        # print(g)
        colors = g.split(', ')
        for c in colors:
            # print(c)
            c_split = c.split()
            color = c_split[1]
            total_cube = c_split[0]

            if color == 'red' and int(total_cube) > int(max_red):
                max_red = total_cube

            elif color == 'green' and int(total_cube) > int(max_green):
                max_green = total_cube
                
            elif color == 'blue' and int(total_cube) > int(max_blue):
                max_blue = total_cube

    # print('max blue:', max_blue)
    # print('max green:', max_green)
    # print('max red:', max_red)

    total = total + (int(max_red) * int(max_blue) * int(max_green))
                    
                

        

print(total)
        