# Test 4 passed [Hidden]

from math import floor

def solution(x, y):
    int_m = int(x)
    int_f = int(y)
    if (int_m == int_f) and (int_m != 1):
        return "impossible"
    counter = 0
    while (int_m > 1) or (int_f > 1):
        if int_m > int_f:
            if (int_m % int_f) == 0:
                counter += (floor(int_m / int_f) - 1)
                int_m = int_m - (int_f * (floor(int_m / int_f) - 1))
            else:
                counter += floor(int_m / int_f)
                int_m = int_m - (int_f * floor(int_m / int_f))
        else:
            if (int_f % int_m) == 0:
                counter += (floor(int_f / int_m) - 1)
                int_f = int_f - (int_m * (floor(int_f / int_m) - 1))
            else:
                counter += floor(int_f / int_m)
                int_f = int_f - (int_m * floor(int_f / int_m))
        if (int_m == int_f) and (int_m != 1):
            return "impossible"
        if (int_m == 0) or (int_f == 0):
            return "impossible"
    return str(counter)

def main():
    m1 = "100000000000000000000000000000000000000000000000000"
    f1 = "100000000000000000000000000000000000000000000000001"
    print(f"M = '2' and F = '1' => \"{solution('2', '1')}\"")
    print(f"M = '2' and F = '4' => \"{solution('2', '4')}\"")
    print(f"M = '4' and F = '7' => \"{solution('4', '7')}\"")
    print(f"M = \"{m1}\" and F = \"{f1}\" => \"{solution(m1, f1)}\"")

if __name__ == "__main__":
    main()
