'''
@Descripttion: 
@version: 
@Author: HuiKwok
@Date: 2019-10-09 16:06:37
@LastEditors: HuiKwok
@LastEditTime: 2019-10-09 16:09:06
'''

import time
import numpy as np
from BCP import *
from KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize

keyGen()
# bcp = genBCPContext(paramPath = 'param')

# secparam = 1024
# p,q = randomPrime(512,True),randomPrime(512,True)

# pk,sk = readKeyPairFromFile(keyPairPath = 'keyPair')
# print(pk,sk)
# keyGen()

# mk = readMKFromFile(mkPath = 'mk')
# pa = readParamFromFile(paramPath = 'param')
# bcp = genBCPContext(paramPath = 'param')
# pk1,sk1 = genKeyPair(bcp,keyPairPath = 'keyPair1')
# pk2,sk2 = genKeyPair(bcp,keyPairPath = 'keyPair2')
# pk3,sk3 = genKeyPair(bcp,keyPairPath = 'keyPair3')
# pa = readParamFromFile(paramPath = 'param')
# N = pa.N