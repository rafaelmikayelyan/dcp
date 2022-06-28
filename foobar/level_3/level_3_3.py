# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly. 

# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

# The fuel control mechanisms have three operations: 

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

import unittest


def solution(n: str) -> int:
    n = int(n)
    step = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        elif (n - 1) / 2 == 1:
            n -= 1
        elif (n + 1) / 2 == 1:
            n += 1
        elif (n - 1) / 2 % 2 == 0:
            n -= 1
        elif (n + 1) / 2 % 2 == 0:
            n += 1
        step +=1
    return step


class Test(unittest.TestCase):
    def test_0(self):
        self.assertEqual(solution('1'), 0)

    def test_1(self):
        self.assertEqual(solution('4'), 2)

    def test_2(self):
        self.assertEqual(solution('15'), 5)

    def test_3(self):
        self.assertEqual(solution('10'), 4)

    def test_4(self):
        self.assertEqual(solution('13'), 5)


if __name__ == '__main__':
    unittest.main()
