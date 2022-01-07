"""
CSC110 Fall 2020 Project 1, Part 1 Open Json File

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the professors and TAs
in CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110 project,
please consult with us.

This file is Copyright (c) 2020 Jiajin Wu, Ehsan Emadi, Ashkan Aleshams and Michael Galloro.
"""

from typing import List, Dict

# large set of stopwords and other words we want to remove from our raw twitter data
import stopwords_and_redundancies

# from other files we wrote
import reading_data


# main functions
def accumulate_tweet_words(tweets: List[reading_data.Tweet]) -> Dict[str, int]:
    """
    Returns a dict with words in tweets as keys and how often they appear as values.
    """
    # tweet word accumulator
    tweet_words_so_far = {}

    for twit in tweets:
        tweet = clean_words(twit.tweet)  # cleans the words that we don't want

        for word in tweet:
            # adds a key:value pair to tweet_words_so_far if the key does not exist
            if word not in tweet_words_so_far:
                tweet_words_so_far[word] = 1
            # increases tweet word value by one if the key already exist
            else:
                tweet_words_so_far[word] += 1

    return tweet_words_so_far


def accumulate_locations(tweets: List[reading_data.Tweet]) -> Dict[str, int]:
    """
    Returns a dict with twitter user locations as keys and how often they appear as values.
    """
    # location accumulator
    locations_so_far = {}

    for tweet in tweets:
        # removes the words that we don't want from user location
        # description
        locations = clean_locations(clean_words(tweet.user.location))

        for location in locations:
            # adds a key:value pair to locations_so_far if the key does not exist
            if location not in locations_so_far:
                locations_so_far[location] = 1
            # increases location value by one if the key already exist
            else:
                locations_so_far[location] += 1

    return locations_so_far


def accumulate_descriptions(tweets: List[reading_data.Tweet]) -> Dict[str, int]:
    """
    Returns a dict with twitter user descriptions as keys and how often they appear as values.
    """
    # description accumulator
    descriptions_so_far = {}

    for tweet in tweets:
        # removes words in user descriptions that we don't want
        description = clean_words(tweet.user.description)

        for word in description:
            if len(word) >= 4:  # so we don't have meaningless descriptions
                # adds a key:value pair to descriptions_so_far if the key
                # does not exist
                if word not in descriptions_so_far:
                    descriptions_so_far[word] = 1
                # increases description word value by one if the key already exists
                else:
                    descriptions_so_far[word] += 1

    return descriptions_so_far


def accumulate_hashtags(tweets: List[reading_data.Tweet]) -> Dict[str, int]:
    """
    Returns a dict with twitter hashtags as keys and how often they appear as values.
    """
    # hashtag accumulator
    hashtags_so_far = {}

    for tweet in tweets:
        hashtags = tweet.hashtags

        for hashtag in hashtags:
            # adds a key:value pair to hashtags_so_far if the key does not exist
            if hashtag not in hashtags_so_far:
                hashtags_so_far[hashtag] = 1
            # increase hashtag value by one if the key already exists
            else:
                hashtags_so_far[hashtag] += 1

    return hashtags_so_far


def get_max_tweet_words(tweets: List[reading_data.Tweet], number_of_words_wanted: int) -> Dict[str, int]:
    """
    Returns the most common tweet words in a dict with the length of number_of_words_wanted.
    """
    tweet_words = accumulate_tweet_words(tweets)
    # change the value into a list
    list_of_values = list(tweet_words.values())
    # change the keys into a list.
    list_of_keys = list(tweet_words.keys())

    x = number_of_words_wanted

    # pairs with max values accumulator
    max_pairs_so_far = {}

    while x > 0:
        # finds the max value in the list of values
        maximum = max(list_of_values)
        # uses the index of the max value to acquire a key pair with that value
        corresponding_key = list_of_keys[list_of_values.index(maximum)]
        # puts the pair into the accumulator
        max_pairs_so_far[corresponding_key] = maximum

        list_of_keys.remove(corresponding_key)
        list_of_values.remove(maximum)
        # to ensure while loop runs the desired number of times
        x -= 1

    return max_pairs_so_far


