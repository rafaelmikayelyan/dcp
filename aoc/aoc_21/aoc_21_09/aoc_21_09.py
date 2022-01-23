def read_file(txt):
    file = open(txt, "r")
    data = file.read().splitlines()
    file.close()
    return data


def find_low_points(txt):
    low_points = []
    x = y = 0
    while y < len(txt):
        while x < len(txt[y]):
            low_point = compare_values(txt, x, y)
            if low_point is not None:
                low_points.append(low_point)
            x += 1
        y += 1
        x = 0
    return low_points


def compare_values(l, x, y):
    if less_than_left(l, x, y) and less_than_right(l, x, y) and less_than_above(l, x, y) and less_than_below(l, x, y):
        # return l[y][x]
        return [y, x]


def less_than_left(l, x, y):
    if x > 0:
        return l[y][x] < l[y][x - 1]
    else:
        return True


def less_than_right(l, x, y):
    if x < len(l[y]) - 1:
        return l[y][x] < l[y][x + 1]
    else:
        return True


def less_than_above(l, x, y):
    if y > 0:
        return l[y][x] < l[y - 1][x]
    else:
        return True


def less_than_below(l, x, y):
    if y < len(l) - 1:
        return l[y][x] < l[y + 1][x]
    else:
        return True


def get_low_point_values(low_points, txt):
    values = []
    for p in low_points:
        values.append(txt[p[0]][p[1]])
    return values


def calculate_risk_level(data):
    result = 0
    for i in data:
        result += int(i) + 1
    return result


def calculate_basins(data):
    result = 1
    for i in data:
        result = result * i
    return result


def find_basins(low_points, txt):
    result = []
    for point in low_points:
        result.append(find_basin_area(point, txt))
    return result


def find_basin_area(point, txt):

    return 1


def run():
    # txt = read_file("input.txt")
    txt = read_file("sample.txt")

    low_points = find_low_points(txt)

    answer_1 = calculate_risk_level(get_low_point_values(low_points, txt))
    print(f'AOC 2021-09-1: {answer_1}')

    basins = find_basins(low_points, txt)

    answer_2 = calculate_basins(basins)
    print(f'AOC 2021-09-2: {answer_2}')


if __name__ == '__main__':
    run()
