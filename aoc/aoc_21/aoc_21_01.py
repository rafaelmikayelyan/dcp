# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

test_depth = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def convert_str_array_to_int(array):
    return [int(i) for i in array]


def count_single_increase(data):
    count = 0
    i = 1
    while i < len(data):
        if data[i] > data[i - 1]:
            count += 1
        i += 1
    return count


def count_group_increase(data):
    count = 0
    i = 3
    while i < len(data):
        # test_get_sum(data, i)
        if get_sum(data, i) > get_sum(data, i - 1):
            count += 1
        i += 1
    return count


def test_get_sum(data, i):
    answer1 = sum(data[i-2:i+1])
    answer2 = data[i-2] + data[i-1] + data[i]
    print(f'{answer2} - {answer1}')


def get_sum(data, i):
    return sum(data[i-2:i+1])


def run():
    raw = read_file("aoc_21_01_input.txt")
    depths = convert_str_array_to_int(raw)
    result_single = count_single_increase(depths)
    print(f'AOC 2021-01-1: {result_single}')
    result_group = count_group_increase(depths)
    print(f'AOC 2021-01-2: {result_group}')


if __name__ == '__main__':
    run()