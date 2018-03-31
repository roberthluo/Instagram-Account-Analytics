import json
import boto3
from sklearn.feature_extraction.text import CountVectorizer


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
    print( vectorizer.fit_transform(data).todense() )
    print( vectorizer.vocabulary_ )

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

    #print(acc_list)

    vectorize(acc_list)

def is_json(json_str):
    try:
        json_object = json.loads(json_str)
    except ValueError, e:
        return False
    return True
checkExists()
