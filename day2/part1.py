sum = 0

with open('input1.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:

        line = line.strip().split(':')

        game_number = int(line[0].split(' ')[1])
        parsed_game = line[1].strip().split(';')

        is_possible = True

        for game in parsed_game:

            num_red = 12
            num_green = 13
            num_blue = 14

            game = game.strip().split(' ')
            
            for i in range(0, len(game), 2):
            
                cube_quantity = int(game[i])
                cube_color = game[i+1]
                if cube_color[-1] == ',':
                    cube_color = cube_color[:-1]
                
                if cube_color == 'red':
                    num_red -= cube_quantity
                elif cube_color == 'green':
                    num_green -= cube_quantity
                elif cube_color == 'blue':
                    num_blue -= cube_quantity

            if num_red < 0 or num_green < 0 or num_blue < 0:
                is_possible = False
                break
        
        if is_possible:
            sum += game_number

print(sum)