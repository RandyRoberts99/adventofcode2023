import re

card_sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()

    cards = [1] * len(lines)
    card_sum = 0
    for i in range(len(lines)):

        curr_card = lines[i].strip().split('|')

        # Gross but works!
        winning_numbers = set(curr_card[0].split(':')[1].strip().split(' '))
        card_numbers = re.findall(r'\d+', curr_card[1])

        matching_numbers = 0

        for num in card_numbers:
            if num in winning_numbers:
                matching_numbers += 1

        for j in range(i + 1, min(len(lines), i + 1 + matching_numbers)):
            cards[j] += cards[i]
        
        card_sum += cards[i]

print(card_sum)