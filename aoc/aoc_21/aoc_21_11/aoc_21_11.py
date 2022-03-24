def read_file(txt):
    file = open(txt, "r")
    data = file.read().splitlines()
    file.close()
    return data


def run():
    # txt = read_file("input.txt")
    txt = read_file("sample.txt")

    answer_1 = False
    print(f'AOC 2021-09-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-09-2: {answer_2}')


if __name__ == '__main__':
    run()
