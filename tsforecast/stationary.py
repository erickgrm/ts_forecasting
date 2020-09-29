import statsmodels.api as sm

class Stationarity(object):
    
    def __init__(self):
        self.tested = False
        self.d = 0
        self.kpss_stationary = False
        self.adf_stationary = False
    
    def fit(self, timeseries, alpha=0.05, verbose=True):
        
        self.tested = True
    
        # Kwiatkowski–Phillips–Schmidt–Shin test
        kpsstest = sm.tsa.kpss(timeseries, regression='c', nlags="auto")
        kpss_pvalue = kpsstest[1]
        self.kpss_lags = kpsstest[2]
        if alpha < kpss_pvalue:
            self.kpss_stationary = True
    
        # Augmented Dickey-Fuller test
        adftest = sm.tsa.adfuller(timeseries, autolag='AIC')
        adf_pvalue = adftest[1]
        adf_lags = adftest[2] 
        if adf_pvalue < alpha:
            self.adf_stationary = True
        
        if verbose:
            print("KPSS stationary:", self.kpss_stationary)
            print("ADF stationary:", self.adf_stationary)
            
    
    def transform(self, timeseries, max_diff=3):        
        flag = False
        ts = timeseries
        while not(self.kpss_stationary and self.adf_stationary) and self.d < max_diff:
            print('>> ',self.d+1,'differencing')
            ts = ts[1:]-ts[:-1]
            self.fit(ts, alpha=0.05, verbose=True)
            self.d += 1        
        return ts
    
    def fit_transform(self, timeseries, alpha=0.05, verbose=True, max_diff=3):
        self.fit(timeseries, alpha=alpha, verbose=verbose)
        
        return self.transform(timeseries, max_diff=max_diff)
    
