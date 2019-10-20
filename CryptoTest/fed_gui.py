'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-20 14:53:12
@LastEditTime: 2019-10-20 14:53:12
@LastEditors: your name
'''
import time
import math
import numpy as np
import pandas as pd
from BCP import *
from KeyGenAndRead import *
from charm.core.math.integer import serialize, deserialize

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier  # AdaBoost


def mulkeys_add_int(x1, x2):

    mk = readMKFromFile(mkPath='mk')
    bcp = genBCPContext(paramPath='param')
    pk1, sk1 = genKeyPair(bcp, keyPairPath='keyPair1')
    pk2, sk2 = genKeyPair(bcp, keyPairPath='keyPair2')
    pk3, sk3 = genKeyPair(bcp, keyPairPath='keyPair3')
    pa = readParamFromFile(paramPath='param')
    N = pa.N

    r1 = np.random.randint(1, 100)
    r2 = np.random.randint(1, 100)

    ciphertext_x1 = bcp.Encrypt(pk1, x1)
    ciphertext_x2 = bcp.Encrypt(pk2, x2)

    ciphertext_r1 = bcp.Encrypt(pk1, r1)
    ciphertext_r2 = bcp.Encrypt(pk2, r2)

    ciphertext_x1_r1 = bcp.multiply(ciphertext_x1, ciphertext_r1)
    ciphertext_x2_r2 = bcp.multiply(ciphertext_x2, ciphertext_r2)

    x1_r1 = bcp.DecryptMK(ciphertext_x1_r1, mk, pk1)
    x2_r2 = bcp.DecryptMK(ciphertext_x2_r2, mk, pk2)

    ciphertext_all_sum_pk1 = bcp.Encrypt(pk1, x1_r1+x2_r2)
    ciphertext_all_sum_pk2 = bcp.Encrypt(pk2, x1_r1+x2_r2)

    ciphertext_r1_r2_pk1 = bcp.Encrypt(pk1, r1+r2)
    ciphertext_r1_r2_pk2 = bcp.Encrypt(pk2, r1+r2)
    ciphertext_r1_r2_pk1 = bcp.exponentiate(ciphertext_r1_r2_pk1, N-1)
    ciphertext_r1_r2_pk2 = bcp.exponentiate(ciphertext_r1_r2_pk2, N-1)

    ciphertext_x1_x2_pk1 = bcp.multiply(
        ciphertext_all_sum_pk1, ciphertext_r1_r2_pk1)
    ciphertext_x1_x2_pk2 = bcp.multiply(
        ciphertext_all_sum_pk2, ciphertext_r1_r2_pk2)

    result_A = bcp.Decrypt(ciphertext_x1_x2_pk1, sk1)
    result_B = bcp.Decrypt(ciphertext_x1_x2_pk2, sk2)
    #print result_A
    #print result_B
    #print '-----------------------'
    #print N
    if(result_A == result_B):
        if abs(int(result_A)-0) < abs(int(math.pow(2, 64))-int(result_A)):
            return (integer(result_A))
        else:
            return (int(result_A) - int(math.pow(2, 64)))
    else:
        return None


def mulkeys_add_float(a, b):

    if a*b > 0:
        if a + b < 0:
            flag = 1
        else:
            flag = 0
        a = abs(a)
        b = abs(b)
    else:
        flag = 0

    int_a = int(a)
    int_b = int(b)

    float_a = a - int(a)
    float_b = b - int(b)

    if int_a == 0 and int_b == 0:
        sum_int_ab = 0
    else:
        sum_int_ab = mulkeys_add_int(int_a, int_b)

    if abs(float_a) < 0.00000001 and abs(float_b) < 0.00000001:
        return float(int(sum_int_ab))

    float_a = float(("%.8f" % float_a))
    float_b = float(("%.8f" % float_b))
    float_a = int(float_a * 100000000)
    float_b = int(float_b * 100000000)

    sum_float_ab = mulkeys_add_int(float_a, float_b)

    sum_float_ab = float(int(sum_float_ab)) / 100000000

    sum_ab = float(int(sum_int_ab)) + sum_float_ab
    if flag == 1:
        sum_ab = -sum_ab
    return sum_ab


def mulkeys_add_array(array1, array2):
    if len(array1) != len(array2):
        return None
    array = []
    for i in range(len(array1)):
        array.append(mulkeys_add_float(array1[i], array2[i]))
    array = np.array(array)
    return array


def mulkeys_add_2Darray(array1, array2):
    if len(array1) != len(array2):
        return None

    row = len(array1)
    array = []

    for i in range(row):
        array.append(mulkeys_add_array(array1[i], array2[i]))
    array = np.array(array)
    return array


def fed_integrate_model_svm(model1, model2):

    coef_1 = model1.coef_
    coef_2 = model2.coef_

    intercept_1 = model1.intercept_
    intercept_2 = model2.intercept_

    classes = model1.classes_

    model = LinearSVC()
    model.coef_ = mulkeys_add_2Darray(model1.coef_, model2.coef_)/2
    model.intercept_ = mulkeys_add_array(
        model1.intercept_, model1.intercept_)/2
    model.classes_ = classes

    return model

def fed_integrate_model_cart(model1, model2):

    coef_1 = model1.coef_
    coef_2 = model2.coef_

    intercept_1 = model1.intercept_
    intercept_2 = model2.intercept_

    classes = model1.classes_

    model = DecisionTreeClassifier()
    model.coef_ = mulkeys_add_2Darray(model1.coef_, model2.coef_)/2
    model.intercept_ = mulkeys_add_array(
        model1.intercept_, model1.intercept_)/2
    model.classes_ = classes

    return model


def fed_integrate_model_lr(model1, model2):

    coef_1 = model1.coef_
    coef_2 = model2.coef_

    intercept_1 = model1.intercept_
    intercept_2 = model2.intercept_

    classes = model1.classes_

    model = LogisticRegression(solver='sag')
    model.coef_ = mulkeys_add_2Darray(model1.coef_, model2.coef_)/2
    model.intercept_ = mulkeys_add_array(
        model1.intercept_, model1.intercept_)/2
    model.classes_ = classes

    return model

