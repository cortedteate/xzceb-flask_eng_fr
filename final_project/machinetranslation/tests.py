import unittest
from translator import eng_2_fre, fre_2_eng

class TestE2F(unittest.TestCase): 
    def testoutput(self): 
        self.assertEqual(eng_2_fre('Hello'), 'Bonjour') # test when Hello is given as input the output is Bonjour.
    def testinput(self):     
        self.assertIsNone(eng_2_fre(None)) # test when input is null
class TestF2E(unittest.TestCase): 
    def testoutput(self): 
        self.assertEqual(fre_2_eng('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
    def testinput(self):     
        self.assertIsNone(fre_2_eng(None)) # test when input is null

unittest.main()