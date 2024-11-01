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
        translator_any = PigLatin("any")
        translator_apple = PigLatin("apple")
        translator_ask = PigLatin("ask")

        self.assertEqual(translator_any.translate(), "anynay")
        self.assertEqual(translator_apple.translate(), "appleyay")
        self.assertEqual(translator_ask.translate(), "askay")

    def test_phrase_starting_with_single_consonant(self):
        translator = PigLatin("hello")
        self.assertEqual(translator.translate(), "ellohay")

    def test_phrase_starting_with_multiple_consonants(self):
        translator = PigLatin("known")
        self.assertEqual(translator.translate(), "ownknay")

    def test_phrase_with_multiple_words(self):
        translator = PigLatin("hello world")
        self.assertEqual(translator.translate(), "ellohay orldway")
        translator = PigLatin("well-being")
        self.assertEqual(translator.translate(), "ellway-eingbay")
