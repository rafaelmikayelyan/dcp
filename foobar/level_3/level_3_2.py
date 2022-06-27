# You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in
# order to do so, you need to deploy special self-replicating bombs designed for you
# by the brightest scientists on Bunny Planet.
# There are two types: Mach bombs (M) and Facula bombs (F).
# The bombs, once released into the LAMBCHOP's inner workings will automatically
# deploy to all the strategic points you've identified and destroy them at the same time.

# But there's a few catches. First, the bombs self-replicate via one of two distinct
# processes:
# Every Mach bomb retrieves a syne unit from a Facula bomb;
# for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb

# For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce
# 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The
# replication process can be changed each cycle.

# Second, you need to ensure that you have exactly the right number of Mach and
# Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive.
# Too many, and you might overload the mass capacitors and create a singularity at
# the heart of the space station - not good!

# And finally, you were only able to smuggle one of each type of bomb - one Mach, one
# Facula - aboard the ship when you arrived, so that's all you have to start with.
# (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's
# not going to stop you from trying!)

# You need to know how many replication cycles (generations) it will take to generate
# the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F)
# where M and F are the number of Mach and Facula bombs needed. Return the fewest
# number of generations (as a string) that need to pass before you'll have the exact
# number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if
# this can't be done! M and F will be string representations of positive integers no
# larger than 10^50.
# For example, if M = "2" and F = "1" one generation would need to pass,
# so the solution would be "I". However, if M "2" and F "4" it would not be possible.


import unittest


def solution(x, y):
    x = convert_and_check_exp(x)
    y = convert_and_check_exp(y)
    gen = 0
    while x != 1 and y != 1:
        if (x % 2 == 0 and y % 2 == 0) or x % y == 0 or y % x == 0:
            return 'impossible'
        elif x > y:
            gen += int(x / y)
            x = x % y
        else:
            gen += int(y / x)
            y = y % x
    if x > y:
        gen += x - 1
    else:
        gen += y - 1
    return str(gen)


def convert_and_check_exp(string):
    exp = string.split('^')
    if len(exp) > 1:
        return int(exp[0]) ** int(exp[1])
    return int(string)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('4', '7'), '4', ' -> correct : 4')

    def test_2(self):
        self.assertEqual(solution('2', '1'), '1', ' -> correct : 1')

    def test_3(self):
        self.assertEqual(solution('2', '4'), 'impossible', ' -> correct : impossible')

    def test_4(self):
        self.assertEqual(solution('4', '4'), 'impossible', ' -> correct : impossible')

    def test_5(self):
        self.assertEqual(solution('1', '1'), '0', ' -> correct : 0')

    def test_6(self):
        self.assertEqual(solution('20050', '654777790'), 'impossible', ' -> correct : impossible')

    def test_7(self):
        self.assertEqual(solution('2100507', '654777790'), '397', ' -> correct : 397')

    def test_8(self):
        self.assertEqual(solution('10^5', '903'), '149', ' -> correct : 149')

    def test_9(self):
        self.assertEqual(solution('10^5', '902'), 'impossible', ' -> correct : impossible')

    def test_10(self):
        self.assertEqual(solution('10^5', '7'), '14289', ' -> correct : 14289')

    def test_11(self):
        self.assertEqual(solution('10^6', '1'), '999999', ' -> correct : 999999')

    def test_12(self):
        self.assertEqual(solution('10^6', '2'), 'impossible', ' -> correct : impossible')

    def test_13(self):
        self.assertEqual(solution('10', '3'), '5', ' -> correct : 5')


if __name__ == '__main__':
    unittest.main()
