import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('training.csv', sep='\t', names=['Classification', 'Labels'], lineterminator='\n')

#df.loc[df["Classification"]=='Nature',"Classification"]=0
#df.loc[df["Classification"]=='Politician',"Classification"]=1
#df.loc[df["Classification"]=='Space',"Classification"]=2
#print df.head()
print df.to_string()

df_x=df["Labels"]
df_y=df["Classification"]

cv = TfidfVectorizer()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

x_traincv= cv.fit_transform(x_train)

a = x_traincv.toarray()

print a
