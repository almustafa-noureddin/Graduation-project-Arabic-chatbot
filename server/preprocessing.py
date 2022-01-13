import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin 
from sklearn.externals import joblib 
from sklearn.pipeline import Pipeline 
from .helper import resource_path 
def clean_text(text):
    import re 
    search = ["أ","إ","آ","ة","_","-","/",".","،"," و "," يا ",'"',"","'","ى","\\",'\n', '\t','&quot;','?','؟','!'] 
    replace = ["ا","ه"," "," ","","",""," و"," يا ","","","","ي","",' ', ' ',' ',' ? ',' ؟',' ! ']
    #remove tashkeel 
    p_tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]') 
    text = re.sub(p_tashkeel,"", text)
    #remove longation 
    p_longation = re.compile(r'(.)\1+') 
    subst = r"\1\1" 
    text = re.sub(p_longation, subst, text) 
    text = text.replace('وو ', 'و') 
    text = text.replace('يي ', 'ي') 
    text = text.replace('اا ', 'ا') 
    text = text.replace('؟', '') 
    for i in range(0, len(search)): 
        text = text.replace(search[i], replace[i])
    #trim 
    text = text.strip() 
    return text
def stop_words_removal(sentance, word_list): 
    sentance = clean_text(sentance) 
    for word in sentance.split(): 
        if word in word_list: 
            sentance = sentance.replace(word, '') 
    sentance = clean_text(sentance) 
    return sentance
class TextCleaner(BaseEstimator, TransformerMixin): 
    def __init__(self):
        pass
    def fit(self, X): 
        return self 
    def transform(self, X): 
        temp = np.array([]) 
        for text in X: 
            t = clean_text(text) 
            temp = np.append(temp, t) 
        X = temp.reshape(-1, 1) 
        return X
class StopWordsRemoval(BaseEstimator, TransformerMixin): 
    def __init__(self, stop_words_path): 
        self.words_list = joblib.load(stop_words_path) 
    def fit(self, X): 
        return self 
    def transform(self, X): 
        temp = np.array([]) 
        for text in X:
            t = stop_words_removal(text[0], word_list=self.words_list) 
            temp = np.append(temp, t)
        X = pd.Series(temp)
        return X
def make_preprocessing_pipline(): 
    stop_words_path = resource_path('preprocessing\\stop_words.pkl') 
    pipeline = Pipeline([('cleaner', TextCleaner()), ('removal', StopWordsRemoval(stop_words_path))]) 
    return pipeline
if __name__ == "__main__": 
    pass