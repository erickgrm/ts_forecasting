from sklearn.metrics import mean_squared_error as mse

class Model():

    def __init__():
        self.train_score = 0.0
        self.val_score = 0.0


    def score(self, X, target_col)
        series = X[target_col].values
        forecasts = self.predict(X.drop([target_col], axis=1))

        return mse(series, forecasts)

