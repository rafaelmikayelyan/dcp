def read_file(txt):
    file = open(txt, "r")
    data = file.read().splitlines()
    file.close()
    return data


def convert_to_int(data):
    matrix = []
    i = 0
    for y in data:
        matrix.append([])
        for x in y:
            matrix[i].append(int(x))
        i += 1
    return matrix


def increment(matrix, n):
    total_flashes = 0
    for i in range(0, n):
        charged = []
        add_charge(matrix, charged)
        flash(matrix, charged)
        total_flashes = recharge(matrix, charged, total_flashes)
    print(f'matrix:  {matrix}')
    print(f'charged: {charged}')
    print(f'flashes: {total_flashes}')
    pm(matrix, [-1, -1])
    return total_flashes


def add_charge(matrix, charged):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] += 1
            if matrix[y][x] == 10:
                charged.append([y, x])


def flash(matrix, charged):
    for i in charged:
        flash_aoe(matrix, i, charged)


def flash_aoe(matrix, i, charged):
    print(' ! new point !')
    pm(matrix, i)
    if i == [2,2]:
        print(' -> new flash:')
    for y in range(i[0] - 1, i[0] + 2):
        for x in range(i[1] - 1, i[1] + 2):
            print(f' ---- @[{i[1]},{i[0]}] : [{x},{y}] ------------ {range(i[0] - 1, i[1] + 2)}[x,y]')
            if -1 < y < len(matrix) and -1 < x < len(matrix[0]):
                if matrix[y][x] != 10:
                    matrix[y][x] += 1
                    pm(matrix, i)
                    if matrix[y][x] == 10:
                        charged.append([y, x])
                        print(f' -> add [{x},{y}] flash')
                        flash_aoe(matrix, [y, x], charged)


def recharge(matrix, charged, total_flashes):
    for y, x in charged:
        matrix[y][x] = 0
        total_flashes += 1
    return total_flashes


def pm(matrix, octopus_flash):
    for y in range(len(matrix)):
        line = ''
        for x in range(len(matrix[y])):
            a = ''
            if y == octopus_flash[0] and x == octopus_flash[1]:
                a = '!'
            elif matrix[y][x] == 10:
                a = '.'
            else:
                a = matrix[y][x]
            line = line + ' ' + str(a)
        print(line)
    print()


def run():
    # txt = read_file("input.txt")
    txt = read_file("sample.txt")

    list_0 = ['11111', '19991', '19191', '19991', '11111']
    list_1 = ['5483143223', '2745854711', '5264556173', '6141336146', '6357385478', '4167524645', '2176841721', '6882881134', '4846848554', '5283751526']

    octopuses = convert_to_int(list_1)

    answer_1 = increment(octopuses, 2)
    print(f'AOC 2021-09-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-09-2: {answer_2}')


if __name__ == '__main__':
    run()
