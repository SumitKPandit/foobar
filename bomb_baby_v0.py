def solution(x, y):
    int_m = int(x)
    int_f = int(y)
    counter = 0;
    while (int_m > 1) or (int_f > 1):
        if int_m > int_f:
            int_m = int_m - int_f
        else:
            int_f = int_f - int_m
        counter += 1
        if (int_m == 0) or (int_f == 0):
            counter = "impossible"
            break
    return str(counter)

def main():
    print(solution('4', '7'))

if __name__ == "__main__":
    main()
