# passed test case 1 and 2
def main():
    print(solution(100000, 100000))

def solution(x, y):
    cells = []
    i = 1
    exit_loop = False
    while True:
        if len(cells) == 0:
            cells.append([])
            cells[0].append(i)
            i += 1
            continue
        for j in range(len(cells)):
            for k in range(len(cells[j])):
                if (cells[j][k] == (i - 1)) and (k == 1):
                    cells.append([])
                    cells[j + 1].append(i)
                elif (cells[j][k] == (i - 1)) and (k == 0):
                    if j == 0:
                        cells[j].append(i)
                    else:
                        cells[0].append(i)
                elif cells[j][k] == (i - 1):
                    cells[j + 1].append(i)
                if ((j + 1) == x) and ((k + 1) == y):
                    exit_loop = True
                if exit_loop == True:
                    break
            if exit_loop == True:
                break
        if exit_loop == True:
            break
        i += 1
    return str(cells[x - 1][y - 1])


main()