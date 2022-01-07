"""
CSC110 Fall 2020 Project, Part 1 Open Json File and get the hashtags. Then count how many of each hashtags we have.
Then we will grade them with how supportive they are with climate change.

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
from typing import List, Dict, Tuple

import plotly.graph_objects as go

import vader_sentiment

false = False
true = True
null = None


# Part 1 Getting the hashtags that we want
def getting_wanted_hashtags(file: str) -> List[str]:
    """
    This function gets all the wanted hashtags that satisfies our wants
    """
    my_file = read_file_data(file)
    wanted_tweets = delete_retweets(my_file)
    original_hashtags = get_hashtag(wanted_tweets)
    return getting_lowercase_hashtags(original_hashtags)


def read_file_data(file: str) -> List[dict]:
    """Return a List containing all the dictionaries in the given file.
    """
    with open(file, encoding="UTF-8") as json_file:
        data = [json.loads(line) for line in json_file]

    return data


def delete_retweets(tweets: List[dict]) -> List[dict]:
    """
    This will delete all the retweets that is in the file that we opened

    Preconditions:
        - len(tweets) != 0
    """
    original_tweets = []
    for tweet in tweets:
        if 'RT @' not in tweet["full_text"]:
            original_tweets.append(tweet)
    return original_tweets


def get_hashtag(climate_id: List[dict]) -> List[str]:
    """
    This function will collect all the hashtags in climate_id and put them into a list.

    Preconditions:
        - climate_id is a file that is a list of dicts that is opened by read_file_data in project_p1.py
    """
    hashtags = []
    for dictionaries in climate_id:
        entities_value = dictionaries["entities"]
        multi_hashtag = entities_value["hashtags"]
        for values in multi_hashtag:
            hashtags.append(values["text"])
    return hashtags


def getting_lowercase_hashtags(hashtags: List[str]) -> List[str]:
    """
    This function will make all the hashtags lowercase.

    Preconditions:
      - hashtags != []
    """
    lowercase_hashtags = []
    for hashtag in hashtags:
        lowercase_hashtags.append(hashtag.lower())
    return lowercase_hashtags


def get_tweet_vader_score(tweets: List[dict]) -> None:
    """Given the tweets, plot vader score of all tweet texts

    Preconditions:
      - tweets != []
    """


    vader_scores = []
    for dictionaries in tweets:
        score = vader_sentiment.report_sentiment(dictionaries['full_text'])
        vader_scores.append(score[1])

    return plot_points(vader_scores)


def plot_points(vader_scores: List[float]) -> None:
    """Plot vader scores

    Preconditions:
      - vader_scores != []
    """
    # Create a blank figure
    fig = go.Figure()

    # Add the raw data
    fig.add_trace(go.Scatter(x=[x for x in range(0, len(vader_scores))], y=vader_scores, mode='markers', name='Tweets represented by Vader Lexicon', ))

    fig.update_layout(
                      title='Tweets represented by Vader Lexicon',
                      xaxis_title='Tweets',
                      yaxis_title='Vader Score')
    # Display the figure in a web browser.
    fig.show()
