import json
import boto3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


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
    #vectorize(data)

# Create vectors from tags
def vectorize(data):
    print("vectorize")
    vectorizer = CountVectorizer()

    # This is number of occurences
    x_tag_counts = vectorizer.fit_transform(data).todense()

    # Prints number of occurences for each social media profile
    #print( x_tag_counts )
    #print( vectorizer.vocabulary_ )
    # Shaping the count
    x_tag_counts_shape = x_tag_counts.shape
    print( "Counts" , x_tag_counts_shape )

    # This is number of frequencies (Used to determine for bigger instagram account (bigger accounts have higher count values))
    # term frequencies
    # tf_transformer = TfidfTransformer(use_idf=False).fit(x_tag_counts)
    # x_tag_tf = tf_transformer.transform(x_tag_counts)
    # x_tag_tf_shape = x_tag_tf.shape
    # print( "Frequencies", x_tag_tf_shape )

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



checkExists()
