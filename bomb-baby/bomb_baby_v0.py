# Test 3 failed [Hidden]

def solution(x, y):
    int_m = int(x)
    int_f = int(y)
    counter = 0
    while (int_m > 1) or (int_f > 1):
        if int_m > int_f:
            int_m = int_m - int_f
        else:
            int_f = int_f - int_m
        counter += 1
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
