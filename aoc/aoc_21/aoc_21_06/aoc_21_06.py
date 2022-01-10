def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def split_input(input):
    temp = []
    output = []
    temp = input[0].split()
    for i in temp[0].split(','):
        output.append(int(i))
    return output


def next_day(fish):
    i = 0
    newborn = []
    while i < len(fish):
        if fish[i] == 0:
            fish[i] = 6
            newborn.append(8)
        else:
            fish[i] -= 1
        i += 1
    if newborn:
        fish.extend(newborn)
    return fish


def population_after(days, raw):
    day = 0
    while day < days:
        print(day)
        next_day(raw)
        day += 1
    return raw


def run():
    # raw = read_file("input.txt")
    raw = [3,4,3,1,2] # Sample

    population = raw
    # population = split_input(raw)


    answer_1 = len(population_after(80, population))
    print(f'AOC 2021-05-1: {answer_1}')

    # answer_2 = len(population_after(256, population))
    # print(f'AOC 2021-05-2: {answer_2}')


if __name__ == '__main__':
    run()
