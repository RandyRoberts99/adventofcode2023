import re

winning_sum = 0

with open('input1.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:

        card = line.strip().split('|')

        # Gross but works!
        winning_numbers = set(card[0].split(':')[1].strip().split(' '))
        card_numbers = re.findall(r'\d+', card[1])
        print(card_numbers)

        card_sum = 0

        for num in card_numbers:
            if num in winning_numbers:
                if card_sum == 0:
                    card_sum = 1
                else:
                    card_sum *= 2
        
        winning_sum += card_sum

print(winning_sum)