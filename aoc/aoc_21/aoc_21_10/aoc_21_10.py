BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>'}
POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}


def read_file(txt):
    file = open(txt, "r")
    data = file.read().splitlines()
    file.close()
    return data


def check_first_illegal(line):
    opened = []
    for i in line:
        if is_opening(i):
            opened.append(i)
        if is_closing(i):
            if not is_complete(opened.pop(), i):
                return i


def find_all_first_illegal(txt):
    illegal_list = []
    for i in txt:
        illegal = check_first_illegal(i)
        if illegal:
            illegal_list.append(illegal)
    return illegal_list


def is_opening(i):
    return i in BRACKETS


def is_closing(i):
    return i in BRACKETS.values()


def is_complete(opening, closing):
    return BRACKETS[opening] == closing


def score_illegal(illegal):
    score = 0
    print(illegal)
    if len(illegal) > 0:
        for i in illegal:
            score += POINTS[i]
    return score


def run():
    txt = read_file("input.txt")
    # txt = read_file("sample.txt")

    illegal_list = find_all_first_illegal(txt)

    answer_1 = score_illegal(illegal_list)
    print(f'AOC 2021-09-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-09-2: {answer_2}')


if __name__ == '__main__':
    run()
