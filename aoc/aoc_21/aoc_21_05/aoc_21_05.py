def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def split_input(raw):
    output = []
    row = []
    temp = []
    for string in raw:
        temp = string.split(' -> ')
        for xy in temp:
            for i in xy.split(','):
                row.append(int(i))
        output.append(row)
        row = []
    return output


def get_map_dimensions(lines):
    max_x = max_y = 0
    for line in lines:
        if line[0] > max_x:
            max_x = line[0]
        if line[2] > max_x:
            max_x = line[2]
        if line[1] > max_y:
            max_y = line[1]
        if line[3] > max_y:
            max_y = line[3]
    # return [[0] * max_x] * max_y
    map = []
    y = 0
    while y < max_y + 1:
        map.append([0] * (max_x + 1))
        y += 1
    # [[0] * max_x] * max_y
    # map = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # print(map)
    return map


def print_map(map):
    string = ''
    for row in map:
        for i in row:
            if i != 0:
                string = string + str(i)
            else:
                string = string + '.'
        print(string)
        string = ''


def deep_copy(map):
    deep_copy = []
    for row in map:
        deep_copy.append(row[:])
    return deep_copy


def map_orthogonal_lines(lines, map):
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                map[y][x1] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                map[y1][x] += 1
    return map


def map_diagonal_lines(lines, map):
    for line in lines:
        dif = (abs(line[0] - line[2])) + 1
        i = 0
        if (abs(line[0] - line[2]) == abs(line[1] - line[3])):
            x1, y1, x2, y2 = line
            if y1 < y2:
                if x1 < x2:
                    while i < dif:
                        map[y1 + i][x1 + i] += 1
                        i += 1
                if x1 > x2:
                    while i < dif:
                        map[y1 + i][x1 - i] += 1
                        i += 1
            if y1 > y2:
                if x1 < x2:
                    while i < dif:
                        map[y1 - i][x1 + i] += 1
                        i += 1
                if x1 > x2:
                    # print(line)
                    # print_map(map)
                    while i < dif:
                        map[y1 - i][x1 - i] += 1
                        i += 1
                    # print("-----")
                    # print_map(map)
    return map


def check_overlaps(map):
    counter = 0
    for row in map:
        for i in row:
            if i > 1:
                counter += 1
    return counter


def run():
    raw = read_file("input.txt")
    # raw = read_file("sample.txt")

    lines = split_input(raw)
    map = get_map_dimensions(lines)

    map_w_ortho_lines = map_orthogonal_lines(lines, map)
    # map_w_ortho_lines = map_orthogonal_lines(lines, deep_copy(map))
    answer_1 = check_overlaps(map_w_ortho_lines)
    print(f'AOC 2021-05-1: {answer_1}')

    map_w_all_lines = map_diagonal_lines(lines, map)
    # map_w_all_lines = map_diagonal_lines(lines, deep_copy(map))
    answer_2 = check_overlaps(map_w_all_lines)
    print(f'AOC 2021-05-2: {answer_2}')

    # print_map(map)
    # print_map(map_w_ortho_lines)
    # print_map(map_w_all_lines)

if __name__ == '__main__':
    run()
