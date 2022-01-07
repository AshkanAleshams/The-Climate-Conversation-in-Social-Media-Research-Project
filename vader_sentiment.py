import codecs
from inspect import getsourcefile
import os
from typing import List, Dict, Tuple


PUNCTUATION = '!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'


def report_sentiment(tweet_text: str) -> Tuple[str, float]:
    """Return the VADER sentiment of the review in text.

    The VADER sentiment is a tuple of the polarity, intensity of the review.
    """

    # Read vader_lexicon and get the word to intensity dictionary
    lex_dict = read_vader_lexicon_file("csc_project/vader_lexicon.txt")

    # First clean the review text and split into a list of words.
    word_list = clean_text(tweet_text)

    # Extract the number of times each VADER keyword appears in the review.
    occurrences = count_keywords(word_list, lex_dict)

    # Calculate the average intensity of the keywords in the review.
    average_intensity = calculate_average_intensity(occurrences, lex_dict)

    if average_intensity >= 0.05:
        return ('positive', average_intensity)
    elif average_intensity <= -0.05:
        return ('negative', average_intensity)
    else:
        return ('neutral', average_intensity)


def read_vader_lexicon_file(lexicon_file: str):
    _this_module_file_path_ = os.path.abspath(getsourcefile(lambda: 0))
    lexicon_full_filepath = os.path.join(os.path.dirname(_this_module_file_path_), lexicon_file)
    with codecs.open(lexicon_full_filepath, encoding='utf-8') as f:
        lexicon_full_filepath = f.read()

    lex_dict = {}
    for line in lexicon_full_filepath.rstrip('\n').split('\n'):
        if not line:
            continue
        (word, measure) = line.strip().split('   ')[0:4]
        lex_dict[word] = float(measure)
    return lex_dict


def clean_text(text: str) -> List[str]:
    """Return text as a list of words that have been cleaned up.

    Cleaning up involves:
        - removing punctuation
        - converting all letters to lowercase (because our VADER keywords
          are all written as lowercase)
    """
    # Remove punctuation from text
    for p in PUNCTUATION:
        text = str.replace(text, p, ' ')

    # Convert text to lowercase
    text = str.lower(text)

    # Split text into words and return
    return str.split(text)


def count_keywords(word_list: List[str], lex_dict: dict) -> Dict[str, int]:
    """Return a frequency mapping of the VADER keywords in text.
    """
    # ACCUMULATOR: A mapping of keyword frequencies seen so far
    occurrences_so_far = {}

    for word in word_list:
        if word in lex_dict:
            if word in occurrences_so_far:
                occurrences_so_far[word] = occurrences_so_far[word] + 1
            else:
                occurrences_so_far[word] = 0
                occurrences_so_far[word] = occurrences_so_far[word] + 1

    return occurrences_so_far


def calculate_average_intensity(occurrences: Dict[str, int], lex_dict: dict) -> float:
    """Return the average intensity of the given keyword occurrences.

    Preconditions:
        - occurrences != {}
        - all({occurrences[keyword] >= 1 for keyword in occurrences})
    """
    num_keywords = sum([occurrences[word] for word in occurrences])
    total_intensity = sum([lex_dict[word] * occurrences[word]
                           for word in occurrences])
    return total_intensity / num_keywords
