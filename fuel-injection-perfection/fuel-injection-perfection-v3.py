# Passed test case 1, 2, 8 and 9
import math
def main():
    print(solution('4'))

def solution(n):
    num = int(n)
    steps = 0
    if num == 0:
        return 1
    if num == 1:
        return 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            steps += 1
        else:
            exp = math.log(num, 2)
            exp_low = math.floor(exp)
            exp_high = math.ceil(exp)
            low_dif = num - (2 ** exp_low)
            high_dif = (2 ** exp_high) - num
            if low_dif > high_dif:
                num += 1
                steps += 1
            else:
                num -= 1
                steps += 1
    return steps

main()