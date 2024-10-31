class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"
        if len(self._phrase.split()) < 2 or len(self._phrase.split("-")):
            return self._translate_phrase(self._phrase)
        else:
            resulting_phrases = []
            if " " in self._phrase:
                for phrase in self._phrase.split(" "):
                    resulting_phrases.append(self._translate_phrase(phrase))
                return " ".join(resulting_phrases)
            elif "-" in self._phrase:
                for phrase in self._phrase.split("-"):
                    resulting_phrases.append(self._translate_phrase(phrase))
                return "-".join(resulting_phrases)

    def _translate_phrase(self, phrase: str) -> str:
        if self._starts_with_vowel(phrase):
            return self._handle_phrase_starting_vowel(phrase)

        if self._starts_with_single_consonant(phrase):
            return self._handle_phrase_starting_single_consonant(phrase)

        if self._starts_with_multiple_consonant(phrase):
            return self._handle_phrase_starting_multiple_consonant(phrase)

    def _starts_with_vowel(self, phrase: str) -> bool:
        if phrase:
            # y is considered as consonant
            return phrase.lower()[0] in (
                "a",
                "e",
                "i",
                "o",
                "u",
            )

    def _ends_with_vowel(self, phrase) -> bool:
        if phrase:
            # y is considered as consonant
            return phrase.lower()[len(phrase) - 1] in (
                "a",
                "e",
                "i",
                "o",
                "u",
            )

    def _is_consonant(self, character) -> bool:
        return "bcdfghjklmnpqrstvwxz".find(character.lower()) > -1

    def _starts_with_single_consonant(self, phrase) -> bool:
        if phrase:
            if len(phrase) < 2 and self._is_consonant(phrase[0]):
                return True
            elif self._is_consonant(phrase[0]) and not self._is_consonant(phrase[1]):
                return True
            return False

    def _handle_phrase_starting_vowel(self, phrase) -> str:
        if phrase:
            if phrase[len(phrase) - 1] == "y":
                return phrase + "nay"
            if self._ends_with_vowel(phrase):
                return phrase + "yay"
            else:
                return phrase + "ay"

    def _handle_phrase_starting_single_consonant(self, phrase) -> str:
        if phrase:
            if self._starts_with_single_consonant(phrase):
                return phrase[1:] + phrase[0] + "ay"

    def _starts_with_multiple_consonant(self, phrase):
        if self._phrase:
            if len(phrase) < 2:
                return False
            if self._is_consonant(phrase[0]) and self._is_consonant(phrase[1]):
                return True

    def _handle_phrase_starting_multiple_consonant(self, phrase):
        if phrase:
            consonants = []
            first_vowel = -1
            for character in phrase:
                if self._is_consonant(character):
                    consonants.append(character)
                    first_vowel += 1
                else:
                    break
            first_vowel += 1
            if first_vowel < len(phrase):
                return phrase[first_vowel:] + "".join(consonants) + "ay"


# The input phrase can contain more phrases (separated by white spaces). In that case, the translator applies the translation rules (reported in User Stories 3-5) to the single phrases. Moreover, for composite phrases (those separated by a “-”), the translation rules apply to the single phrases.
#
# **Requirement:**
#
# - Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a phrase containing more phrases, as well as composite phrases.
#
# **Examples:**
#
# - The translation of “hello world” is “ellohay orldway”.
# - The translation of “well-being” is “ellway-eingbay”.
