def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def row_to_int(row):
    if len(row) > 5:
        index = 0
        while index < 5:
            if row[index] == '':
                row.pop(index)
                index -= 1
            index += 1
    row = [int(i) for i in row]
    return row


def check_boards(score_boards):
    answer = []
    for score in score_boards:
        answer = check_board(score)
    return answer


def check_board(board):
    sum_v = 0
    sum_h = 0

    for row in board:
        for i in row:
            sum_h = sum_h + i
        if sum_h == 5:
            return board
        sum_h = 0

    for i in range(len(board)):
        for row in board:
            sum_v = sum_v + row[i]
        if sum_v == 5:
            return board
        sum_v = 0


def extract_random(raw):
    random_numbers = []
    for string in raw.pop(0).split(','):
        random_numbers.append(int(string))
    return random_numbers


def extract_boards(raw):
    boards = []
    score_boards = []
    board = []
    score_board = []
    row = []
    score_row = []

    for raw_row in raw:
        if len(raw_row) > 1:
            row = row_to_int(raw_row.split(' '))
            score_row = [0] * len(row)
            board.append(row)
            score_board.append(score_row)
            if len(board) == 5:
                boards.append(board)
                board = []
                score_boards.append(score_board)
                score_board = []
    return boards, score_boards


def calculate_score(board, score, number):
    sum_unmarked = 0
    for row in score:
        i = 0
        while i < 5:
            if row[i] == 0:
                sum_unmarked = sum_unmarked + board[score.index(row)][i]
            i = i + 1
    return sum_unmarked * number


def run():
    raw = read_file("aoc_21_04_input.txt")
    # raw = read_file("sample.txt")
    random_numbers = extract_random(raw)
    boards, scores = extract_boards(raw)

    winning_board = []
    for random in random_numbers:
        for board in boards:
            for row in board:
                for number in row:
                    if number == random:
                        scores[boards.index(board)][board.index(row)][row.index(number)] = 1
                        winning_board = check_boards(scores)
                        if winning_board:
                            break
                    if winning_board:
                        break
                if winning_board:
                    break
            if winning_board:
                break
        if winning_board:
            break

    answer_1 = calculate_score(boards[scores.index(winning_board)],winning_board, random)
    print(f'AOC 2021-04-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-04-2: {answer_2}')


if __name__ == '__main__':
    run()
