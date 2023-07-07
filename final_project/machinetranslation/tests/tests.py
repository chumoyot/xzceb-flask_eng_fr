import unittest
from translator import english_to_french , french_to_english

class TestTranslation(unittest.TestCase):
  
    # Returns True or False. 
    def test_english_to_french(self):        
        self.assertEqual(english_to_french('hello'), 'bonjour')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
  
if __name__ == '__main__':
    unittest.main()