
def both_same_sign(a,b):
    return (a>=0 and b>=0) or (a<=0 and b<=0)

def unsafe_level_combo(diff, prev_diff):
    return diff == 0 or (diff > 3 or diff < -3) or not both_same_sign(prev_diff,diff)

def is_report_safe(report, use_problem_dampener):
    diff=0
    prev_diff=0
    safe = True
    if use_problem_dampener:
        problem_dampener_used = False
    else:
        problem_dampener_used = True
    a=report[0]
    b=report[1]
    i = 2

    while True:
        diff = a-b
        print(report)
        print(a,b, diff, prev_diff, problem_dampener_used)
        # if we hit an unsafe condition
        if unsafe_level_combo(diff, prev_diff):
            if problem_dampener_used:
                # we already had one unsafe level, so this report is definitely unsafe
                safe = False
                break
            else:
                # first unsafe level, so keep track of that
                problem_dampener_used = True

                # check we aren't at the end
                if i==len(report):
                    break

                # Now we keep a but iterate b
                b = report[i]
                i += 1
                print("NEW", a, b)
        elif i==len(report):
            break
        else:
            prev_diff = diff
            a = b
            b = report[i]
            i += 1
            print("all good")

    print("safe" if safe else "unsafe", "\n")
    return safe

def solve(file):
    count_safe = 0
    for raw_report in file:
        report = [int(r) for r in raw_report.split(" ")]
        reversed_report = list(reversed(report))
        # just in case it was one of the very first two levels that had to be eliminated, we also check the report reversed
        if is_report_safe(report=report, use_problem_dampener=True) or is_report_safe(report=reversed_report, use_problem_dampener=True):
            count_safe += 1
    return count_safe
        
        

if __name__ == "__main__":
    # Open the file in read mode
    with open('day2_input.txt', 'r') as file:
        result = solve(file)
        print(f"And the answer is {result}")
