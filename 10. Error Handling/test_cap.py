# Just for reference, capitalize only does this for the first word
# Title capitalizes every word

import unittest
import cap
  # this imports the cap.py file we just created

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()