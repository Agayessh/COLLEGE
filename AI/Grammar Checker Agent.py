# it can do majority stuff except for prepositions

# grammar checker agent (identifies grammar issues & improves user-submitted sentences)

import re

user_text = input("Enter a sentence: ")

# duplicates
def remove_duplicates(text):
      return re.sub(r'\b(\w+)\s+\1\b', r'\1', text, flags=re.IGNORECASE)


# capitalizations
def capitalize_sentence(text):
    if len(text) == 0:
        return text
    return text[0].upper() + text[1:]

# basic contractions
def fix_contractions(text):
    text = text.replace("won't", "will not")
    text = text.replace("can\'t", "can not")
    text = text.replace("n\'t", " not")
    text = text.replace("\'re", " are")

    corrections = {
        "i'm": "i am", "you're": "you are", "he's": "he is", "she's": "she is", "it's": "it is",
        "we're": "we are", "they're": "they are", "i've": "i have", "you've": "you have",
        "we've": "we have", "they've": "they have", "i'll": "i will", "you'll": "you will",
        "he'll": "he will", "she'll": "she will", "it'll": "it will", "we'll": "we will",
        "they'll": "they will", "isn't": "is not", "aren't": "are not", "wasn't": "was not",
        "weren't": "were not", "hasn't": "has not", "haven't": "have not", "hadn't": "had not",
        "doesn't": "does not", "don't": "do not", "didn't": "did not", "can't": "can not",
        "couldn't": "could not", "shouldn't": "should not", "wouldn't": "would not",
        "mustn't": "must not", "mightn't": "might not"
    }

    for wrong, right in corrections.items():
        text = text.replace(wrong, right)
        text = text.replace(wrong.capitalize(), right.capitalize())
    return text

# Fix simple subject-verb agreement
def fix_subject_verb(text):
    corrections = {
        "he dont": "he doesn't",
        "she dont": "she doesn't",
        "it dont": "it doesn't",
        "he doesnt": "he doesn't",
        "she doesnt": "she doesn't",
        "it doesnt": "it doesn't"
    }

    for wrong, right in corrections.items():
        # lowercase and capitalized versions
        text = text.replace(wrong, right)
        text = text.replace(wrong.capitalize(), right.capitalize())
    return text

# Add punctuation if missing
def add_punctuation(text):
    if len(text) == 0:
        return text
    if text[-1] not in ".!?":
        text += "."
    return text

def linking_verb(text):
  corrections = {
        "he are": "he is",
        "she are": "she is",
        "it are": "it is",
        "i are": "I am",
        "they is": "they are",
        "we is": "we are",
        "he were": "he was",
        "she were": "she was",
        "it were": "it was",
        "i were": "I was",
        "there was": "there were",
        "we was": "we were"
    }

  for wrong, right in corrections.items():
      text = text.replace(wrong, right)
      text = text.replace(wrong.capitalize(), right.capitalize())
  return text


def grammar_checker(text):
    text = capitalize_sentence(text)
    text = fix_contractions(text)
    text = fix_subject_verb(text)
    text = linking_verb(text)
    text = remove_duplicates(text)
    text = add_punctuation(text)
    return text

corrected_text = grammar_checker(user_text)
print("Corrected Sentence:", corrected_text)
