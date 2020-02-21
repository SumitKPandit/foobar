def solution(x, y):
    int_m = int(x)
    int_f = int(y)
    steps = 0
    while (int_m != 1) or (int_f != 1):
        if (int_m == int_f) and (steps > 0):
            return "impossible"
        if int_m > int_f:
            if (int_m % int_f) == 0:
                steps += ((int_m // int_f) - 1)
                int_m -= (int_f * ((int_m // int_f) - 1))
            else:
                steps += (int_m // int_f)
                int_m -= (int_f * (int_m // int_f))
        if int_f > int_m:
            if (int_f % int_m) == 0:
                steps += ((int_f // int_m) - 1)
                int_f -= (int_m * ((int_f // int_m) - 1))
            else:
                steps += (int_f // int_m)
                int_f -= (int_m * (int_f // int_m))
    return str(steps)
        
# Code for testing below
def main():
    m1 = "100000000000000000000000000000000000000000000000000"
    f1 = "100000000000000000000000000000000000000000000000001"
    print(f"M = '2' and F = '1' => \"{solution('2', '1')}\"")
    print(f"M = '2' and F = '4' => \"{solution('2', '4')}\"")
    print(f"M = '4' and F = '7' => \"{solution('4', '7')}\"")
    print(f"M = \"{m1}\" and F = \"{f1}\" => \"{solution(m1, f1)}\"")
    print(f"M = '6' and F = '7' => \"{solution('6', '7')}\"")
    print(f"M = '5' and F = '7' => \"{solution('5', '7')}\"")
    print(f"M = '4' and F = '7' => \"{solution('4', '7')}\"")


if __name__ == "__main__":
    main()