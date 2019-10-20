'''
@Descripttion: 根据BCP算法，本文件分别实现了多密钥下整数和浮点数的加法。
@version: V1.1
@Author: HuiKwok
@Date: 2019-10-09 10:24:55
@LastEditors: Please set LastEditors
@LastEditTime: 2019-10-11 06:16:48
'''

import time
import numpy as np
from BCP import *
# from KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize


def mulkeys_add_int(x1,x2):
    bcp = BCP()
    mk = bcp.GetMK()
    param = bcp.GetParam()
    pk1,sk1 = bcp.KeyGen()
    pk2,sk2 = bcp.KeyGen()
    N = param.N

    r1 = np.random.randint(1,100)
    r2 = np.random.randint(1,100)

    ciphertext_x1 = bcp.Encrypt(pk1,x1)
    ciphertext_x2 = bcp.Encrypt(pk2,x2)

    ciphertext_r1 = bcp.Encrypt(pk1,r1)
    ciphertext_r2 = bcp.Encrypt(pk2,r2)

    ciphertext_x1_r1 = bcp.multiply(ciphertext_x1,ciphertext_r1)
    ciphertext_x2_r2 = bcp.multiply(ciphertext_x2,ciphertext_r2)

    x1_r1 = bcp.DecryptMK(ciphertext_x1_r1,mk,pk1)
    x2_r2 = bcp.DecryptMK(ciphertext_x2_r2,mk,pk2)

    ciphertext_all_sum_pk1 = bcp.Encrypt(pk1,x1_r1+x2_r2)
    ciphertext_all_sum_pk2 = bcp.Encrypt(pk2,x1_r1+x2_r2)

    ciphertext_r1_r2_pk1 = bcp.Encrypt(pk1,r1+r2)
    ciphertext_r1_r2_pk2 = bcp.Encrypt(pk2,r1+r2)
    ciphertext_r1_r2_pk1 = bcp.exponentiate(ciphertext_r1_r2_pk1,N-1)
    ciphertext_r1_r2_pk2 = bcp.exponentiate(ciphertext_r1_r2_pk2,N-1)

    ciphertext_x1_x2_pk1 = bcp.multiply(ciphertext_all_sum_pk1,ciphertext_r1_r2_pk1)
    ciphertext_x1_x2_pk2 = bcp.multiply(ciphertext_all_sum_pk2,ciphertext_r1_r2_pk2)

    result_A = bcp.Decrypt(ciphertext_x1_x2_pk1,sk1)
    result_B = bcp.Decrypt(ciphertext_x1_x2_pk2,sk2)

    if(result_A == result_B):
        return int(result_A)
    else:
        return None

def mulkeys_add_float(a,b):

    int_a = int(a)
    int_b = int(b)

    float_a = a - int(a)
    float_b = b - int(b)
    
    if int_a == 0 and int_b ==0:
        sum_int_ab = 0
    else:
        sum_int_ab = mulkeys_add_int(int_a,int_b)
    
    if float_a < 0.00000001 and float_b < 0.00000001:
        return float(int(sum_int_ab))

    float_a = float(("%.8f" % float_a))
    float_b = float(("%.8f" % float_b))

    float_a = int(float_a * 100000000)
    float_b = int(float_b * 100000000)

    sum_float_ab = mulkeys_add_int(float_a,float_b)
    
    sum_float_ab = float(int(sum_float_ab)) / 100000000

    sum_ab = float(int(sum_int_ab)) + sum_float_ab

    return sum_ab

def mulkeys_add_array(array1,array2):
    pass

def fed_integrate_model(model1,model2):
    pass
    
if __name__ == '__main__':
    
    x1 = 1.029012
    x2 = 2.108112
    
    start = time.clock()
    print(x1+x2)
    print("Normal addition costs:",time.clock()-start)
    
    start = time.clock()
    print(mulkeys_add_float(x1,x2))
    print("Multikeys addition costs:",time.clock()-start)
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

