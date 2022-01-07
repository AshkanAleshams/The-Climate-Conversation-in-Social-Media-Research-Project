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

from typing import Dict, List

# graphing libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

# from other files
import computing_data


def locations_wordcloud(words: Dict[str, int], image: str) -> None:
    """
    Plots a word cloud designed for words related to twitter user locations.
    """
    # Generate a word cloud image
    earth = np.array(Image.open(image))
    # set a min font size and a max font size, and how the size of a word in word cloud scales
    # so the graph won't look too ridiculous
    earth_word_cloud = WordCloud(background_color="white", mode="RGBA", mask=earth,
                                 min_font_size=0, max_font_size=50,
                                 relative_scaling=0.5).generate_from_frequencies(words)

    # create coloring from image
    image_colors = ImageColorGenerator(earth)

    plt.figure(figsize=[11, 11])
    # Let word cloud have the colour of the picture
    plt.imshow(earth_word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
    # creates a title
    plt.suptitle('About The Tweeters: Where Do They Live?', size='xx-large',
                 y=0.92, weight='bold', family='sans-serif')
    plt.axis("off")

    plt.show()


def tweet_words_wordcloud(words: Dict[str, int], image: str) -> None:
    """
    Plots a word cloud designed for words related to words in tweets.
    """
    # Generate a word cloud image
    speech = np.array(Image.open(image))
    # set a min font size and a max font size, and how the size of singular word scales
    # so the graph won't look too ridiculous
    speech_word_cloud = WordCloud(background_color="white", mode="RGBA", mask=speech,
                                  min_font_size=2, max_font_size=50,
                                  relative_scaling=0.5).generate_from_frequencies(words)

    # create coloring from image
    image_colors = ImageColorGenerator(speech)

    plt.figure(figsize=[10, 10])
    # Let word cloud have the colour of the picture
    plt.imshow(speech_word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
    # creates a title
    plt.suptitle('About The Tweets: What Are They Saying?', size='xx-large',
                 y=0.87, weight='bold', family='sans-serif')
    plt.axis("off")

    plt.show()


def descriptions_wordcloud(words: Dict[str, int], image: str) -> None:
    """
    Plots a word cloud designed for words related to twitter user descriptions.
    """
    # Generate a word cloud image
    brain = np.array(Image.open(image))
    # set a min font size and a max font size, and how the size of singular word scales
    brain_word_cloud = WordCloud(background_color="white", mode="RGBA", mask=brain,
                                 min_font_size=2, max_font_size=50,
                                 relative_scaling=0.5).generate_from_frequencies(words)

    # create coloring from image
    image_colors = ImageColorGenerator(brain)

    plt.figure(figsize=[10, 10])
    # Let word cloud have the colour of the picture
    plt.imshow(brain_word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
    # creates a title
    plt.suptitle('About The Tweeters: How Do They Describe Themselves?', size='xx-large', y=0.89,
                 weight='bold', family='sans-serif')
    plt.axis("off")

    plt.show()


def hashtags_wordcloud(words: Dict[str, int], image: str) -> None:
    """
    Draws a word cloud designed for words related to tweet hashtags.
    """
    # Generate a word cloud image
    bird = np.array(Image.open(image))
    # set a min font size and a max font size, and how the size of singular word scales
    bird_word_cloud = WordCloud(background_color="white", mode="RGBA", mask=bird,
                                min_font_size=2, max_font_size=50,
                                relative_scaling=0.5).generate_from_frequencies(words)

    # create coloring from image
    image_colors = ImageColorGenerator(bird)

    plt.figure(figsize=[10, 10])
    # Let word cloud have the colour of the picture
    plt.imshow(bird_word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
    # creates a title
    plt.suptitle('About The Tweets: What Are The Hashtags?', size='xx-large', y=0.89,
                 weight='bold', family='sans-serif')
    plt.axis("off")

    plt.show()


def vader_piechat(vader_scores: List) -> None:
    """
    Draws a piechart designed for VADER sentiment analysis data.
    """

    labels = 'Extremely Positive', 'Positive', 'Mildly Positive', 'Neutral', 'Mildly Negative', \
             'Negative', 'Extremely Negative'
    # uses get_vader_score_ratios to compute sizes of each respective pie
    sizes = computing_data.get_vader_score_ratios(vader_scores)
    explode = (0, 0.1, 0, 0, 0, 0, 0)  # "explode" designates which pie slightly slides
    # out of frame

    _, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.suptitle('Distribution of Tweet VADER Sentiment Positivity Ratings',
                 size='medium', y=0.95, weight='bold', family='sans-serif')

    plt.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'typing', 'computing_data', 'matplotlib.pyplot', 'wordcloud',
                          'numpy', 'PIL'],
        'max-line-length': 150,
        'disable': ['R1705', 'C0200']
    })

    import doctest

    doctest.testmod()
