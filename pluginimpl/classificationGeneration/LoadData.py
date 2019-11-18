from pandas import Series, DataFrame
import pandas as pd
import pickle
from string import punctuation
import re
from tqdm import tqdm
from nltk.stem.porter import PorterStemmer
from textblob import TextBlob
from pandas import Series, DataFrame
import pickle
from collections import Counter
import numpy as np

class dataprocesser(object):
    def __init__(self):
        self.all_words = set()

    def removeUnWantedWord(self,x):
        try:
            # add all the conditions that are found here to remove unwanted words
            x = x.replace('status: current','')
            x = x.replace('status:','')
            x = x.replace('deprecated','')
            x = x.translate(str.maketrans('', '', punctuation))
            # x = re.sub(r'[^\w]','',x)
            return x
        except:
            return x

    def convert2list(self,i):
        """Returns a list with words - spell corrected and stemmed"""
        porter = PorterStemmer()
        words = list()
        flag = True
        try:
            for word in i.split(' '):
                if (len(word) > 2):
                    word_digits_removed = re.sub(r'[0-9]*', '', self.removeUnWantedWord(word)).lower()
                    stemmed_word = porter.stem(word_digits_removed)
                    spelling_corrected_word = TextBlob(stemmed_word).correct()

                    words.append(str(spelling_corrected_word))
                    self.all_words.add(str(spelling_corrected_word))
        except AttributeError:
            print(i)
            flag = False
        return words, flag

if __name__ == '__main__':

    # reading the traindata
    classificationsfile = pd.read_csv('classifications.csv', usecols=[' Description', ' Alarm classification'])

    # Removing the lines which have description as "status: current"
    classificationsfile = classificationsfile[classificationsfile[' Description'] != "status: current "]

    dataclass = dataprocesser()
    classificationsfile = classificationsfile.applymap(dataclass.removeUnWantedWord)
    # print(classificationsfile)
    all_words = set()
    # print(classificationsfile.isna())
    # classificationsfile.to_csv('test.csv')
    for i in tqdm(classificationsfile[' Description']):
        dataclass.convert2list(i)
    print(dataclass.all_words)
    f = open('total_words-1.p', 'wb')
    pickle.dump(dataclass.all_words, f)
    f.close()




