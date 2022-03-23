BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>'}
POINTS_CORRUPTED = {')': 3, ']': 57, '}': 1197, '>': 25137}
POINTS_INCOMPLETE = {')': 1, ']': 2, '}': 3, '>': 4}


def read_file(txt):
    file = open(txt, "r")
    data = file.read().splitlines()
    file.close()
    return data


def check_line_illegal(line):
    opened = []
    for i in line:
        if is_opening(i):
            opened.append(i)
        if is_closing(i):
            if not is_complete(opened.pop(), i):
                return {"corrupted": i}
    if opened:
        return {"incomplete": opened}


def find_all_illegal(txt):
    list_corrupted = []
    list_incomplete = []
    for i in txt:
        illegal = check_line_illegal(i)
        if "corrupted" in illegal:
            list_corrupted.append(illegal["corrupted"])
        else:
            list_incomplete.append(illegal["incomplete"])
    return list_corrupted, list_incomplete


def is_opening(i):
    return i in BRACKETS


def is_closing(i):
    return i in BRACKETS.values()


def is_complete(opening, closing):
    return BRACKETS[opening] == closing


def score_corrupted(corrupted):
    score = 0
    if len(corrupted) > 0:
        for i in corrupted:
            score += POINTS_CORRUPTED[i]
    return score


def value_of_incomplete_bracket(bracket):
    return POINTS_INCOMPLETE[BRACKETS[bracket]]


def score_incomplete_line(incomplete):
    score = 0
    incomplete.reverse()
    for i in incomplete:
        score = score * 5 + value_of_incomplete_bracket(i)
    return score


def score_incomplete_list(incomplete):
    score = []
    for i in incomplete:
        score.append(score_incomplete_line(i))
    score.sort()
    index_mid = int(len(score)/2)
    return score[index_mid]


def run():
    txt = read_file("input.txt")
    # txt = read_file("sample.txt")

    list_corrupted, list_incomplete = find_all_illegal(txt)

    answer_1 = score_corrupted(list_corrupted)
    print(f'AOC 2021-09-1: {answer_1}')

    answer_2 = score_incomplete_list(list_incomplete)
    print(f'AOC 2021-09-2: {answer_2}')


if __name__ == '__main__':
    run()
