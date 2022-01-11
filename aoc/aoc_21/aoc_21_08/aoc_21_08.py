def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def run():
    # txt = read_file("input.txt")
    txt = read_file("sample.txt")

    # print(txt)

    answer_1 = False
    print(f'AOC 2021-05-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-05-2: {answer_2}')


if __name__ == '__main__':
    run()
