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

        self.assertEqual(translator_nay.translate(), "yaynay")
        self.assertEqual(translator_yaa.translate(), "yaayay")
        self.assertEqual(translator_yan.translate(), "yanay")

        translator_any = PigLatin("any")
        translator_apple = PigLatin("apple")
        translator_ask = PigLatin("ask")

        self.assertEqual(translator_any.translate(), "anynay")
        self.assertEqual(translator_apple.translate(), "appleyay")
        self.assertEqual(translator_ask.translate(), "askay")
