# Project-5:  Social media analytics

In this project, we will implement a new technique that learns a unique pattern of how individuals create social identities on social platforms. Anonymized user datasets will be obtained via APIs. By using the individual behavior patterns, we will try to detect anomalies on user accounts.  
    Platform: Python  
    Deliverables:  The data analytics code, anomaly function, the dataset on which the experiments have been run, performance results under various scenarios (i.e. latency, accuracy, precision, false negatives).  


Install and tools
-------
instagram-scraper:
```bash
$ pip install instagram-scraper
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

## Accounts Used:
Celebrity
[kimkardashian](https://www.instagram.com/kimkardashian/), [therock](https://www.instagram.com/therock/), [kendalljenner](https://www.instagram.com/kendalljenner/)

Politician
[realdonaldtrump](https://www.instagram.com/realdonaldtrump/), [narendramodi](https://www.instagram.com/narendramodi/), [justinpjtrudeau](https://www.instagram.com/justinpjtrudeau)

Sports
[ussoccer_wnt](https://www.instagram.com/justinpjtrudeau), [kingjames](https://www.instagram.com/kingjames), [anthony_joshua](https://www.instagram.com/anthony_joshua/)

Nature
[nationalparkservice](https://www.instagram.com/nationalparkservice), [nature](https://www.instagram.com/nature/)

Space
[nasa](https://www.instagram.com/nasa)


## Order of operations
1. Run instagram-scraper
2. Run name_script.py
3. Run iterate_photos.py
4. Run parser.py to parse output.json file and place in DynamoDB
5. Run output_csv.py to format tags and add class cooresponding to username and output training.csv to be used in model
6. Run bow_classifiers.py to perform Naive Bayes and SVM classification,
7. Run analysis.py to generate visual our data, generate a word cloud and Scatter plot Comparison



### To Do:
~~1. Create database referencing unprocessed images to attributes in json file. (NoSQL) Parse username into our existing JSON file.
    - tags
    - edge_media_preview_like count
    - taken_at_timestamp
    - display_urls
    - owner_id
    - edge_media_to_comment~~

~~2. Run rekognition (on an ec2 instance not locally) (Create a new db with Results or add to previous db)~~

~~3. Visualize our data from 3. using libraries such as matplotlib and bokeh and maybe Flask? (if we want a web interface)~~
