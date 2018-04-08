import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

df = pd.read_csv('training.csv', sep='\t', names=['Classification', 'Labels'], lineterminator='\n')
 
print df.to_string()

# Change classifications to numerical values
df.loc[df["Classification"]=='Nature',"Classification"]=0
df.loc[df["Classification"]=='Politician',"Classification"]=1
df.loc[df["Classification"]=='Celebrity',"Classification"]=2
df.loc[df["Classification"]=='Space',"Classification"]=3

# print out table
print df.to_string()

df_x=df["Labels"]
df_y=df["Classification"]

cv = TfidfVectorizer()

#print df_x

x_traincv = cv.fit_transform(df_x)

x_train_shape = x_traincv.shape
y_train = df_y.astype('int')

#print y_train

mnb = MultinomialNB()
mnb.fit(x_traincv, y_train)

#print mnb

test = ['Dark','Night','Space','Nebula','Star','Asteroid','Comet','Sun','Light','Planet']

x_testcv = cv.transform(test)

pred = mnb.predict_proba(x_testcv)
print "Naive Bayes:"
print pred


svm = SVC(probability=True)
svm.fit(x_traincv, y_train)
results = svm.predict_proba(x_testcv)[0]
#prediction = svm.decision_function(x_testcv)
print "SVM"
print results
