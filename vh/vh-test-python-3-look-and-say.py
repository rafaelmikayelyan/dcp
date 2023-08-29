def look_say(number: int) -> int:
    if number < 10:
      return 10 + number
    
    string = str(number)
    output = ''
    index = 0

    while index < len(string):
      digit = string[index]
      quantity = 0

      for i in range(index, len(string)):
        if string[i] == digit:
          quantity += 1
        else:
          break;
          
      index = index + quantity
    
      output += str(quantity) + digit
    
    return int(output)

import unittest
from solution import look_say

class TestSampleTests(unittest.TestCase):
    def test_should_work_on_sample_tests(self):
        self.assertEqual(look_say(0), 10)
        self.assertEqual(look_say(11), 21)
        self.assertEqual(look_say(12), 1112)

