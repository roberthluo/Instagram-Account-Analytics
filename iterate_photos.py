'''
iterate_photos.py allows us to go through the directory of the S3 bucket and 
'''

import boto3
import re

# Preliminaries: Let's start off by reading all files

if __name__ == "__main__":

    # Object and variable used to run Rekognition API
    client=boto3.client('rekognition','us-west-2')
    # You may want to put the file path here
    bucket_name = 'seg4300proj1-w2018'

    #Objects and list used to retrieve the names of each
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('seg4300proj1-w2018')
    lst=[]

    # Collect all the image file names
    for i in bucket.objects.all():
        if(re.search('[A-z]*.jpg',i.key)):
            lst.append(str(i.key))
            #print(i.key)

    # Run run run, let rekognition do all the dirty work
    for img_name in lst:
        response = client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':img_name}})
        print('Detected labels for ' + i)
        for label in response['Labels']:
            print (label['Name'] + ' : ' + str(label['Confidence']))
