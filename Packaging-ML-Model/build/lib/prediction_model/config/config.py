import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = 'pollution.csv'
TEST_FILE = 'pollution.csv'

MODEL_NAME = 'pollution_model.h5'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

TARGET = 'pollution'

FEATURES = ['pollution','dew', 'temp', 'pressure', 'w_speed', 'snow', 'rain']


NUMERICAL_FEATURES = ['pollution', 'dew', 'temp', 'pressure', 'w_speed', 'snow', 'rain']

CATEGORICAL_FEATURES = []

FEATURES_TO_ENCODE = []  # Encoding typically applies to categorical features

DROP_FEATURES = ['dew', 'temp', 'pressure', 'w_speed', 'snow', 'rain']

