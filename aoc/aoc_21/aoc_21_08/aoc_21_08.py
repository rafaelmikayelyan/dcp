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
    decoded_number = ''
    digits = [''] * 10
    positions = [''] * 7
    zero_six_nine = []
    two_three_five = []
    for strings in txt:
        for s in strings.split(' '):
            if len(s) == 2:
                digits[1] = list(s)
            elif len(s) == 4:
                digits[4] = list(s)
            elif len(s) == 3:
                digits[7] = list(s)
            elif len(s) == 7:
                digits[8] = list(s)
            elif len(s) == 6:
                zero_six_nine.append(list(s))
            elif len(s) == 5:
                two_three_five.append(list(s))
            else:
                print(f'ERROR !!! unknown len(s) of {s} !!!')

    #p0, p1, p3
    positions[0] = list(set(digits[1]).symmetric_difference(set(digits[7])))[0]
    positions[1] = positions[3] = list(set(digits[1]).symmetric_difference(set(digits[4])))
    #5, p1
    for letter in two_three_five:
        if positions[1][0] in letter and positions[1][1] in letter:
            digits[5] = letter
            break
    #p5, p2
    for letter in digits[1]:
        if letter in digits[5]:
            positions[5] = letter
        else:
            positions[2] = letter
    #6, p4
    for letter in zero_six_nine:
        if (set(digits[8]).symmetric_difference(set(letter))) == set(positions[2]):
            digits[6] = letter
    positions[4] = list(set(digits[5]).symmetric_difference(set(digits[6])))[0]
    #9
    for letter in zero_six_nine:
        if (set(digits[8]).symmetric_difference(set(letter))) == set(positions[4]):
            digits[9] = letter
    #0, p3, p1
    for letter in zero_six_nine:
        for p in positions[1]:
            if (set(digits[8]).symmetric_difference(set(letter))) == set(p):
                digits[0] = letter
                positions[3] = p
                positions[1].remove(p)
                positions[1] = positions[1][0]
    #p6
    for letter in digits[8]:
        if letter not in positions:
            positions[6] = letter
    #2, 3
    for letter in two_three_five:
        if set(letter).symmetric_difference(set(positions)) == {positions[1], positions[5]}:
            digits[2] = letter
        elif set(letter).symmetric_difference(set(positions)) == {positions[1], positions[4]}:
            digits[3] = letter

    for output in txt[1].split(' '):
        for digit in digits:
            if set(output).symmetric_difference(set(digit)) == set():
                decoded_number = decoded_number + str(digits.index(digit))

    return int(decoded_number)


def print_digit(p):
    for side in p:
        if p[p.index(side)] == '':
            p[p.index(side)] = ' '
    digit = [f' {p[0] * 4} ',
             f'{p[1]}    {p[2]}',
             f'{p[1]}    {p[2]}',
             f' {p[3] * 4} ',
             f'{p[4]}    {p[5]}',
             f'{p[4]}    {p[5]}',
             f' {p[6] * 4} ']
    for line in digit:
        print(line)


def print_digit_list(digits):
    i = 0
    for digit in digits:
        print(f' {i} - {digit}')
        i += 1


def add_all_outputs(source):
    outputs = []
    for line in source:
        outputs.append(decode_line(line))
    return sum(outputs)


def run():
    txt = read_file("input.txt")
    # txt = read_file("sample.txt")
    # txt = [['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']]

    answer_1 = count_occurrences(txt)
    print(f'AOC 2021-08-1: {answer_1}')

    answer_2 = add_all_outputs(txt)
    print(f'AOC 2021-08-2: {answer_2}')


if __name__ == '__main__':
    run()
