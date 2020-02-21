# passed all test cases
def main():
    print(solution(100000, 100000))

def solution(x, y):
    val = 1
    y_inc = 0
    x_inc = y + 1
    for i in range(y):
        val += y_inc
        y_inc += 1
    for j in range(x):
        if j == 0:
            continue
        val += x_inc
        x_inc += 1
    return str(val)

main()