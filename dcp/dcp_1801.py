# DCP 1801
#
# Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions.
# If there are multiple solutions, return any of them.
# For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

import unittest


def dcp1801(string):
    open_par = 0
    i = 0
    while i < len(string):
        if string[i] == "(":
            open_par += 1
        if string[i] == ")":
            if open_par > 0:
                open_par -= 1
            else:
                string = string[:i] + "(" + string[i:]
                i += 1
        i += 1
    while open_par > 0:
        string += ")"
        open_par -= 1
    return string


class Test(unittest.TestCase):
    def test_o(self):
        self.assertEqual(dcp1801("("),"()" , "")

    def test_c(self):
        self.assertEqual(dcp1801(")"),"()" , "")

    def test_oc(self):
        self.assertEqual(dcp1801("()"),"()" , "")

    def test_oo(self):
        self.assertEqual(dcp1801("(("),"(())" , "")

    def test_cc(self):
        self.assertEqual(dcp1801("))"),"()()" , "")

    def test_ooc(self):
        self.assertEqual(dcp1801("(()"),"(())" , "")

    def test_ccoco(self):
        self.assertEqual(dcp1801("))()("),"()()()()" , "")


if __name__ == '__main__':
    unittest.main()
