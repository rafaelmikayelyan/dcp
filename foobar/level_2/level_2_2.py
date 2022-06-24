import unittest


def solution(s: str) -> int:
    salutes = 0
    left = 0
    for i in s:
        if i == '>':
            left += 1
        elif i == '<':
            salutes += left
    return salutes * 2


class Test(unittest.TestCase):
    def test_0(self):
        self.assertEqual(solution(">"), 0, ' -> correct : 0')

    def test_0_long(self):
        self.assertEqual(solution(">->"), 0, ' -> correct : 0')

    def test_10(self):
        self.assertEqual(solution("--->-><-><-->-"), 10, ' -> correct : 10')

    def test_2_short(self):
        self.assertEqual(solution("><"), 2, ' -> correct : 2')

    def test_2(self):
        self.assertEqual(solution(">----<"), 2, ' -> correct : 2')

    def test_4(self):
        self.assertEqual(solution("<<>><"), 4, ' -> correct : 4')


if __name__ == '__main__':
    unittest.main()
