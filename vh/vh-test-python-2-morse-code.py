from unittest import TestCase
from solution import possibilities
TestCase.maxDiff = None

class TestSampleTestCases(TestCase):
    def test_works_on_a_single_signal(self):
        "works on a single signal"
        self.assertEqual(possibilities("."), ["E"])
        self.assertEqual(possibilities(".-"), ["A"])

    def test_works_on_a_word_with_a_single_unknown_signal(self):
        "works on a word with a single unknown signal"
        self.assertEqual(possibilities("?"), ["E", "T"])
        self.assertEqual(possibilities("?."), ["I", "N"])
        self.assertEqual(possibilities(".?"), ["I", "A"])


from typing import List

class Node:
  def __init__(self, letter, dot=None,  dash=None):
    self.letter = letter
    self.dot = dot
    self.dash = dash
    

def possibilities(word: str) -> List[str]:
    morse_tree = Node('_')
    morse_tree.dot = Node('E')
    morse_tree.dash = Node('T')
    morse_tree.dot.dot = Node('I')
    morse_tree.dot.dash = Node('A')
    morse_tree.dash.dot = Node('N')
    morse_tree.dash.dash = Node('M')
    morse_tree.dot.dot.dot = Node('S')
    morse_tree.dot.dot.dash = Node('U')
    morse_tree.dot.dash.dot = Node('R')
    morse_tree.dot.dash.dash = Node('W')
    morse_tree.dash.dot.dot = Node('D')
    morse_tree.dash.dot.dash = Node('K')
    morse_tree.dash.dash.dot = Node('G')
    morse_tree.dash.dash.dash = Node('O')

    return decode(0, word, morse_tree)


def decode(signal_index: int, word: str, current_node: Node) -> List[str]:
    print('loop',signal_index, word, current_node.letter)
    if signal_index == len(word):
      return [current_node.letter]
    elif word[signal_index] == '.':
      return decode(signal_index + 1, word, current_node.dot)
    elif word[signal_index] == '-':
      return decode(signal_index + 1, word, current_node.dash)
    else:
      dot = decode(signal_index + 1, word, current_node.dot)
      dash = decode(signal_index + 1, word, current_node.dash)
      return dot + dash
