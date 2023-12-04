sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()

    # On each line, grab the first digit and the last digit, and add them to the sum
    for line in lines:

        left = 0
        right = 0

        for i in range(len(line)):
            if line[i].isdigit():
                left = line[i]
                break
                
        for i in range(len(line) - 1, -1 , -1):
            if line[i].isdigit():
                right = line[i]
                break

        sum += int(left + right)

print(sum)