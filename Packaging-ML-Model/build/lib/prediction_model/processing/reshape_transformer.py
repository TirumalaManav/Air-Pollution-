from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class ReshapeForLSTM(BaseEstimator, TransformerMixin):
    def __init__(self, time_steps=1):
        self.time_steps = time_steps

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Check if input is 2D
        if len(X.shape) != 2:
            raise ValueError("Input must be a 2D array")

        n_samples, n_features = X.shape

        # Ensure the features can be reshaped correctly
        if n_features % self.time_steps != 0:
            raise ValueError("Number of features must be divisible by time_steps")

        n_features_per_time_step = n_features // self.time_steps

        # Reshape to (n_samples, time_steps, n_features_per_time_step)
        return X.reshape((n_samples, self.time_steps, n_features_per_time_step))
