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
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from collections import OrderedDict

data_set = pd.read_csv("/Users/johnkim/Documents/GitHub/SEG4300-project/training.csv", 
                       header = None).replace('\t',' ')
usernames = ['nature','nationalparkservice','narendramodi','realdonaldtrump','justinpjtrudeau','anthony_joshua','kingjames','kendalljenner','therock','kimkardashian','nasa']

'''
words = []
category = []

for i in range(len(data_set)): 
    process_row = data_set[0][i].replace('\t',' ').split(' ') 
    words.append(process_row[1:len(process_row)]) 
    category.append(process_row[0])
    
category = pd.Series(category, name = "Category") 
words = pd.DataFrame(words) 
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
    plt.imsave(save_img, wc, format='jpg', dpi = 16000)
    
#data_set = pd.concat([category,words], axis = 1)