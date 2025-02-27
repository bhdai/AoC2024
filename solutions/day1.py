from collections import Counter


def parseInput(filename: str) -> tuple[list[int], list[int]]:
    first_list = []
    second_list = []
    
    with open(filename, 'r') as f:
        for line in f:
            left, right = line.strip().split()
            first_list.append(int(left))
            second_list.append(int(right))

    return first_list, second_list

def solve_part1(first_list, second_list):
    """
    calculate the total distance between two list of number

    - sort the lists
    - find the absolute distance between coresponing elements
    - sum up these differences
    """
    left_sorted = sorted(first_list)
    right_sorted = sorted(second_list)

    abs_differences = [abs(left - right) for left, right in zip(left_sorted, right_sorted)]
    
    return sum(abs_differences)

def solve_part2(first_list, second_list):
    """
    calculate the total similarity score
    - for each number in the first list, find the number of times it appears in the second list
    - multiply them together before sum them up
    """
    right_counts = Counter(second_list)
    similarity_score = sum(num * right_counts.get(num, 0) for num in first_list)
    
    return similarity_score

if __name__ == "__main__":
    filename = "../inputs/day1_input.txt"
    first_list, second_list = parseInput(filename)

    print(solve_part2(first_list, second_list))
