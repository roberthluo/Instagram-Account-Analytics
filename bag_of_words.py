import json
import boto3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

file_name = 'tags.json'
tags = []


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
    #print('Data Scanned', data)
    format_tags(data)

# Change formatting returned from tags
def format_tags(data):
    print("format tags")

    for key, value in data.items():
        print(key)

    items_list = data.get('Items')
    #print(type(items_list))
    #print(items_list)

    acc_list = []
    for x in items_list:

        print("account tags")
        str = ""
        for key in x:
            #print (x[key])
            str += x[key]
            str += " "
        acc_list.append(str)
        vectorize(acc_list)


# Create vectors from tags
def vectorize(data):
    print("vectorize")
    vectorizer = CountVectorizer()

    # This is number of occurences
    x_tag_counts = vectorizer.fit_transform(data).todense()

    # Prints number of occurences for each social media profile
    print( x_tag_counts )
    #print( vectorizer.vocabulary_ )
    # Shaping the count
    x_tag_counts_shape = x_tag_counts.shape
    print( "Counts" , x_tag_counts_shape )

    # This is number of frequencies (Used to determine for bigger instagram account (bigger accounts have higher count values))
    # term frequencies
    tfidf_transformer = TfidfTransformer()
    x_tag_tfidf = tfidf_transformer.fit_transform(x_tag_counts)
    x_tag_tf_shape = x_tag_tfidf.shape
    print( "Frequencies", x_tag_tf_shape)

    # Some have 2 classifiers
    classify(x_tag_tfidf, x_tag_tf_shape[0])


# Training the classifier
def classify(x_tag_tfidf, user_type_size):
    # since we only have 1-2 types currently
    user_type = range(user_type_size)


    # Not sure about this part
    clf = MultinomialNB().fit(x_tag_tfidf, user_type)
    print(clf)

    # Need to store classifier somewhere


checkExists()
