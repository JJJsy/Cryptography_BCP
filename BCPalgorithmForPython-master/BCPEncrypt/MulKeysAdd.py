'''
@Descripttion: 
@version: 
@Author: HuiKwok
@Date: 2019-10-09 10:24:55
@LastEditors: Please set LastEditors
@LastEditTime: 2019-10-14 13:27:06
'''

import time
import math
import numpy as np
from BCP import *
from KeyGenAndRead import *
from charm.core.math.integer import serialize, deserialize
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC


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


def fed_integrate_model(model1, model2):

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


if __name__ == '__main__':

    x1 = -0.3996482
    x2 = 0.39963947
    start = time.clock()
    print(x1+x2)
    print("normal addition costs:", time.clock()-start)
    print("---------------------------------------------")
    start = time.clock()
    print(mulkeys_add_float(x1, x2))
    print("mul additions costs:", time.clock()-start)
    # array1 = np.array([1,2,3,4])
    # array2 = np.array([1,2,3,4])
    # array = []
    # for i in range(len(array1)):
    #     array.append(array1[i]+array2[i])

    # array = np.array(array)
    # print(array)
    # print(type(array))
    # x1 = 0.11111111
    # x2 = 0.00000001

    # #print(mulKeys_add_int(x1,x2))
    # print(mulkeys_add_float(x1,x2))

    start = time.clock()

    iris = load_iris()
    features = iris.data
    target = iris.target

    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.6, random_state=10)

    model_1 = LinearSVC()
    model_1.fit(x_train, y_train)

    model_2 = LinearSVC()
    model_2.fit(x_train, y_train)

    model = fed_integrate_model(model_1, model_2)
    print(model_1.coef_)
    print(model_1.intercept_)
    print(model.coef_)
    print(model.intercept_)

    print('SVM compution time: '+str(time.clock() - start))
