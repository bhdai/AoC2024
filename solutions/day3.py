import re


def parseInput(file_name):
    with open(file_name, 'r') as f:
        return f.read()

corr_mem = parseInput("../inputs/day3_input.txt")

def part1_re(corr_mem):
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", corr_mem)
    return sum(int(mul[0]) * int(mul[1]) for mul in muls)


def part1_manual(corr_mem):
    total_sum = 0
    i = 0
    while i < len(corr_mem):
        if i+4 < len(corr_mem) and corr_mem[i:i+4] == "mul(":
            i+=4
            # extract first number
            num1 = ""
            while (i < len(corr_mem) and corr_mem[i].isdigit()):
                num1+=corr_mem[i]
                i+=1
            # check for comma
            if (i < len(corr_mem) and corr_mem[i] == ',' and 1<=len(num1)<=3):
                i+=1 # skip comma
                # extract second number
                num2=""
                while(i<len(corr_mem) and corr_mem[i].isdigit()):
                    num2+=corr_mem[i]
                    i+=1
                if i < len(corr_mem) and corr_mem[i] == ')' and 1<=len(num2)<=3:
                    total_sum += int(num1) * int(num2)
                    i+=1
                    continue
        # if we get here that means no pattern matched at this posision skip to the next char
        i+=1
    return total_sum

def part2(corr_mem):
    total_sum = 0
    enabled = True
    i = 0
    while i < len(corr_mem):
        # check for do()
        if i + 4 < len(corr_mem) and corr_mem[i:i+4] == "do()":
            i+=4
            enabled = True
            continue
        # check for don't()
        if i + 7 < len(corr_mem) and corr_mem[i:i+7] == "don't()":
            i+=7
            enabled = False
            continue
        # check for mul(X,Y)
        if i+4 <= len(corr_mem) and corr_mem[i:i+4] == "mul(":
            i+=4
            num1 = ""
            while i < len(corr_mem) and corr_mem[i].isdigit():
                num1+=corr_mem[i]
                i+=1
            # check for comma
            if i < len(corr_mem) and corr_mem[i] == ',' and 1<=len(num1)<=3:
                i+=1
                num2 = ""
                while i < len(corr_mem) and corr_mem[i].isdigit():
                    num2+=corr_mem[i]
                    i+=1
                if i < len(corr_mem) and corr_mem[i] == ')' and 1<=len(num2)<=3:
                    if enabled:
                        total_sum += int(num1) * int(num2)
                        i+=1
                    continue
        i+=1
    return total_sum


print(part2(corr_mem))
