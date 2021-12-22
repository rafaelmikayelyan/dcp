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
    if(isinstance(bits, list)):
        bits = convert_to_str(bits)
    return int(bits, 2)


def convert_to_str(bits):
    string = ''
    for i in bits:
        string += str(i)
    return string


def common_bit(bits, index, criteria):
    bit_sum = 0
    for row in bits:
        bit_sum += int(row[index])
    chosen_bit = abs(bit_average(bit_sum / len(bits)) + criteria)
    return str(chosen_bit)


def bit_average(ratio):
    if ratio < .5:
        return 0
    else:
        return 1


def searh_bit(bits, position, bit):
    result = []
    for row in bits:
        if row[position] == bit:
            result.append(row)
    return result


def life_support_rating(raw):
    oxygen = narrow_down_search(raw.copy(), 0)
    co2 = narrow_down_search(raw.copy(), -1)
    return oxygen, co2


def narrow_down_search(source, criteria):
    i = 0
    while len(source) != 1:
        source = eliminate_unpop(source, i, common_bit(source, i, criteria))
        i += 1
        if i == len(source[0]):
            break
    return source[0]


def eliminate_unpop(source, bit_position, pop_bit):
    i = 0
    while i < len(source):
        if source[i][bit_position] != pop_bit:
            source.pop(i)
            i -= 1
        i += 1
    return source



def run():
    raw = read_file("aoc_21_03_input.txt")

    rates = add_vertical_bits(raw)
    gamma = get_average_bits(raw, rates)
    epsilon = inverse_bits(gamma)

    answer_1 = convert_to_decimal(gamma) * convert_to_decimal(epsilon)
    print(f'AOC 2021-03-1: {answer_1}')

    oxygen, co2 = life_support_rating(raw)

    answer_2 = convert_to_decimal(oxygen) * convert_to_decimal(co2)
    print(f'AOC 2021-03-2: {answer_2}')


if __name__ == '__main__':
    run()
