# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int num_rows);

# Example 1:

# Input: s = "PAYPALISHIRING", num_rows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", num_rows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", num_rows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= num_rows <= 1000


import unittest


def convert(s: str, num_rows: int) -> str:
    if len(s) <= 1:
        return s

    solution = ""
    row_jump = num_rows * 2 - 2

    for i in range(0, num_rows):
        counter = row_jump - 2 * i
        for j in range(i, len(s), row_jump):
            solution += s[j]
            if (i > 0) and (i < num_rows - 1) and (j + counter <= len(s)):
                solution += s[j + counter]

    return solution


class Test(unittest.TestCase):
    def test_00(self):
        self.assertEqual(convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_01(self):
        self.assertEqual(convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_02(self):
        self.assertEqual(convert("A", 1), "A")

    def test_03(self):
        self.assertEqual(convert("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG")


if __name__ == '__main__':
    unittest.main()
