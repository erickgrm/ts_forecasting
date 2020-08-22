

from statsmodels.tsa.arima_model import ARMA 
from statsmodels.tsa.arima_model import ARIMA

class ARMA(Model):

    def __init__(self):
        self.p = None
        self.q = None
        self.AIC = None
        self.train_split = None
        self.val_split = None


    def fit(self, X, target_col)
        self.arma = self.best_arma(X, target_col)



    def predict(self):
        self.arma.predict(self.val_split, 

    def 


class ARIMA(Model);

class CNN(Model):

class LSTM(Model):

class AttentionLSTM(Model):



