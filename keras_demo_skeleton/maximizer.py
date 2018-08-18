# -*- coding: utf-8 -*-

import sys
import time
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from maximizer.generic_maximizer import GenericMaximizer


def wider_model():
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def larger_model():
    # create model
    model = Sequential()
    model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


# define base model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


class Maximizer(GenericMaximizer):
    def __init__(self):
        """
            Initialize code
        """
        GenericMaximizer.__init__(self)

    def do_housing_scenario(self):
        """
            Initially taken from this sample code:
            https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/
        :return: nothing
        """

        my_start_time = time.time()
        # load dataset
        dataframe = pandas.read_csv(my_instance.data["datafile"], delim_whitespace=True, header=None)
        dataset = dataframe.values
        # split into input (X) and output (Y) variables
        X = dataset[:, 0:13]
        Y = dataset[:, 13]
        print("data loaded in ", time.time() - my_start_time, " seconds")


        my_start_time = time.time()
        # fix random seed for reproducibility
        seed = 7
        numpy.random.seed(seed)
        # evaluate model with standardized dataset
        estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)
        kfold = KFold(n_splits=10, random_state=seed)
        results = cross_val_score(estimator, X, Y, cv=kfold)
        print("step 1: done in ", time.time() - my_start_time, " seconds")
        print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

        my_start_time = time.time()
        # evaluate model with standardized dataset
        numpy.random.seed(seed)
        estimators = []
        estimators.append(('standardize', StandardScaler()))
        estimators.append(('mlp', KerasRegressor(build_fn=baseline_model, epochs=50, batch_size=5, verbose=0)))
        pipeline = Pipeline(estimators)
        kfold = KFold(n_splits=10, random_state=seed)
        results = cross_val_score(pipeline, X, Y, cv=kfold)
        print("step 2: done in ", time.time() - my_start_time, " seconds")
        print("Standardized: %.2f (%.2f) MSE" % (results.mean(), results.std()))

        my_start_time = time.time()
        numpy.random.seed(seed)
        estimators = []
        estimators.append(('standardize', StandardScaler()))
        estimators.append(('mlp', KerasRegressor(build_fn=larger_model, epochs=50, batch_size=5, verbose=0)))
        pipeline = Pipeline(estimators)
        kfold = KFold(n_splits=10, random_state=seed)
        results = cross_val_score(pipeline, X, Y, cv=kfold)
        print("step 3: done in ", time.time() - my_start_time, " seconds")
        print("Larger: %.2f (%.2f) MSE" % (results.mean(), results.std()))

        my_start_time = time.time()
        numpy.random.seed(seed)
        estimators = []
        estimators.append(('standardize', StandardScaler()))
        estimators.append(('mlp', KerasRegressor(build_fn=wider_model, epochs=100, batch_size=5, verbose=0)))
        pipeline = Pipeline(estimators)
        kfold = KFold(n_splits=10, random_state=seed)
        results = cross_val_score(pipeline, X, Y, cv=kfold)
        print("step 4 done in ", time.time() - my_start_time, " seconds")
        print("Wider: %.2f (%.2f) MSE" % (results.mean(), results.std()))


if __name__ == "__main__":

    my_instance = Maximizer()
    my_instance.use_command_line()
    my_instance.use_config_file()
    my_instance.sys_info()

    if my_instance.data["scenario"] == "housing":
        print("Starting " + my_instance.get_name())
        print("Scenario " + my_instance.data["scenario"])
        my_instance.do_housing_scenario()
    else:
        print("ERROR: Could not recognize scenario " + my_instance.data["scenario"])

    print("All done. Have a great day!")
