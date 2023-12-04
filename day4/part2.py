import re

card_sum = 0

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()

    # Create a deck of cards, where each card represents the number clones we have
    # for each unique card
    cards = [1] * len(lines)
    card_sum = 0
    for i in range(len(lines)):

        curr_card = lines[i].strip().split('|')

        # Gross splicing and splitting the dataset, but it works!
        winning_numbers = set(curr_card[0].split(':')[1].strip().split(' '))
        card_numbers = re.findall(r'\d+', curr_card[1])

        # Create and find the sum of matching numbers
        matching_numbers = 0

        for num in card_numbers:
            if num in winning_numbers:
                matching_numbers += 1

        # Add to our deck of cards based on the number of matches
        # For example: if we have 4 matches, we'll take our current stack count,
        # and add that to the next 4 cards
        # If we start with [2, 1, 1, 1, 1] and have 4 matches, we'll end up with 
        # [2, 3, 3, 3, 3]
        for j in range(i + 1, min(len(lines), i + 1 + matching_numbers)):
            cards[j] += cards[i]
        
        # Get our current card count, and add it to our overall sum
        card_sum += cards[i]

print(card_sum)