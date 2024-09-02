# DCP 1802
#
# Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

import unittest


def dcp1802(words):
    combo = []
    for word_a in range(len(words) - 1):
        for word_b in range(word_a + 1, len(words)):
            if is_palindrome(words[word_a] + words[word_b]):
                combo.append((word_a, word_b))
            if is_palindrome(words[word_b] + words[word_a]):
                combo.append((word_b, word_a))
    return combo


def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True


class Test(unittest.TestCase):
    def test_pass_4_4(self):
        self.assertEqual(dcp1802(["code", "edoc", "da", "d"]), [(0, 1), (1, 0), (2, 3)], "")

    def test_fail_4_0(self):
        self.assertEqual(dcp1802(["code", "edockn", "dap", "d"]), [], "")

    def test_fail_5_0(self):
        self.assertEqual(dcp1802(["a", "b", "c", "d", "ef"]), [], "")


if __name__ == '__main__':
    unittest.main()
