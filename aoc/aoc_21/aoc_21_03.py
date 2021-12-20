def read_file(input):
    file = open(input, "r")
    data = file.read().splitlines()
    file.close()
    return data


def add_vertical_bits(data):
    bits_sum = [0] * len(data[0])
    index = 0
    for row in data:
        for bit in row:
            bits_sum[index] += int(bit)
            index += 1
        index = 0
    return bits_sum


def get_average_bits(data, bits_sum):
    data_size = len(data)
    bits = []
    for i in bits_sum:
        if (i / data_size) < 0.5:
            bits.append(0)
        else:
            bits.append(1)
    return bits


def inverse_bits(bits):
    inverse = []
    for bit in bits:
        if bit == 0:
            inverse.append(1)
        else:
            inverse.append(0)
    return inverse


def convert_to_decimal(bits):
    binary = 0
    for i in bits:
        binary = binary * 10 + i
    binary = str(binary)
    return int(binary, 2)


def multiply_g_e(gamma, epsilon):
    return convert_to_decimal(gamma) * convert_to_decimal(epsilon)


def run():
    raw = read_file("aoc_21_03_input.txt")
    rates = add_vertical_bits(raw)
    gamma = get_average_bits(raw, rates)
    epsilon = inverse_bits(gamma)
    answer_1 = multiply_g_e(gamma, epsilon)
    print(f'AOC 2021-03-1: {answer_1}')
    answer_2 = True
    print(f'AOC 2021-03-2: {answer_2}')


if __name__ == '__main__':
    run()
