# passed test case 1, 2 and 9
def main():
    print(solution('15'))

def solution(n):
    i = 0
    if int(n) == 0:
        return 1
    while True:
        if (2 ** i) >= int(n):
            break
        i += 1
    high = 2 ** i
    low = 2 ** (i - 1)
    low_dif = int(n) - low
    high_dif = high - int(n)
    if high == int(n):
        return i
    if low_dif > high_dif:
        return high_dif + i
    else:
        return low_dif + (i - 1)

main()