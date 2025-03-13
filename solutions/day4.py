def parseInput(file_name):
    word_search = []
    with open(file_name, 'r') as f:
        for line in f:
            word_search.append(line.strip())
    return word_search

word_search = parseInput("../inputs/day4_input.txt")

def part1(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    count = 0

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    for i in range(rows):
        for j in range(cols):
            # only check the position that have 'X' as the first letter
            if word_search[i][j] == 'X':
                # check all 8 directions
                for di, dj in directions:
                    if check_directions(word_search, i, j, di, dj, "XMAS"):
                        count+=1
    return count

def check_directions(word_search, i, j, di, dj, target) -> bool:
    rows = len(word_search)
    cols = len(word_search[0])
    tar_len = len(target)

    if not (0 <= i + di *(tar_len -1) < rows and 0 <= j + dj * (tar_len -1) < cols):
        return False

    for k in range(len(target)):
        if word_search[i + di * k][j + dj * k] != target[k]:
            return False
    return True

def part2(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if word_search[i][j] == 'A':
                # check X-MAS patterns
                diag1 = [
                    word_search[i - 1][j - 1],
                    word_search[i][j],
                    word_search[i + 1][j + 1]
                ]

                diag2 = [
                    word_search[i - 1][j + 1],
                    word_search[i][j],
                    word_search[i + 1][j - 1]
                ]

                diag1_str = "".join(diag1)
                diag2_str = "".join(diag2)
                
                if diag1_str in ["MAS", "SAM"] and diag2_str in ["MAS", "SAM"]:
                    count+=1
    return count


print(part2(word_search))
