# PLT

_Pig Latin_ is a language game where English words are altered, according to some rules, to obtain their _Pig Latin_ translation. _PLT_ (_Pig Latin Translator_) is an API for translating a phrase from the English language into the _Pig Latin_ one.

You do not need to know more so far. The _User Stories_ section will provide further details.

## Instructions for You

- FORK this project and make sure your forked repository is PUBLIC. Then, IMPORT the forked project into PyCharm.
- If you BELONG to the GAI4-TDD group, you are asked to develop _PLT_ by following **TDD WITH** the support of **GAI4-TDD**. If you do NOT BELONG to the GAI4-TDD group, you are asked to develop _PLT_ by following **TDD WITHOUT** the support of **GAI4-TDD**.
- You DO NOT need to develop a GUI.
- You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods called by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
- You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
- You CANNOT use AI tools (if you are in the GAI4-TDD group, you can use GAI4-TDD of course).
- You CANNOT interact with your colleagues. Work alone and do your best!
- The _PLT_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _User Stories_ section).
- You should be able to incrementally develop _PLT_ without an upfront comprehension of all its requirements. DO NOT read ahead and handle the requirements (specified in the user stories) one at a time in the provided order. Develop _PLT_ by starting from the first story's requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
- Each time you end a GREEN or REFACTOR phase, COMMIT.
- At the end of the task, PUSH your forked project and fill in the following post-questionnaire: <https://forms.gle/6vc5a3miF1oZmHKQ7>.

## API Usage

Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because more details will be given later in the _User Stories_ section. A typical API usage follows.

```python
# Initialize a translator with a phrase
translator = PigLatinTranslator.PigLatinTranslator("This is a phrase")
# Get the phrase
phrase = translator.get_phrase()
# Get the Pig Latin translation
translation = translator.translate()
```

See the provided source files to improve your understanding of the API before starting to implement the user stories.

## User Stories

Remember to read and implement the user stories once at a time (in the provided order). Therefore, do not read the next user story, if the current one is not implemented yet.

### User Story 1 -- Input Phrase

A translator (from English to Pig Latin) takes a phrase as the input. The phrase is represented as a string where words are separated by white spaces.

**Requirement:**

- Implement `PigLatinTranslator.PigLatinTranslator(self, phrase: str)` to create a translator that takes a phrase as the input.
- Implement `PigLatinTranslator.get_phrase(self) -> str` to let anyone get the input phrase from the translator.

**Example:**

- The translator takes as the input the phrase “hello world”. Anyone gets the input phrase: “hello world”.

### User Story 2 -- Translating an Empty Phrase

The translator translates an input phrase into _Pig Latin_. The input phrase can be an empty string. When this happens, the result of the translation is “nil”.

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate an empty string.

**Example:**

- The translation of an empty string is “nil”.

### User Story 3 -- Translating a Word Starting with a Vowel

The input phrase can be a single word starting with a vowel. In that case, the translator applies to following translation rules:

- If the word ends with "y", append “nay” to the and of the word.
- If the word ends with a vowel, append “yay” to the and of the word.
- If the word ends with a consonant, append “ay” to the and of the word.

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a word starting with a vowel.

**Examples:**

- The translation of “any” is “anynay”.
- The translation of “apple” is “appleyay”.
- The translation of “ask” is “askay”.

### User Story #4 -- Translating a Word Starting with a Single Consonant

The input phrase can be a single word starting with a single consonant (note that the "y" letter is considered a consonant). In that case, the translator applies the following translation rule:

- Remove the consonant from the beginning of the word and add it to the end of the word. Finally, append “ay” to the end of the resulting word.

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a word starting with a single consonant.

**Example:**

- The translation of “hello” is “ellohay”.

### User Story #5 -- Translating a Word Starting with More Consonants

The input phrase can be a single word starting with more consonants. In that case, the translator applies the following translation rule:

- Remove the consonants from the beginning of the word and add them to the end of the word. Finally, append “ay” to the end of the resulting word.

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a word starting with more consonants.

**Example:**

- The translation of “known” is “ownknay”.

### User Story #6 -- Translating a Phrase Containing More Words

The input phrase can contain more words (separated by white spaces). In that case, the translator applies the translation rules (reported in User Stories 3-5) to the single words. Moreover, for composite words (those separated by a “-”), the translation rules apply to the single words.

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a phrase containing more words, as well as composite words.

**Examples:**

- The translation of “hello world” is “ellohay orldway”.
- The translation of “well-being” is “ellway-eingbay”.

### User Story #7 -- Translating a Phrase Containing Punctuations

The input phrase can contain punctuation marks. In that case, the translator applies the translation rules to the single and composite words while preserving the punctuation marks. Only the following punctuation marks are allowed: point, comma, semi-colon, colon, apostrophe, question mark, exclamation mark, and round parenthesis.

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a phrase containing the allowed punctuation marks. For punctuation marks not allowed, raise a `PigLatinError`.

**Example:**

- The translation of “hello world!” is “ellohay orldway!”.

### User Story #8 -- Translating a Phrase with Upper- and Title-case Words

The input phrase can contain upper- and title-case words. In those cases, the translator applies the translation rules to the single and composite words while preserving the upper- and title-cases. Cases different from upper- and title-cases are not allowed (e.g., “biRd”).

**Requirement:**

- Implement `PigLatinTranslator.translate(self) -> str` to let the translator translate a phrase containing upper- and title-case words. For cases different from upper- and title-cases, raise a `PigLatinError`.

**Example:**

- The translation of “APPLE” (upper case) is “APPLEYAY”. The translation of “Hello” (title case) is “Ellohay”.
