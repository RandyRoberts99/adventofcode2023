engine_sum = 0
engine = []

# Responsible for searching left and right for the bounds of the current number and adding it to the sum,
# then replacing the number with a '.' to avoid double counting
def search_engine(eng, i, j, eng_sum):

    l = j
    r = j

    while l - 1 > -1 and eng[i][l - 1].isdigit():
        l -= 1

    while (r + 1) < len(eng[i]) and eng[i][r + 1].isdigit():
        r += 1
    
    eng_sum += int("".join(eng[i][l:r+1]))

    for a in range(l, r+1):
        eng[i][a] = '.'

    return eng, eng_sum

with open('input2.txt', 'r') as file_input:

    lines = file_input.readlines()
    for line in lines:
        engine.append(list(line.strip()))

# Search the engine
for i in range(len(engine)):
    for j in range(len(engine[i])):

        # When you find a special character, search the adjacent indices for numbers
        if engine[i][j] != '.' and not engine[i][j].isdigit():

            # Bounds of our adjacent search
            u = max(0, i-1)
            d = min(i+2, len(engine))
            l = max(0, j-1)
            r = min(j+2, len(engine[i]))

            for a in range(u, d):
                for b in range(l, r):
                    
                    curr = engine[a][b]

                    # If we find a number, search the engine for the bounds of the number
                    if curr.isdigit():
                        engine, engine_sum = search_engine(engine, a, b, engine_sum)

print(engine_sum)