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
