class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"

        if self._starts_with_vowel(self._phrase):
            return self._handle_phrase_starting_vowel(self._phrase)

    def _starts_with_vowel(self, phrase: str) -> bool:
        if phrase:
            return phrase.lower()[0] in ("a", "e", "i", "o", "u", "y")

    def _ends_with_vowel(self, phrase: str) -> bool:
        if phrase:
            return phrase.lower()[len(phrase) - 1] in ("a", "e", "i", "o", "u", "y")

    def _handle_phrase_starting_vowel(self, phrase: str) -> str:
        if phrase:
            if phrase[len(phrase) - 1] == "y":
                return phrase + "nay"
            if self._ends_with_vowel(phrase):
                return phrase + "yay"
            else:
                return phrase + "ay"
