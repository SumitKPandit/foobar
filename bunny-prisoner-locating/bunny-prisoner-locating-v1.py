# passed test case 1, 2 and 5
def main():
    print(solution(3, 2))

def solution(x, y):
    cells = []
    i = 1
    counter = {}
    last_number = {'x': 0, 'y': 0}
    while True:
        if len(cells) == 0:
            cells.append([])
            cells[0].append(i)
            counter[0] = 1
            last_number['x'] = 0
            last_number['y'] = 0
            i += 1
            continue
        if last_number['y'] == 0:
            cells[0].append(i)
            counter[0] += 1
            last_number['x'] = 0
            last_number['y'] = counter[0] - 1
        elif last_number['y'] == 1:
            cells.append([])
            cells[last_number['x'] + 1].append(i)
            counter[last_number['x'] + 1] = 1
            last_number['x'] += 1
            last_number['y'] = 0
        else:
            cells[last_number['x'] + 1].append(i)
            counter[last_number['x'] + 1] += 1
            last_number['x'] += 1
            last_number['y'] -= 1
        if last_number['x'] == x and last_number['y'] == y:
            break
        i += 1
    return str(cells[x - 1][y - 1])


main()