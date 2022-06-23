import unittest


def solution(xs):
    if xs == 1:
        return xs.pop()
    return max_output(xs)


def max_output(nums):
    hasPositive = False
    hasZero = False
    max_output = 1
    negatives = []
    for x in nums:
        if x > 0:
            hasPositive = True
            max_output *= x
        elif x < 0:
            negatives.append(x)
        else:
            hasZero = True
    negatives = max_negatives(negatives)
    if hasPositive:
        if negatives > 0:
            max_output *= negatives
        return max_output 
    elif hasZero:
        if negatives > 0:
            return negatives
        else:
            return 0 

    else:
        return negatives


def max_negatives(negatives):
    if len(negatives) == 0:
        return 0
    elif len(negatives) < 2:
        return negatives.pop()

    elif len(negatives) % 2 == 1:
        negatives.remove(max(negatives))

    product = 1
    for x in negatives:
        product *= x

    return product



class Test(unittest.TestCase):
    def test_single_negative(self):
        self.assertEqual(solution([-1]), -1, ' -> correct : -1')

    def test_single(self):
        self.assertEqual(solution([1]), 1, ' -> correct : 1')

    def test_single_zero(self):
        self.assertEqual(solution([0]), 0, ' -> correct : 0')

    def test_double_zero(self):
        self.assertEqual(solution([0, 0]), 0, ' -> correct : 0')

    def test_zero_positive(self):
        self.assertEqual(solution([0, 1]), 1, ' -> correct : 1')

    def test_zero_negative(self):
        self.assertEqual(solution([0, -1]), 0, ' -> correct : 0')

    def test_zero(self):
        self.assertEqual(solution([2, 0, 2, 2, 0]), 8, ' -> correct : 8')

    def test_negative(self):
        self.assertEqual(solution([-2, -3, 4, -5]), 60, ' -> correct : 60')
    
    def test_random(self):
        self.assertEqual(solution([2,-3,1,0,-5]), 30, ' -> correct : 30')

if __name__ == '__main__':
    unittest.main()
