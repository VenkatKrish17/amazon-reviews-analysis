# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:37:46 2018

@author: Venkat
"""

import pandas as pd

from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

import seaborn as sns

#nltk.download('all');


def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

   
        
data=pd.read_csv('test.csv',sep=",",names=["class","title","review"]).head(n=1000)
#print(data[['class','title']])
my_stemmer = PorterStemmer();
tokenizer= RegexpTokenizer(r'\w+');
poswords=read_words("positive.txt")
negwords=read_words("negative.txt")
col=['text','class','senti'];
processeddata=pd.DataFrame(columns=col);

count=0;
for review,clas in zip(data['review'],data['class']):
    senticount=0;
    for token in tokenizer.tokenize(review):
        stemmed=my_stemmer.stem(token)
        if(stemmed not in stopwords.words('english')):
            if(stemmed in poswords):
                senticount+=1;
            elif(stemmed in negwords):
                senticount-=1;
    if(senticount>0):
        data.ix[count,'senti']='positive'
    elif(senticount<0):
        data.ix[count,'senti']='negative'
    else:
        data.ix[count,'senti']='neutral'
    count+=1;
print(data['class'])
print(data['senti'])
#plt.plot(data['senti'],data['class'],'ro')

#plt.scatter(data['senti'],data['class'],color=['red','green','blue'])
#plt.boxplot(data['class'],by=data['senti'])
sns.boxplot(x=data['senti'],y=data['class'])


    
        
        
        
    


