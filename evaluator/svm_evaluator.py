from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def svm_evaluator(clf, target, test):
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                               alpha=1e-3, random_state=42,
                                               max_iter=5, tol=None)),
    ])

    text_clf.fit(data, target)

    predicted = clf.predict(test)
    np.mean(predicted == target)


svm_evaluator()
