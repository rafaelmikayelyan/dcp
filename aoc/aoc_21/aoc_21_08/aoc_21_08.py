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


def count_occurrences(txt):
    count = 0
    for strings in txt:
        for s in strings[1].split(' '):
            if len(s) == 2 or len(s) == 4 or len(s) == 3 or len(s) == 7:
                count += 1
    return count


def decode_line(txt):
    decoded = [''] * 9
    for parts in txt:
        for strings in txt:
            for s in strings.split(' '):
                if len(s) == 2:
                    decoded[1] = s
                if len(s) == 4:
                    decoded[4] = s
                if len(s) == 3:
                    decoded[7] = s
                if len(s) == 7:
                    decoded[8] = s
    print(decoded)

    return False


def add_all_outputs(list):
    sum = 0
    for output in list:
        sum += output
    return sum


def run():
    # txt = read_file("input.txt")
    # txt = read_file("sample.txt")
    txt = [['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']]

    # print(txt)

    answer_1 = count_occurrences(txt)
    print(f'AOC 2021-08-1: {answer_1}')

    decoder = []

    answer_2 = decode_line(txt[0])
    print(f'AOC 2021-08-2: {answer_2}')


if __name__ == '__main__':
    run()
