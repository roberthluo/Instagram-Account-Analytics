import json
import boto3
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

file_name = 'tags.json'
tags = []
classes = ['Nature','Politician','Space']
# Begin connection to DynamoDB
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

# Get array of table names associated with current AWS account
table_names = client.list_tables()

# Check if table exists
def checkExists():
    if not 'imagetags' in table_names['TableNames']:
        raise ValueError('Table does not exist.')
    else:
        table = dynamodb.Table('imagetags')
        get_tags(table)

# Get tags from DB
def get_tags(table):
    data = table.scan()
    format_tags(data)

# Change formatting returned from tags
def format_tags(data):
    print("format tags")
    items_list = data.get('Items')
    acc_list = []
    for x in items_list:
        print("account tags")
        str = ""
        for key in x:
            str += x[key]
            str += " "
        acc_list.append(str)
    vectorize(acc_list)


# Create vectors from tags
def vectorize(data):
    test = [
           'space nebula star stars moon astronomy eclipse',
	   'nature sky clouds rock outdoors ocean reef tree canyon bird dog animal',
           'person people human building military',
           'universe galaxy solar asteroid meteor'
	   ]
    #cv = CountVectorizer()
    cv = TfidfVectorizer()
    x_traincv = cv.fit_transform(data)
    #print x_traincv.toarray()
    #print cv.get_feature_names()
    #a = x_traincv.toarray()
    #print a
    #print cv.inverse_transform(a[0])
    x_train_shape = x_traincv.shape
    y_train = range(x_train_shape[0])
    mnb = MultinomialNB()
    #y_train = y_train.astype('int')
    mnb.fit(x_traincv, y_train)
    print mnb
    x_testcv = cv.transform(test)
    a2 = x_testcv.toarray()
    #print a2
    pred = mnb.predict(x_testcv)
    print pred
    results = pred.tolist()
    print results
    num = 0
    for i in results:
        print "Result: ", num, " is of class: ", classes[i]
        num += 1
checkExists()
