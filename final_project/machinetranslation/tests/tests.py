import unittest
import translator

class TranslationTextTest(unittest.TestCase):
    def test_null_value_en_fr(self):
        #Test the function for null values
        
        text1 = translator.english_to_french("test")
        text2 = ''
        message = "False means you entered and empty string"

        self.assertNotEqual(text1,text2,message)

    def test_common_value_en(self):
        #text a common example
        self.assertEqual(translator.english_to_french('Hello'), "Bonjour")
    
    def test_null_value_fr_en(self):
        #Test the function for null values
        text1 = translator.french_to_english("test")
        text2 = ''
        message = "False means you entered and empty string"

        self.assertNotEqual(text1,text2,message)

    def test_common_value_fr(self):
        #text a common example
        self.assertEqual(translator.french_to_english('Bonjour'), "Hello")

if __name__ == '__main__':
    unittest.main
