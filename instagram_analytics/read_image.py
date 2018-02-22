
import boto3

if __name__ == "__main__":
    fileName='input.jpg'
    bucket='rekognition-examples-bucket'
    
    client=boto3.client('rekognition','us-west-2')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

    print('Detected labels for ' + fileName)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
 

