import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class TSGenerator(object):

    def __init__(self, timesteps=100, baseline=0.0, slope=0, noise_level=1, noise_seed=None, 
                 season_split=0.5, period=30, amplitude=1.0, phase=0):
        self.timeseries_ = None
        self.normalized_ = None
        self.timesteps = timesteps
        self.time = np.arange(timesteps)
        self.baseline = baseline
        self.slope = slope
        self.noise_level = noise_level
        self.noise_seed = noise_seed
        self.season_split = season_split
        self.period = period
        self.amplitude = amplitude
        self.phase = phase

    def generate(self):
        self.timeseries = self.baseline + self.trend(self.time, self.slope) \
                          + self.seasonality(self.time, self.period, self.amplitude, self.phase, self.season_split) \
                          + self.white_noise(self.time, self.noise_level, self.noise_seed)                          

        return self.timeseries 


    def normalize(self):
        sc = MinMaxScaler()
        ts = self.timeseries
        self.normalized = sc.fit_transform(ts.reshape(-1,1))[0:,0]

        return self.normalized 

    
    def plot(self, format="-", start=0, end=None, label=None, normalized=False):
        if normalized:
            ts = self.normalize()
        else:
            ts = self.timeseries

        plt.plot(self.time[start:end], ts[start:end], format, label=label)
        plt.xlabel("Time")
        plt.ylabel("Value")
        if label:
            plt.legend(fontsize=14)
        plt.grid(True)

    def trend(self, time, slope=0):
        return slope * time

    def white_noise(self, time, noise_level, seed=None):
        if seed == None:
            seed = np.random.randint(10000)
        rnd = np.random.RandomState(seed)
        return rnd.randn(len(time)) * noise_level

    def seasonality(self, time, period, amplitude, phase, season_split):
        phase  = np.random.randint(period)
        season_time = ((time + phase) % period) / period
        return amplitude * self.seasonal_pattern(season_time, season_split)

    def seasonal_pattern(self, season_time, season_split):
        f1 = np.random.choice([np.cos, np.sin])
        return np.where(season_time < season_split,
                        f1(season_time * np.random.randint(4) * np.pi),
                        1 / np.exp(np.random.randint(1,8) * season_time))


class RWGenerator(object):

    def __init__(self, timesteps=100, baseline=0.0, noise_level=1, noise_seed=None):
        self.timeseries = None
        self.normalized = None
        self.timesteps = timesteps
        self.time = np.arange(timesteps)
        self.baseline = baseline
        self.noise_level = noise_level
        self.noise_seed = noise_seed

    def generate(self):
        if self.noise_seed == None:
            self.noise_seed = np.random.randint(10000)

        rnd = np.random.RandomState(self.noise_seed)
        noise = rnd.randn(self.timesteps) * self.noise_level
        X = np.empty(self.timesteps)
        X[0] = self.baseline
        for i in range(1, self.timesteps):
            X[i] = X[i-1] + noise[i-1]

        self.timeseries = X
        return self.timeseries

    def normalize(self):
        sc = MinMaxScaler()
        ts = self.timeseries
        self.normalized = sc.fit_transform(ts.reshape(-1,1))[0:,0]

        return self.normalized


    def plot(self, format="-", start=0, end=None, label=None, normalized=False):
        if normalized:
            ts = self.normalize()
        else:
            ts = self.timeseries

        plt.plot(self.time[start:end], ts[start:end], format, label=label)
        plt.xlabel("Time")
        plt.ylabel("Value")
        if label:
            plt.legend(fontsize=14)
        plt.grid(True)
        
