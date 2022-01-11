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


# def next_day(fish):
#     i = 0
#     newborn = []
#     while i < len(fish):
#         if fish[i] == 0:
#             fish[i] = 6
#             newborn.append(8)
#         else:
#             fish[i] -= 1
#         i += 1
#     if newborn:
#         fish.extend(newborn)
#     return fish
#
#
# def population_after(days, raw):
#     day = 0
#     while day < days:
#         # print(day)
#         next_day(raw)
#         day += 1
#     return raw


def initialize_timer(population):
    timer = [0] * 9
    for fish in population:
        timer[fish] += 1
    return timer


def update_timer(timer, days):
    day = 0
    while day < days:
        timer = update_timer_once(timer)
        day += 1
    return timer


def update_timer_once(timer):
    trans_timer = [0] * 9
    cycle = 8
    while cycle > -1:
        if cycle == 0:
            trans_timer[6] += timer[0]
            trans_timer[8] = timer[0]
        else:
            trans_timer[cycle - 1] = timer[cycle]
        cycle -= 1
    return trans_timer


def count_population(population):
    count = 0
    for i in population:
        count += i
    return count

def run():
    population = split_input(read_file("input.txt"))
    # population = [3,4,3,1,2] # Sample
    DAY_80 = 80
    DAY_256 = 256

    timer = initialize_timer(population)

    answer_1 = count_population(update_timer(timer, DAY_80))
    print(f'AOC 2021-05-1: {answer_1}')

    answer_2 = count_population(update_timer(timer, DAY_256))
    print(f'AOC 2021-05-2: {answer_2}')


if __name__ == '__main__':
    run()
