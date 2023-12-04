sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:

        line = line.strip().split(':')

        # Grab the game number, and the bag sets associated with that game
        game_number = int(line[0].split(' ')[1])
        bag_set = line[1].strip().split(';')

        max_red = 0
        max_green = 0
        max_blue = 0

        # Loop through each bag, check if there are new max values for red, green, or blue.
        for bag in bag_set:

            current_max_red = 0
            current_max_green = 0
            current_max_blue = 0

            bag = bag.strip().split(' ')
            
            for i in range(0, len(bag), 2):
            
                cube_quantity = int(bag[i])
                cube_color = bag[i+1]
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