def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return split_parts(data)


def split_parts(data):
    parts = [''] * len(data)
    i = 0
    for part in data:
        parts[i] = part.split(' | ')
        i += 1
    return parts


def run():
    txt = read_file("input.txt")
    # txt = read_file("sample.txt")

    answer_1 = False
    print(f'AOC 2021-09-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-09-2: {answer_2}')


if __name__ == '__main__':
    run()
