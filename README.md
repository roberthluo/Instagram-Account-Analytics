

# Project-5:  Social media analytics

In this project, you will implement a new technique that learns a unique pattern of how individuals create social identities on social platforms. Anonymized user datasets will be obtained via APIs. By using the individual behavior patterns, you will try to detect anomalies on user accounts.  
    Platform: Your choice (recommended Rhadoop)  
    Deliverables:  The data analytics code,  anomaly function, the dataset on which the experiments have been run, performance results under various scenarios (i.e. latency, accuracy, precision, false negatives).  


Install and tools
-------
instagram-scraper:
```bash
$ pip install instagram-scraper
``` 
bokeh - data visualization on the web 
```bash 
$ pip install bokeh
```
numpy and scipy
```bash
$ sudo dnf install numpy scipy
```
matplotlib
``` bash
$ python -mpip install -U matplotlib
```
boto3
```bash
$ pip install boto3
```
TensorFlow 
```bash 
$ pip install tensorflow 
```


To Do:
1. Create database referencing unprocessed images to attributes in json file. (NoSQL) Parse username into our existing JSON file.
    - tags
    - edge_media_preview_like count
    - taken_at_timestamp
    - display_urls
    - owner_id
    - edge_media_to_comment

2. Run rekognition (on an ec2 instance not locally) (Create a new db with Results or add to previous db) 

3. Take two deep learning algorithms: Convoluted Neural Network and Deep Belief Network and compare the two to evaluate performance against Rekognition and store it in DynamoDB.
->Consider using AlexNet and caffe. 

4. Visualize our data from 3. using libraries such as matplotlib and bokeh and maybe Flask? (if we want a web interface)

Order of operations
1. iterate_photos.py
2. parser.py to parse output.json file and place in DynamoDB
3. output_csv.py to format tags and add class cooresponding to username and output training.csv to be used in model
4. bow_classifiers.py to perform Naive Bayes and SVM classification
