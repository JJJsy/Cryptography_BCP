'''
@Descripttion: 
@version: 
@Author: HuiKwok
@Date: 2019-10-10 06:53:46
@LastEditors: HuiKwok
@LastEditTime: 2019-10-10 07:01:56
'''
from charm.toolbox.integergroup import IntegerGroup
from charm.schemes.pkenc.pkenc_rsa import RSA_Enc, RSA_Sig
from charm.core.math.integer import integer,randomBits,random,randomPrime,isPrime,encode,decode,hashInt,bitsize,legendre,gcd,lcm,serialize,deserialize,int2Bytes,toInt


secparam = 1024
p, q = randomPrime(int(secparam/2),True),randomPrime(int(secparam/2),True)
N = p * q
N2 = N * N

g = random(N2)
print(type(g))
int(g) -1