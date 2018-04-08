import json
import boto3
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import SGDClassifier
import csv

file_name = 'tags.json'
tags = []
#classes = ['Nature','Politician','Space']
# Begin connection to DynamoDB
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

# Get array of table names associated with current AWS account
table_names = client.list_tables()

classes = ['Nature','Politician','Celebrity','Space']
usernames = [['nature','nationalparkservice'],['narendramodi','realdonaldtrump','justinpjtrudeau'],['anthony_joshua','kingjames','kendalljenner','therock','kimkardashian'],['nasa']]

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
    format_tags(data, table)

# Change formatting returned from tags
def format_tags(data, table):
    fd = open('training.csv', 'w')
    for i, item in enumerate(classes):
        class_name = item #get the name of this class
        class_users = usernames[i] #get the list of usernames from each class
        for j, user in enumerate(class_users):
            item = {}
            item['username'] = user
            response = table.get_item(Key=item)
            row = response['Item']
            tag_str = ""
            line = class_name + '\t'
            for tags in row:
                tag_str += row[tags]
                tag_str += " "
            line += tag_str
            fd.write(line)
            fd.write('\n')

checkExists()