# Helper functions
def clean_locations(locations: List[str]) -> List[str]:
    """
    Return a list of unified location terms, and removes many common user location-related
    redundancies, such as calling the same place by a different name, or common non-locations such as
    "city".

    >>> clean_locations(['city', 'as', 'usa', 'ny', 'new', 'york', 'the', 'states'])
    ['usa', 'new york', 'new york', 'usa']
    """
    for i in range(0, len(locations)):
        # so meaningless words won't show up as locations
        if len(locations[i]) < 4 and locations[i] != 'uk' and locations[i] != 'usa' and \
                locations[i] != 'ny':
            locations[i] = ''
        # so meaningless locations won't show up
        elif locations[i] in stopwords_and_redundancies.LOCATION_REDUNDANCIES:
            locations[i] = ''
        # unify the names of the USA
        elif locations[i] == 'states' or locations[i] == 'america':
            locations[i] = 'usa'
        # unify the names of the UK
        elif locations[i] == 'kingdom':
            locations[i] = 'uk'
        # unify the names of New York
        elif locations[i] == 'york' or locations[i] == 'ny':
            locations[i] = 'new york'
    # remove the empty strings
    while '' in locations:
        locations.remove('')

    return locations


def clean_words(words: str) -> List[str]:
    """
    Return a list of strings that is a list of each word in the input words.
    The function also removes words that are considered stopwords.
    Each of these returned words are all lower case and only
    contain alphanumeric characters.

    >>> clean_words('a global war$ming')
    ['warming']
    """
    string_so_far = ''
    string_lower = words.lower()  # make the words lower cased

    for character in string_lower:
        # ignores characters that are not spaces or alphanumeric.
        if character.isalpha() or character == ' ':
            string_so_far = string_so_far + character
    # split the string into lists
    list_of_words = string_so_far.split(' ')

    non_common_words_so_far = []

    for word in list_of_words:
        # remove stopwords
        if word not in stopwords_and_redundancies.STOPWORDS:
            non_common_words_so_far.append(word)

    return non_common_words_so_far


def trim_max_values(full_dict: Dict[str, int], trim_value: int) -> Dict[str, int]:
    """
    This function will mutate the dictionary input by popping out
    entries with the highest key values.
    It removes as many entires as the trim_value input indicates.

    Preconditions:
     - trim_value >= 0
     - len(full_dict) > trim_value

    >>> trimmed = trim_max_values({'renewable': 2, 'actonclimate': 1, 'hello': 5}, 1)
    >>> trimmed == {'actonclimate': 1, 'renewable': 2}
    True
    """
    # change the value into a list
    list_of_values = list(full_dict.values())
    # change the keys into a list.
    list_of_keys = list(full_dict.keys())

    x = trim_value

    while x > 0:
        # gets rid of the most common words, similar to get_max_pairs function
        maximum = max(list_of_values)
        corresponding_key = list_of_keys[list_of_values.index(maximum)]

        full_dict.pop(corresponding_key)
        list_of_keys.remove(corresponding_key)
        list_of_values.remove(maximum)

        # making sure we get the number of dicts we want
        x -= 1

    return full_dict


def get_tweet_vader_score(file: str, tweets: List[reading_data.Tweet]) -> List:
    """Given the tweets, plot vader score of all tweet texts

    Preconditions:
      - tweets != []
      - file is the path to a text file containing vader sentiment analysis data.
    """
    vader = reading_data.read_vader(file)

    # vader scores accumulator
    scores_so_far = []

    for twit in tweets:
        tweet_score_so_far = 0
        tweets_in_vader_so_far = 0
        twit_words = twit.tweet.split(' ')
        for word in twit_words:
            if word in vader:
                tweet_score_so_far += vader[word]
                tweets_in_vader_so_far += 1

        scores_so_far.append(round(tweet_score_so_far / max(1, tweets_in_vader_so_far), 2))
    # removes the tweet that scored 0 because they have
    # no vader lexicon words in them.
    while 0 in scores_so_far:
        scores_so_far.remove(0)

    return scores_so_far


def get_vader_score_ratios(vader_scores: List) -> List:
    """Returns a list of given vader_scores split into 7 categories, as
    described in vader_piechart
    """
    vader_ratio = [0, 0, 0, 0, 0, 0, 0]

    for score in vader_scores:
        if score >= 2:
            vader_ratio[0] += 1
        elif score >= 1:
            vader_ratio[1] += 1
        elif score >= 0.2:
            vader_ratio[2] += 1
        elif score >= -0.2:
            vader_ratio[3] += 1
        elif score >= -1:
            vader_ratio[4] += 1
        elif score >= -2:
            vader_ratio[5] += 1
        else:
            vader_ratio[6] += 1

    return vader_ratio


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'typing', 'reading_data', 'stopwords_and_redundancies'],
        'max-line-length': 150,
        'disable': ['R1705', 'C0200', 'R1702']
    })

    import doctest

    doctest.testmod()
