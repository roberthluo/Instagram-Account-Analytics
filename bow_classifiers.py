import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import numpy

df = pd.read_csv('training.csv', sep='\t', names=['Classification', 'Labels'], lineterminator='\n')

print df.to_string()

#create array to match values
arr = list()
arr.append('Nature')
arr.append('Politician')
arr.append('Celebrity')
arr.append('Space')

# Change classifications to numerical values
df.loc[df["Classification"]=='Nature',"Classification"]=0
df.loc[df["Classification"]=='Politician',"Classification"]=1
df.loc[df["Classification"]=='Celebrity',"Classification"]=2
df.loc[df["Classification"]=='Space',"Classification"]=3

# print out table
print df.to_string()

df_x=df["Labels"]
df_y=df["Classification"]

# Create TfidfVectorizer and fit transform on labels generated
cv = TfidfVectorizer()
x_traincv = cv.fit_transform(df_x)
x_train_shape = x_traincv.shape
y_train = df_y.astype('int')


# Use Multinomial Naive Bayes to generate
mnb = MultinomialNB()
mnb.fit(x_traincv, y_train)

str = 'Military Uniform Human People Person Speech Person Furniture Indoors Trademark Brochure Flyer Paper Poster Human People Person Broom Furniture People Person Speech People Person Suit Human Person Human Human People Flora Person Wheelchair Human Reception Room Person Speech Press Conference Indoors Furniture Person People Crowd Audience People Woman Clothing Female Girl Jar Blonde Crowd Press Conference Person Audience Flora Waiting Room Human Flag Coat American Flag Emblem Person Speech Crowd Human Vehicle Audience Person Debate Human Room Person Vigil Pottery'
test = [str]

# Generate and predict the probability to see if input matches dataset using Naive Bayes
x_testcv = cv.transform(test)
nb_results = mnb.predict_proba(x_testcv)
nb_prediction = mnb.predict(x_testcv)
print "Naive Bayes:"
print "[  Nature      Politician  Celebrity   Space     ]"
print nb_results
print nb_prediction, arr[nb_prediction[0]]
print "\n"

# Generate and predict the probability to see if input matches dataset using Support Vector Machine
svm = SVC(probability=True)
svm.fit(x_traincv, y_train)
results = svm.predict_proba(x_testcv)
svm_prediction = svm.decision_function(x_testcv)
print "SVM"
print "[  Nature      Politician  Celebrity   Space     ]"
print results
print svm_prediction
arr_results = svm_prediction.tolist()
print numpy.argmax(arr_results[0]), arr[numpy.argmax(arr_results[0])]
