def parseInput(filename:str):
    reports = []

    with open(filename, 'r') as f:
        for line in f:
            report = line.strip().split()
            reports.append(list(map(int, report)))

    return reports

reports = parseInput("../inputs/day2_input.txt")

def safe_check(report):
    if report[0]==report[1]: return 0
    is_increased = report[0]<report[1]
    for i in range(0, len(report) - 1):
        diff = report[i+1] - report[i]
        if is_increased and not (1<=diff<=3): return 0
        if not is_increased and not (-3<=diff<=-1): return 0
    return 1

def enhanced_safe_check(report):
    if safe_check(report): return 1
    
    for i in range(len(report)):
        if (len(report)<=1): continue
        
        modified_list = report[:i] + report[i+1:]
        if safe_check(modified_list): return 1
    return 0

def part1(reports):
    return sum(map(safe_check, reports))

def part2(reports: list[list[int]]):
    return sum(map(enhanced_safe_check, reports))

print(part2(reports))
