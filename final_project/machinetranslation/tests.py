import unittest

from translator import englishToFrench,frenchToEnglish
class Translatortest(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englishToFrench(''),'')
        self.assertEqual(englishToFrench(None), '')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish(''),'')
        self.assertEqual(frenchToEnglish(None),'')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    
if __name__ == '__main__':
   unittest.main()