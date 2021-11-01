import copy
import pandas as pd
import river
from river.naive_bayes import MultinomialNB
from river.feature_extraction import BagOfWords
from river.compose import Pipeline

class CategorizerModel:
    def __init__(self):
        self.setup()
    
    def setup(self):
        self.df = pd.read_csv('./data/stock_data.csv')
        self.df['Label'] = self.df['Sentiment'].apply(lambda s: 'bullish' if s > 0 else 'bearish')
        self.df = self.df[['Text','Label']]
        # Convert to Tuple
        self.data = self.df.to_records(index=False)
        # Build Pipeline
        self.pipe_nb = Pipeline(('vectorizer',BagOfWords(lowercase=True)),('nb',MultinomialNB()))
        #Initialize Metric
        self.metric = river.metrics.Accuracy()
        # Train
        for text,label in self.data:
            self.train_model(text,label)
        print(f"Model initialized with {self.metric}")
            

    def predict_category(self,text):
        # Make a Prediction
        return self.pipe_nb.predict_one(text)

    def metric(self):
        return self.metric

    def train_model(self,text,label):
        init_metric = copy.deepcopy(self.metric)
        y_pred = self.pipe_nb.predict_one(text)
        self.pipe_nb = self.pipe_nb.learn_one(text,label)
        self.metric = self.metric.update(label, y_pred)
        return {
            'metrics':{
                'new':f"{self.metric}",
                'old': f"{init_metric}"
            }
        }
