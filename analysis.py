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
from sklearn.linear_model import LinearRegression

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


# Generate word clouds for each instagram account
for i in range(len(data_set)): 
    wc = WordCloud().generate(str(data_set[0][i]))
    title = "Account Name on Instagram: " + usernames[i] 
    save_img = str(usernames[i])+".jpg"
    plt.figure()
    plt.title(title)
    plt.imshow(wc)
    plt.show() 
    plt.imsave(save_img, wc, dpi = 16000)


naive_bayes = pd.Series([ 0.06778083,0.28809941,0.6228622,0.02125756],name = "Naive Bayes")
svm = pd.Series([0.19072639,0.2441206,0.49359594,0.07155707],name="SVM")

# Obtain relevant values for regression lines
slope,yint = np.polyfit(naive_bayes,svm,1)

# Generate R^2 values and equation to denote correlation between naive bayes and SVM
_,_,r_val,_,_ = stats.linregress(naive_bayes,svm)  
r_value = "R^2: "+str(r_val**2) 
equation = "Equation: svm = " + str(slope) +' (naive_bayes) + '+str(yint)

# Plot the graph of the results along with the regression line and see 'results'
plt.scatter(naive_bayes,svm)
plt.plot(naive_bayes,slope*naive_bayes + yint, '-') 
plt.title("Comparison Between Naive Bayes and SVM")  
plt.text(0.3,0.2,r_value) 
plt.text(0.3,0.15,equation)
plt.xlabel("Naive Bayes") 
plt.ylabel("SVM")
plt.show()
