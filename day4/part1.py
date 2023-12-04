import re

winning_sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:

        card = line.strip().split('|')

        # Gross splicing and splitting the dataset, but it works!
        winning_numbers = set(card[0].split(':')[1].strip().split(' '))
        card_numbers = re.findall(r'\d+', card[1])

        # Create a current sum for each matching card, finding the appropriate sum to add to our overall sum
        card_sum = 0

        # Logic to determine the sum based on each matching number
        for num in card_numbers:
            if num in winning_numbers:
                if card_sum == 0:
                    card_sum = 1
                else:
                    card_sum *= 2
        
        # Add the current sum to our overall sum
        winning_sum += card_sum

print(winning_sum)