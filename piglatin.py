class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"
