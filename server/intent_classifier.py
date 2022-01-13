import numpy as np 
from sklearn.externals import joblib 
from .helper import resource_path, generate_paths
from feature_extraction import make_feature_extraction_pipeline
from preprocessing import make_preprocessing_pipline
from sklearn.base import BaseEstimator 
class Voter(BaseEstimator): 
    def __init__(self, voting='hard', models=None): 
        self.voting = voting 
        self.models = models 
    def fit(self, X, y): 
        return self 
    def predict(self, X): 
        predictions = [] 
        probas = [] 
        if self.voting == 'soft': 
            return self.__soft_voting(X) 
        elif self.voting == 'hard': 
                print('hard_voting') 
                for _, model in self.models.items(): 
                    if _ != 'hard_voter': 
                        predictions.append(model.predict(X)) 
                return self.__mode_finder(predictions, X) 
    def predict_proba(self, X): 
        probas = [] 
        for _, model in self.models.items(): 
            if _ != 'soft_voter' and _ != 'hard_voter': 
                probas.append(model.predict_proba(X)) 
        return np.average(probas, axis=0)
    def __soft_voting(self, X, index=None): 
        probas = [] 
        for _, model in self.models.items(): 
            if _ != 'soft_voter' and _ != 'hard_voter': 
                probas.append(model.predict_proba(X)) 
        if not index: 
            return [np.argmax(np.average(probas, axis=0))] 
        else: 
            return [np.argmax(np.average(probas[index], axis=0))] 
    def __mode_finder(self, preds, X): 
        from collections import Counter 
        preds = [p[0] for p in preds] 
        counts = Counter(preds).items() 
        counts = list(counts) 
        counts.sort(key=lambda x: x[1], reverse=True)                             
        self.counts = counts if len(counts) <= 4 else counts[:4] 
        max_count = counts[0][1]
        index=[counts[0][0]] 
        for value, count in counts[1:]: 
            if count == max_count:
                index.append(value) 
        if len(index) > 1: 
            return self.__soft_voting(X, index=index) 
        else: 
            return [index[0]] 
    def get_most_voted(self, X, n): 
        predictions = [] 
        probas = [] 
        if self.voting == 'soft': 
            return self.__soft_voting(X) 
        elif self.voting == 'hard': 
            for _, model in self.models.items(): 
                if _ != 'hard_voter': 
                    predictions.append(model.predict(X)) 
        from collections import Counter 
        predictions = [p[0] for p in predictions] 
        counts = Counter(predictions).items() 
        counts = list(counts) 
        counts.sort(key=lambda x: x[1], reverse=True) 
        counts = counts
        if len(counts) <= n:
        else counts[:n] 
        return counts 
def load_models(vec, voting=['soft', 'hard']): 
    relative_paths = generate_paths(obj='models', vec=vec) 
    paths = [resource_path(path) for path in relative_paths] 
    keys = [path.split('\\')[-1] for path in paths] 
    models = {} 
    for k, p in zip(keys, paths): 
        models[k[:-4]] = joblib.load(p) 
    for v in voting: 
        models[f'{v}_voter'] = Voter(voting=v, models=models) 
    return models 
def prepair_input(text, vec): 
    preprocessing_pipeline = make_preprocessing_pipline() 
    feature_extraction_pipeline = make_feature_extraction_pipeline(vec=vec) 
    clean_text = preprocessing_pipeline.fit_transform(text) 
    features = feature_extraction_pipeline.fit_transform(clean_text) 
    return features
def get_candidate_classes(text, models, vec): 
    X = prepair_input([text], vec) 
    most_voted = models['hard_voter'].get_most_voted(X, 4) 
    most_voted = [m[0] for m in most_voted] 
    return most_voted 
def make_prediction(text, models, vec): 
    X = prepair_input([text], vec) 
    predictions = {} 
    propabilities = {} 
    for name, model in models.items(): 
        prediction = model.predict(X) 
        predictions[name] = prediction[0] 
        try: 
            class_props = model.predict_proba(X) 
        except: 
            class_props = None 
        propabilities[name] = class_props 
    return predictions, propabilities
if __name__ == '__main__': pass