'''
@Descripttion: 
@version: 
@Author: HuiKwok
@Date: 2019-10-08 03:05:42
@LastEditors: HuiKwok
@LastEditTime: 2019-10-09 16:16:46
'''

import time
import numpy as np
from BCP import *
from KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize

print("generating the parameters of keys......")
print("generating the master key......")
print("generating the pk and sk of each data provider......\n")
mk = readMKFromFile(mkPath = 'mk')
bcp = genBCPContext(paramPath = 'param')

pk1, sk1 = genKeyPair(bcp,keyPairPath = 'keyPair1')
pk2, sk2 = genKeyPair(bcp,keyPairPath = 'keyPair2')
pk3, sk3 = genKeyPair(bcp,keyPairPath = 'keyPair3')

pa = readParamFromFile(paramPath = 'param')
N = pa.N


print("Data provider A is dealing......")
m1 = 66
print("Data provider A's data m1 is:",m1)
print("Data provider A use pk1 to encrypt m1")
ciphertext_m1 = bcp.Encrypt(pk1,m1)
print("The ciphertext is:",ciphertext_m1,"\n")



print("Data provider B is dealing......")
m2 = 99
print("Data provider B's data m2 is:",m2)
print("Data provider B use pk2 to encrypt m2")
ciphertext_m2 = bcp.Encrypt(pk2,m2)
print("The ciphertext is:",ciphertext_m2,"\n")


r1 = 4
r2 = 1

ciphertext_r1 = bcp.Encrypt(pk1,r1)
ciphertext_r2 = bcp.Encrypt(pk2,r2)

ciphertext_m1_r1 = bcp.multiply(ciphertext_m1,ciphertext_r1)
ciphertext_m2_r2 = bcp.multiply(ciphertext_m2,ciphertext_r2)



m1_r1 = bcp.DecryptMK(ciphertext_m1_r1,mk,pk1)
m2_r2 = bcp.DecryptMK(ciphertext_m2_r2,mk,pk2)

ciphertext_whole_mr_pk1 = bcp.Encrypt(pk1,m1_r1+m2_r2)
ciphertext_whole_mr_pk2 = bcp.Encrypt(pk2,m1_r1+m2_r2)


ciphertext_r1_r2_pk1 = bcp.Encrypt(pk1,r1+r2)
ciphertext_r1_r2_pk2 = bcp.Encrypt(pk2,r1+r2)
ciphertext_r1_r2_pk1 = bcp.exponentiate(ciphertext_r1_r2_pk1,N-1)
ciphertext_r1_r2_pk2 = bcp.exponentiate(ciphertext_r1_r2_pk2,N-1)

ciphertext_m1_m2_pk1 = bcp.multiply(ciphertext_whole_mr_pk1,ciphertext_r1_r2_pk1)
ciphertext_m1_m2_pk2 = bcp.multiply(ciphertext_whole_mr_pk2,ciphertext_r1_r2_pk2)


print(bcp.Decrypt(ciphertext_m1_m2_pk1,sk1))
print(bcp.Decrypt(ciphertext_m1_m2_pk2,sk2))


