def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def analyze(data):
    position = [0, 0]
    for i in data:
        i = i.split()
        if i[0] == 'forward':
            position[0] += int(i[1])
        elif i[0] == 'down':
            position[1] += int(i[1])
        elif i[0] == 'up':
            position[1] -= int(i[1])
        # print(position)
    return position


def analyze_w_aim(data):
    position = [0, 0, 0]
    for i in data:
        i = i.split()
        if i[0] == 'forward':
            position[0] += int(i[1])
            position[1] += int(i[1]) * position[2]
        elif i[0] == 'down':
            position[2] += int(i[1])
        elif i[0] == 'up':
            position[2] -= int(i[1])
    return position


def run():
    raw = read_file("aoc_21_02_input.txt")
    position = analyze(raw)
    area = position[0] * position[1]
    print(f'AOC 2021-02-1: {area}')
    position_w_aim = analyze_w_aim(raw)
    area_w_aim = position_w_aim[0] * position_w_aim[1]
    print(f'AOC 2021-02-2: {area_w_aim}')


if __name__ == '__main__':
    run()