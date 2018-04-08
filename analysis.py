#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:11:55 2018

@author: johnkim
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:32:30 2018

@author: johnkim
"""
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#import seaborn as sb
from sklearn.linear_model import LinearRegression
#from collections import OrderedDict

data_set = pd.read_csv("/Users/johnkim/Documents/GitHub/SEG4300-project/training.csv", 
                       header = None)
data_set = data_set.replace('\t',' ')
usernames = ['nature','nationalparkservice','narendramodi','realdonaldtrump','justinpjtrudeau','anthony_joshua','kingjames','kendalljenner','therock','kimkardashian','nasa']

words = []
category = []

for i in range(len(data_set)): 
    process_row = data_set[0][i].replace('\t',' ').split(' ') 
    words.append(process_row[:len(process_row)]) 
    category.append(process_row[0])
    
category = pd.Series(category, name = "Category") 
words = pd.DataFrame(words) 

'''
def occurrence_words(df2process = data_set):
    freq_words = {}
        
    for row_df in df2process: 
        #print(df2process[row_df])
        #lst_row_df = row_df.split(" ")
        
        for words in lst_row_df: 
            if words in freq_words.keys(): 
                freq_words[words] += 1 
            else: 
                freq_words[words] = 1
        
    #return(freq_words)
    

occurrence_words()
'''

# Wordcloud
for i in range(len(data_set)): 
    wc = WordCloud().generate(str(data_set[0][i]))
    title = "Account Name on Instagram: " + usernames[i] 
    save_img = str(usernames[i])+".jpg"
    plt.figure()
    plt.title(title)
    plt.imshow(wc)
    plt.show() 
    plt.imsave(save_img, wc, dpi = 16000)

classifiers  = pd.Series(['Nature','Politician','Celebrity','Space'], name ="Classifier")
naive_bayes = pd.Series([ 0.06778083,0.28809941,0.6228622,0.02125756],name = "Naive Bayes")
svm = pd.Series([0.19072639,0.2441206,0.49359594,0.07155707],name="SVM")
results = pd.concat([naive_bayes, svm], axis = 1)
regression = np.polyfit(naive_bayes,svm,1)

plt.scatter(naive_bayes,svm) 
plt.title("Comparison Between Naive Bayes and SVM") 
plt.xlabel("Naive Bayes") 
plt.ylabel("SVM")
plt.show()


#sb.regplot(x = 'Naive Bayes', y = 'SVM', data = results)

#data_set = pd.concat([category,words], axis = 1)