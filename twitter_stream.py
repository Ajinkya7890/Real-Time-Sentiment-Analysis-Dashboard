import pandas as pd

def get_tweets():

    tweets = [
        "I love learning Data Science",
        "Python is amazing",
        "Artificial Intelligence is changing the world",
        "This movie was fantastic",
        "The match today was incredible",
        "I am very happy with this product",
        "Fantastic dashboard design",
        "Machine learning is exciting",
        "The concert was wonderful",
        "Best experience ever",

        "This movie was terrible",
        "The service was disappointing",
        "Worst experience ever",
        "I hate waiting in traffic",
        "The website keeps crashing",
        "The food tasted awful",
        "Very poor customer support",
        "This update ruined everything",
        "I am frustrated with the results",
        "Bad performance overall",

        "Today is a normal day",
        "Nothing special happened today",
        "The meeting starts at 5 PM",
        "I went to the store",
        "Weather seems average today",
        "The train arrived on time",
        "Reading a new book",
        "Working on a project",
        "Just completed my assignment",
        "Having lunch now"
    ]

    return pd.DataFrame({
        "tweet": tweets
    })