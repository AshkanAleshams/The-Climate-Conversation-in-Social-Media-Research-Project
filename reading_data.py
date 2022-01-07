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

import json
from typing import List, Dict


def read_file_data(file: str) -> List[Dict]:
    """Return a list of dictionary values containing the given tweet data file.

    Preconditions:
        - file is the path to a JSON file containing tweet data.
    """
    with open(file, encoding="UTF-8") as json_file:
        data = [json.loads(line) for line in json_file]

    return data


class User:
    """
    A custom data type that represents the person who tweeted.

    Instance Attributes:
        - name: the name of the person who sent the tweet
        - location: where the person is
        - description: this is a description of the user

    Representation Invariants:
        - self.name != ''
    """
    name: str
    location: str
    description: str

    def __init__(self, name: str, location: str, description: str) -> None:
        self.name = name
        self.location = location
        self.description = description


class Tweet:
    """
    A custom data type that represents tweet data.

    Instance Attributes:
        - user: a user of tweet with the dataclass User
        - tweet: the words written in a tweet
        - hashtags: the hashtags in a tweet
        - retweet: the number of retweets it has

    Representation Invariants:
        - self.tweet != ''
        - '@ RT' not in self.tweet
    """
    user: User
    tweet: str
    hashtags: List[str]

    def __init__(self, user: User, tweet: str, hashtags: List[str]) -> None:
        self.user = user
        self.tweet = tweet
        self.hashtags = hashtags


def make_tweets(climate_id: List[Dict]) -> List[Tweet]:
    """Returns a list with all the tweet objects inside it"""
    list_of_tweets = []

    for id_wanted in climate_id:
        # Eliminating retweets
        if 'RT @' not in id_wanted['full_text']:
            # Tweet Info
            text = id_wanted['full_text']
            hashtags = []

            # User Info
            name = id_wanted['user']['screen_name']
            location = id_wanted['user']['location']
            description = id_wanted['user']['description']

            user = User(name, location, description)

            for entry in id_wanted['entities']['hashtags']:
                hashtags.append(entry['text'])

            list_of_tweets.append(Tweet(user, text, hashtags))

    return list_of_tweets


def read_vader(file: str) -> Dict[str, float]:
    """Returns a dictionary containing all of the words in the Vader Sentiment as keys,
    and their corresponding intensity rating as values.

    Preconditions:
        - file is the path to a text file containing vader sentiment analysis data.
    """
    with open(file) as f:
        lines = f.readlines()

    vader_dict_so_far = {}

    for line in lines:
        line = line.split('\t')
        vader_dict_so_far[line[0]] = float(line[1])

    return vader_dict_so_far


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'typing', 'json'],
        'max-line-length': 150,
        'disable': ['R1705', 'C0200'],
        'allowed-io': ['read_file_data', 'read_vader']
    })

    import doctest

    doctest.testmod()
