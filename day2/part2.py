sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:

        line = line.strip().split(':')

        game_number = int(line[0].split(' ')[1])
        parsed_game = line[1].strip().split(';')

        max_red = 0
        max_green = 0
        max_blue = 0

        for game in parsed_game:

            current_max_red = 0
            current_max_green = 0
            current_max_blue = 0

            game = game.strip().split(' ')
            
            for i in range(0, len(game), 2):
            
                cube_quantity = int(game[i])
                cube_color = game[i+1]
                if cube_color[-1] == ',':
                    cube_color = cube_color[:-1]
                
                if cube_color == 'red':
                    current_max_red += cube_quantity
                elif cube_color == 'green':
                    current_max_green += cube_quantity
                elif cube_color == 'blue':
                    current_max_blue += cube_quantity

            max_red = max(max_red, current_max_red)
            max_green = max(max_green, current_max_green)
            max_blue = max(max_blue, current_max_blue)
        
        sum += (max_red * max_green * max_blue)

print(sum)