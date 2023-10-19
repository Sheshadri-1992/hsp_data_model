import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn import datasets, linear_model
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

class IDS:

    def __init__(self):
        self.regr = None
        print("IDS model, training train_model")

    def get_regr_model(self):
        return self.regr

    def train_module(self):
        df = pd.read_csv('ids_data_trace.csv', header=None, names=['num_packets', 'payload_size', 'get_time', 'exec_time'])
        df.head()
        X = df[['num_packets', 'payload_size']].to_numpy()
        Y = df['exec_time'].to_numpy()
        (X_train, X_test, Y_train, Y_test) = train_test_split(X, Y)
        self.regr = linear_model.LinearRegression()
        self.regr.fit(X_train.reshape(-2, 2), Y_train.reshape(-1, 1))
        # Y_predict = regr.predict(X_test.reshape(-2, 2))

    def predict(self, attr1, attr2):
        X_test = np.array([attr1, attr2], dtype=np.float64)
        Y_predict = self.regr.predict(X_test.reshape(-2, 2))
        print("[IDS Latency Prediction] : {0}".format(Y_predict[0][0]))
        return Y_predict[0][0]    

# ids_obj = IDS()
# ids_obj.train_module()
# ids_obj.predict(300, 300)
