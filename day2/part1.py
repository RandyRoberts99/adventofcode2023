sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:

        line = line.strip().split(':')

        # Grab the game number, and the bag sets associated with that game
        game_number = int(line[0].split(' ')[1])
        bag_set = line[1].strip().split(';')

        # State for checking if the game is still possible
        is_possible = True

        # Loop through each bag set, check if the game can be played using each set.
        for bag in bag_set:

            num_red = 12
            num_green = 13
            num_blue = 14

            bag = bag.strip().split(' ')

            # Loop through each bag set, subtracting from the maximum number of cubes respectively.
            for i in range(0, len(bag), 2):
            
                cube_quantity = int(bag[i])
                cube_color = bag[i+1]
                if cube_color[-1] == ',':
                    cube_color = cube_color[:-1]
                
                if cube_color == 'red':
                    num_red -= cube_quantity
                elif cube_color == 'green':
                    num_green -= cube_quantity
                elif cube_color == 'blue':
                    num_blue -= cube_quantity
            
            # If the current bag set is not possible, then the whole game is not possible.
            if num_red < 0 or num_green < 0 or num_blue < 0:
                is_possible = False
                break
        
        # Add to the sum if the game is possible
        if is_possible:
            sum += game_number

print(sum)