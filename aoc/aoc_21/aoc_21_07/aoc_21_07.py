def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    # print(data)
    file.close()
    return data


def split_input(input):
    output = []
    for i in input[0].split()[0].split(','):
        output.append(int(i))
    return output


def run():
    # population = split_input(read_file("input.txt"))
    population = [16,1,2,0,4,2,7,1,2,14] # Sample
    print(population)

    answer_1 = False
    print(f'AOC 2021-05-1: {answer_1}')

    answer_2 = False
    print(f'AOC 2021-05-2: {answer_2}')


if __name__ == '__main__':
    run()
