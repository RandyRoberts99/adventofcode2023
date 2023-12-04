import re

sum = 0
numSet = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
backwardsNumSet = ("orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin")

with open('input.txt', 'r') as file_input:

    lines = file_input.readlines()

    for line in lines:

        print(line)
        left = re.search(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)', line)
        right = re.search(r'(orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)', line[::-1])

        left = left.group(0)
        right = right.group(0)

        if left in numSet:
            left = str(numSet.index(left))
        if right in backwardsNumSet:
            right = str(backwardsNumSet.index(right))

        sum += int(left + right)

print(sum)