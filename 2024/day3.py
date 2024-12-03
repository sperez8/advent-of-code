import re

RE_MUL_PATTERN = r"mul\([0-9]+,[0-9]+\)"
RE_MUL_PATTERN_DONT = r"mul\([0-9]+,[0-9]+\)||do\(\)||don't\(\)"
RE_MUL_PATTERN_GROUPS = r"mul\(([0-9]+),([0-9]+)\)"

def scan_mul(line):
    mul = re.compile(RE_MUL_PATTERN)
    patterns = re.findall(mul, line)

    return patterns

def scan_mul_dont(line):
    mul = re.compile(RE_MUL_PATTERN_DONT)
    patterns = re.findall(mul, line)
    return patterns

def multiply_pattern(pattern):
    result = re.search(RE_MUL_PATTERN_GROUPS, pattern)
    return int(result.group(1))*int(result.group(2))

def solve(file):
    total = 0
    doit = True
    for line in file:
        patterns = scan_mul_dont(line)
        for pattern in patterns:
            if pattern == "don't()":
                doit = False
            elif pattern == "do()":
                doit = True
            elif pattern:
                if doit:
                    total += multiply_pattern(pattern)
    return total
        
        
if __name__ == "__main__":
    # Open the file in read mode
    with open('input_day3.txt', 'r') as file:
        result = solve(file)
        print(f"And the answer is {result}")
