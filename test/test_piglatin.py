import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):
    def test_get_phrase(self):
        translator = PigLatin("phrase")
        self.assertEqual("phrase", translator.get_phrase())

    def test_translate_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_phrase_starting_with_vowel(self):
        translator_nay = PigLatin("yay")
        translator_yaa = PigLatin("yaa")
        translator_yan = PigLatin("yan")

        print(translator_nay.translate())
        print(translator_yaa.translate())
        print(translator_yan.translate())
        self.assertEqual(translator_nay.translate(), "yaynay")
        self.assertEqual(translator_yaa.translate(), "yaayay")
        self.assertEqual(translator_yan.translate(), "yanay")
