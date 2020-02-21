# Failed test case 5 and 10
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
            low = num - 1
            high = num + 1
            i = 1
            low_won = False
            high_won = False
            while True:
                if low % (2 ** i) == 0:
                    low_won = True
                else:
                    low_won = False
                if high % (2 ** i) == 0:
                    high_won = True
                else:
                    high_won = False
                if not low_won or not high_won:
                    break
                i += 1
            if low_won:
                num = low
                steps += 1
            else:
                num = high
                steps += 1
    return steps

main()