import csv
import os.path
import logging
import random

logger = logging.getLogger(__name__)


class Dataloader():

    def load_sentiment_analysis_dataset(self):
        """
        Soruce: http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/
        1 = positive
        0 = negative
        :return:
        """
        logger.debug("Loading Sentiment Analysis Dataset")
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "datasets/sentiment_analysis_dataset.csv")
        with open(path) as f:
            csvreader = csv.reader(f)
            next(csvreader) # skip header
            data = [(line[3],line[1]) for line in csvreader]
            random.shuffle(data) # Shuffle data
            train_data = data[:int((len(data) + 1) * .80)]  # Remaining 80% to training set
            test_data = data[int(len(data) * .80 + 1):]  # Splits 20% data to test set
            train_texts, train_classes = [list(tup) for tup in zip(*train_data)]
            test_texts, test_classes = [list(tup) for tup in zip(*test_data)]
        logger.debug("Found "+str(len(data))+" entries!")
        return train_texts, train_classes, test_texts, test_classes

    def load_small_fake_data(self):
        texts = ["This is super!", "This is very bad."]
        classes = [1, 0]
        return texts, classes
