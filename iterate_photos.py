'''
iterate_photos.py allows us to go through the directory of the S3 bucket and
runs rekognition for each photos
To run it do python iterate_photos.py on Terminal
'''

import boto3, re, json

def make_json(data2write):
   with open('output.json','a') as out:
        json.dump(obj = data2write, fp = out, indent = 3) 
def main():
    # Object and variable used to run Rekognition API
    client=boto3.client('rekognition','us-west-2')
    # You may want to put the file path here
    #bucket_name = 'seg4300proj1-w2018'
    bucket_name = 'seg4300proj1-w2018'
    #Objects and list used to retrieve the names of each
    s3 = boto3.resource('s3')
    #bucket = s3.Bucket(bucket_name)

    # Collect all the image file names
    def photos_name(name_bket=bucket_name):
        bucket = s3.Bucket(name_bket)
        lst_imgs=[]

        for i in bucket.objects.all():
            if(re.search('[A-z]*.jpg',i.key)):
                lst_imgs.append(str(i.key))
        #print(lst_imgs)
        return(lst_imgs)

    lst_imgs = photos_name()
    
    # Run run run, let rekognition do all the dirty work
    def process_photos(lst_imgs = lst_imgs):
        json_list = []
        rekog_img_results = {}
        lst_all_photos = []

        for img_name in lst_imgs:
            print(img_name)
            rekog_img_results['File_Name'] = img_name
            response = client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':img_name}})
            rekog_img_results['Analysis'] = response
            lst_all_photos.append(rekog_img_results)
            json_list.append(rekog_img_results.copy())
        make_json(json_list)

    process_photos()

if __name__ == "__main__":
    main()
