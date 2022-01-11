def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return split_input(data)


def split_input(input):
    output = []
    for i in input[0].split()[0].split(','):
        output.append(int(i))
    return output


def cheap_alignment(positions, crab_eng):
    position = [0] * max(positions)
    i = 0
    while i < len(position):
        for x in positions:
            dif = abs(i - x)
            if crab_eng:
                counter = 0
                while counter < dif:
                    counter += 1
                    position[i] += counter
            else:
                position[i] += dif
        i += 1
    return min(position)


def run():
    positions = read_file("input.txt")
    # positions = [16,1,2,0,4,2,7,1,2,14] # Sample

    answer_1 = cheap_alignment(positions, False)
    print(f'AOC 2021-05-1: {answer_1}')

    answer_2 = cheap_alignment(positions, True)
    print(f'AOC 2021-05-2: {answer_2}')


if __name__ == '__main__':
    run()
