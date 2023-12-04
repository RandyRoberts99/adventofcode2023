import re

sum = 0

# Create a couple sets for easy lookups of letter-based digits
numSet = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
backwardsNumSet = ("orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin")

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()

    for line in lines:

        # Grab the first and last digit, and add them to the sum using regex
        left = re.search(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)', line)
        right = re.search(r'(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)', line[::-1])

        left = left.group(0)
        right = right.group(0)

        # If the digit is a letter, replace it with its index in the numSet
        if left in numSet:
            left = str(numSet.index(left))
        if right in backwardsNumSet:
            right = str(backwardsNumSet.index(right))

        # Add the digits to the sum
        sum += int(left + right)

print(sum)