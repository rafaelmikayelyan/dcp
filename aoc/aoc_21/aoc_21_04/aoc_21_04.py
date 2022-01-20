def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def extract_random(raw):
    random_numbers = []
    for string in raw.pop(0).split(','):
        random_numbers.append(int(string))
    return random_numbers


def extract_boards(raw):
    boards = []
    board = []

    for raw_row in raw:
        if len(raw_row) > 1:
            row = row_sting_to_int(raw_row.split(' '))
            board.append(row)
            if len(board) == 5:
                boards.append(board)
                board = []
    return boards


def row_sting_to_int(row):
    if len(row) > 5:
        index = 0
        while index < 5:
            if row[index] == '':
                row.pop(index)
                index -= 1
            index += 1
    row = [int(i) for i in row]
    return row


def check_board(board):
    sum_v = 0
    sum_h = 0

    for row in board:
        for i in row:
            sum_h = sum_h + i
        if sum_h == -5:
            return board
        sum_h = 0

    for i in range(len(board)):
        for row in board:
            sum_v = sum_v + row[i]
        if sum_v == -5:
            return board
        sum_v = 0


def calculate_score(board, number):
    sum_unmarked = 0
    for row in board:
        for i in row:
            if i != -1:
                sum_unmarked = sum_unmarked + i
    return sum_unmarked * number


def mark_numbers(randoms, boards, last_hand):
    board = 0
    row = 0
    number = 0
    last_board = []
    last_number = 0
    winners = []
    for random in randoms:
        while board < len(boards):
            if board not in winners:
                while row < len(boards[board]):
                    while number < len(boards[board][row]):
                        if boards[board][row][number] == random:
                            boards[board][row][number] = -1
                            winning_board = check_board(boards[board])
                            if winning_board:
                                if last_hand:
                                    winners.append(board)
                                    last_board = winning_board
                                    last_number = random
                                else:
                                    return winning_board, random
                        number += 1
                    number = 0
                    row += 1
            row = 0
            board += 1
        board = 0
    return last_board, last_number


def print_boards(boards):
    for board in boards:
        i = boards.index(board)
        print(f' - {i} ------------------- {i} - ')
        print_board(board)
        print()


def print_board(board):
    for row in board:
        print_row(row)


def print_row(row):
    output = ""
    for i in row:
        if i == -1:
            output += "  ."
        elif i < 10:
            output += "  " + str(i)
        else:
            output += " " + str(i)
    print(output)


def run():
    raw = read_file("aoc_21_04_input.txt")
    # raw = read_file("sample.txt")

    randoms = extract_random(raw)
    boards = extract_boards(raw)

    winning_board, last_number = mark_numbers(randoms, boards, False)

    answer_1 = calculate_score(winning_board, last_number)
    print(f'AOC 2021-04-1: {answer_1}')

    last_hand, last_number = mark_numbers(randoms, boards, True)

    answer_2 = calculate_score(last_hand, last_number)
    print(f'AOC 2021-04-2: {answer_2}')


if __name__ == '__main__':
    run()
