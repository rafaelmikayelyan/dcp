# Write a function solution(l) that takes a list of positive integers l and counts the number
# of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.
# The length of l is between 2 and 2000 inclusive.
# The elements of l are between 1 and 999999 inclusive.
# The solution fits within a signed 32-bit integer. Some of the lists are purposely generated
# without any access codes to throw off spies, so if no triples are found, return 0. 

# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

import random
import unittest


def solution(l: list[int]) -> int:
    triples = 0
    step = len(l)
    for i in range(0, step - 2):
        for j in range(i + 1, step - 1):
            if l[j] % l[i] == 0:
                for k in range(j + 1, step):
                    if l[k] % l[j] == 0:
                        triples += 1
    return triples


class Test(unittest.TestCase):
    def test_00(self):
        self.assertEqual(solution([1]), 0, ' -> correct : 0')

    def test_0_short(self):
        self.assertEqual(solution([1, 1]), 0, ' -> correct : 0')

    def test_0(self):
        self.assertEqual(solution([1, 3, 2, 1]), 0, ' -> correct : 0')

    def test_1(self):
        self.assertEqual(solution([1, 1, 1]), 1, ' -> correct : 1')

    def test_3(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3, ' -> correct : 3')

    def test_5(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 86, 357]), 5, ' -> correct : 5')

    def test_9(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 86, 357, 2000]), 9, ' -> correct : 9')

    def test_x(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 86, 357, 2000, 70, 3, 2]), 13, ' -> correct : 13')

    def test_z(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 86, 357, 2000, 70, 3, 2, 2, 1]), 16, ' -> correct : 13')

    def test_none(self):
        self.assertEqual(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0, ' -> correct : 0')


if __name__ == '__main__':
    unittest.main()
