import numpy as np 
import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin 
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline 
from .helper import resource_path 
class Vectorizer(BaseEstimator, TransformerMixin): 
    def __init__(self, vectorizer_path):
        self.vectorizer = joblib.load(vectorizer_path) 
    def fit(self, X): 
        return self 
    def transform(self, X):
        X = self.vectorizer.transform(X) 
        return X
class SimilarityExtractor(BaseEstimator, TransformerMixin): 
    def __init__(self, vectors_path): 
        from sklearn.metrics.pairwise import cosine_similarity 
        self.vectors = joblib.load(vectors_path) 
        self.cos_sim = cosine_similarity 
    def fit(self, X):
        return self 
    def transform(self, X):
        print(X) 
        X = self.cos_sim(X, self.vectors) 
        return X
def make_feature_extraction_pipeline(vec): 
    vectorizer_path = resource_path(f'feature_extraction\\{vec}\\vec_{vec}.pkl') 
    vectors_path = resource_path(f'feature_extraction\\{vec}\\question_vectors_{vec}.pkl') 
    duplications_path = resource_path(f'feature_extraction\\{vec}\\duplicated_{vec}.pkl') 
    pipeline = Pipeline([('vectorizer', Vectorizer(vectorizer_path)), ('similarity', SimilarityExtractor(vectors_path))]) 
    return pipeline 
if __name__ == '__main__':
    pass