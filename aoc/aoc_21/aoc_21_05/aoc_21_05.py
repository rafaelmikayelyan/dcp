def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def run():
    # raw = read_file("input.txt")
    raw = read_file("sample.txt")

    answer_1 = False
    print(f'AOC 2021-05-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-05-2: {answer_2}')

if __name__ == '__main__':
    run()
