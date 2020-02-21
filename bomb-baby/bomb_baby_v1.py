from math import floor

def solution(x, y):
    int_m = int(x)
    int_f = int(y)
    if (int_m == int_f) and (int_m != 1):
        return "impossible"
    counter = 0;
    while (int_m > 1) or (int_f > 1):
        if int_m > int_f:
            # int_m = int_m - (int_f * floor(int_m / int_f))
            # counter += floor(int_m / int_f)
            int_m = int_m - int_f
            counter += 1
        else:
            # int_f = int_f - (int_m * floor(int_f / int_m))
            # counter += floor(int_f / int_m)
            int_f = int_f - int_m
            counter += 1
        if (int_m == 0) or (int_f == 0):
            counter = "impossible"
            break
    return str(counter)

def main():
    # print(solution('100000000000000000000000000000000000000000000000000', '100000000000000000000000000000000000000000000000001'))
    print(solution('4', '7'))

if __name__ == "__main__":
    main()
