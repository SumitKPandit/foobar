def main():
    print(solution([-1000, 10, 30, -10, -50]))

def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    working = []
    faulty = []
    value = 1
    working_sum = 0
    total_sum = 0
    for elem in xs:
        total_sum += abs(elem)
        if elem < 0:
            faulty.append(elem)
        else:
            working.append(elem)
            if elem != 0:
                value *= elem
                working_sum += elem
    if len(faulty) % 2 == 0:
        faulty.sort(reverse=True)
        for elem in faulty:
            value *= elem
    else:
        faulty.sort()
        for i in range(len(faulty) - 1):
            value *= faulty[i]
    if (len(xs) == (len(working) + 1)) and (working_sum == 0):
        return str(0)
    return str(value)

main()