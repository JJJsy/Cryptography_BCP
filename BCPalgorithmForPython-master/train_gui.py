'''
@Description: In User Settings Edit
@Author: JSY
@Date: 2019-10-20 13:21:15
@LastEditTime: 2019-10-20 13:45:10
@LastEditors: Please set LastEditors
'''
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier  # AdaBoost

from sklearn.utils import shuffle

file = pd.read_csv('')

def train_svm(df):
    df = shuffle(df)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = preprocessing.StandardScaler()
    x_train_scaler = scaler.fit_transform(x_train)
    x_test_scaler = scaler.fit_transform(x_test)

    clf= LinearSVC()
    clf.fit(x_train_scaler, y_train)
    y_predict = clf.predict(x_test_scaler)
    # print('clf_1_acc:%0.4f' % accuracy_score(y_predict, y_test))
    return accuracy_score(y_predict, y_test)

def train_lr(df):
    df = shuffle(df)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = preprocessing.StandardScaler()
    x_train_scaler = scaler.fit_transform(x_train)
    x_test_scaler = scaler.fit_transform(x_test)

    clf=LogisticRegression(solver='sag')
    clf.fit(x_train_scaler, y_train)
    y_predict = clf.predict(x_test_scaler)
    # print('clf_1_acc:%0.4f' % accuracy_score(y_predict, y_test))
    return accuracy_score(y_predict, y_test)

def train_cart(df):
    df = shuffle(df)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = preprocessing.StandardScaler()
    x_train_scaler = scaler.fit_transform(x_train)
    x_test_scaler = scaler.fit_transform(x_test)

    clf=DecisionTreeClassifier()
    clf.fit(x_train_scaler, y_train)
    y_predict = clf.predict(x_test_scaler)
    # print('clf_1_acc:%0.4f' % accuracy_score(y_predict, y_test))
    return accuracy_score(y_predict, y_test)

def train_AdaBoostClassifier(df):
    df = shuffle(df)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = preprocessing.StandardScaler()
    x_train_scaler = scaler.fit_transform(x_train)
    x_test_scaler = scaler.fit_transform(x_test)

    clf=AdaBoostClassifier()
    clf.fit(x_train_scaler, y_train)
    y_predict = clf.predict(x_test_scaler)
    # print('clf_1_acc:%0.4f' % accuracy_score(y_predict, y_test))
    return accuracy_score(y_predict, y_test)