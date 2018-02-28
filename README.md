

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
numpy and scipy
```bash
$ sudo dnf install numpy scipy
```

scikit-learn:
```bash
$ pip install -U scikit-learn
```
boto3
```bash
$ pip install boto3
```



To Do:
1. Create database referencing unprocessed images to attributes in json file. (NoSQL)
    - tags
    - edge_media_preview_like count
    - taken_at_timestamp
    - display_urls
    - owner_id
    - comments
    - location
    
2. For Parks Service, get location from tags

3. Run rekognition on an ec2 instance not locally (Create a new db with Results or add to previous db) 

