import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


def naive_bayes_evaluator(clf, target, test):

    test = [[1],[0]]

    predicted = clf.predict(test)
    np.mean(predicted == target)
    print("naive_bayes_evaluator", np.mean(predicted == target))


naive_bayes_evaluator()
