"""
CSC110 Fall 2020 Project, Phase 2 Climate Deniers in Social Media:
Analyzing Linguistic Patterns of Climate Change Related Tweets.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the professors and TAs
in CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this CSC110 project,
please consult with us.

This file is Copyright (c) 2020 Jiajin Wu, Ehsan Emadi, Ashkan Aleshams and Michael Galloro.
"""
import json
from typing import List, Dict, Tuple, Set, Any


# graphing libraries:

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image


# required files:

# stopwords_and_redundancies file:
from stopwords_and_redundancies import STOPWORDS, LOCATION_REDUNDANCIES

# reading_data file:
from reading_data import read_file_data, User, Tweet, make_tweets, read_vader

# computing_data file:
from computing_data import accumulate_tweet_words, accumulate_locations, accumulate_descriptions, \
    accumulate_hashtags, get_max_tweet_words, clean_locations, clean_words, \
    trim_max_values, get_tweet_vader_score, get_vader_score_ratios

# visualizing_data file:
from visualizing_data import locations_wordcloud, tweet_words_wordcloud, \
    descriptions_wordcloud, hashtags_wordcloud, vader_piechat


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # Please always keep this section uncommented while running the following examples:

    a = read_file_data('climate_id.jsonl')
    b = make_tweets(a)
    # c = get_max_tweet_words(b, 10000)  # 10000 words is recommended, but it can be replaced.

    ####################################################################################
    ####################################################################################
    # Word Cloud Graphs:
    ####################################################################################
    ####################################################################################

    # EXAMPLE 1: Word cloud for tweets' words:
    # d = accumulate_tweet_words(c)
    # tweet_words_wordcloud(d, '\img\speech.png')

    # EXAMPLE 2: Word cloud for locations:
    # d = accumulate_locations(b)
    # locations_wordcloud(d, '\img\earth.png')

    # EXAMPLE 3: Word cloud for users' descriptions:
    # d = accumulate_descriptions(b)
    # descriptions_wordcloud(d, '\img\brain.png')

    # EXAMPLE 4: Word cloud for hashtags:
    # d = accumulate_hashtags(b)
    # hashtags_wordcloud(d, '\img\bird.png')

    ####################################################################################
    ####################################################################################
    # VADER Pie Chart:
    ####################################################################################
    ####################################################################################

    # (Delete the "#" and space before each EXAMPLE.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block

    # EXAMPLE 5: VADER pie chart:

    # e = get_tweet_vader_score('vader_file', b)
    # f = get_vader_score_ratios(e)
    # vader_piechat(f)

    # pyTA
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'reading_data', 'computing_data', 'visualizing_data'],
        'max-line-length': 150,
        'disable': ['R1705', 'C0103', 'E9997'],
    })
