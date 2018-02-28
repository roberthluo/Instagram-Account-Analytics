'''
iterate_photos.py allows us to go through the directory of the S3 bucket and
runs rekognition with it
'''

import boto3, re, json

def make_json(data2write):
    with open('output.txt','w') as out:
        json.dump(obj = data2write, fp = out, indent = 3)

def main():
    # Object and variable used to run Rekognition API
    client=boto3.client('rekognition','us-west-2')

    # You may want to put the file path here
    bucket_name = 'seg4300proj1-w2018'

    #Objects and list used to retrieve the names of each
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('seg4300proj1-w2018')
    lst_imgs=[]

    rekog_img_results = {}
    lst_all_photos = []

    # Collect all the image file names
    for i in bucket.objects.all():
        if(re.search('[A-z]*.jpg',i.key)):
            lst_imgs.append(str(i.key))
            #print(i.key)

    # Run run run, let rekognition do all the dirty work
    for img_name in lst_imgs:
        rekog_img_results['File_Name'] = img_name
        response = client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':img_name}})
        rekog_img_results['Analysis'] = response
        #print('Detected labels for ' + img_name)
        lst_all_photos.append(rekog_img_results)

    make_json(combine_all_results)

if __name__ == "__main__":
    main()
