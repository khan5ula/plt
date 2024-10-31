class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"

        if self._starts_with_vowel():
            return self._handle_phrase_starting_vowel()

        if self._starts_with_single_consonant():
            return self._handle_phrase_starting_single_consonant()

    def _starts_with_vowel(self) -> bool:
        if self._phrase:
            # y is considered as consonant
            return self._phrase.lower()[0] in (
                "a",
                "e",
                "i",
                "o",
                "u",
            )

    def _ends_with_vowel(self) -> bool:
        if self._phrase:
            # y is considered as consonant
            return self._phrase.lower()[len(self._phrase) - 1] in (
                "a",
                "e",
                "i",
                "o",
                "u",
            )

    def _is_consonant(self, character) -> bool:
        return "bcdfghjklmnpqrstvwxz".find(character.lower()) > -1

    def _starts_with_single_consonant(self) -> bool:
        if self._phrase:
            if len(self._phrase) < 2 and self._is_consonant(self._phrase[0]):
                return True
            elif self._is_consonant(self._phrase[0]) and not self._is_consonant(
                self._phrase[1]
            ):
                return True
            return False

    def _handle_phrase_starting_vowel(self) -> str:
        if self._phrase:
            if self._phrase[len(self._phrase) - 1] == "y":
                return self._phrase + "nay"
            if self._ends_with_vowel():
                return self._phrase + "yay"
            else:
                return self._phrase + "ay"

    def _handle_phrase_starting_single_consonant(self) -> str:
        if self._phrase:
            if self._starts_with_single_consonant():
                return self._phrase[1:] + self._phrase[0] + "ay"
