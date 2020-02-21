# passed test case 1, 2 and 9
import math

def main():
    print(solution('4'))

def solution(n):
    if int(n) == 0:
        return 1
    i = math.log(int(n), 2)
    i_low = int(math.floor(i))
    i_high = int(math.ceil(i))
    high = 2 ** i_high
    low = 2 ** (i_low - 1)
    low_dif = int(n) - low
    high_dif = high - int(n)
    if high == int(n):
        return i_high
    if low_dif > high_dif:
        return high_dif + i_high
    else:
        return low_dif + (i_low - 1)

main()