'''
@Descripttion: 
@version: 
@Author: HuiKwok
@Date: 2019-10-10 02:19:59
@LastEditors: HuiKwok
@LastEditTime: 2019-10-10 11:16:27
'''
from charm.toolbox.integergroup import IntegerGroup
from charm.schemes.pkenc.pkenc_rsa import RSA_Enc, RSA_Sig
from charm.core.math.integer import integer,randomBits,random,randomPrime,isPrime,encode,decode,hashInt,bitsize,legendre,gcd,lcm,serialize,deserialize,int2Bytes,toInt

secparam = 1024

# 1- 原bcp需要修改处
p, q = randomPrime(int(secparam/2),True),randomPrime(int(secparam/2),True)
pp = (p-1)/2
qq = (q-1)/2

# 2- 原bcp需要修改处
N = p * q
if bitsize(N) ==secparam and len(int2Bytes(N)) == secparam/8 and int2Bytes(N)[0] &128 !=0:
    print("good N")
N2 = N**2
g = random(N2)
one = integer(1)% N2

g = random(N2)


while True:
    g = random(N2)
    # 3- 原bcp需要修改处
    g = integer((int(g)-1)*(int(g)-1))% N2
    if g == one:
        continue
    tmp = g**p % N2
    if tmp == one:
        continue
    tmp == g**pp % N2
    if tmp == one:
        continue
    tmp = g**q % N2
    if tmp == one:
        continue
    tmp = g**qq % N2
    if tmp == one:
        continue
    tmp = g**(p*pp) % N2
    if tmp == one:
        continue
    tmp = g**(p*q) % N2
    if tmp == one:
        continue
    tmp = g**(p*qq) % N2
    if tmp == one:
        continue
    tmp = g**(pp*q) % N2
    if tmp == one:
        continue
    tmp = g**(pp*qq) % N2
    if tmp == one:
        continue
    tmp = g**(q*qq) % N2
    if tmp == one:
        continue
    tmp = g**(p*pp*q) % N2
    if tmp == one:
        continue
    tmp = g**(p*pp*qq) % N2
    if tmp == one:
        continue
    tmp = g**(p*q*qq) % N2
    if tmp == one:
        continue
    tmp = g**(pp*q*qq) % N2
    if tmp == one:
        continue
    break
# print(g)
# k = integer((g**(pp*qq)-1)) 
pp * qq
# 4- 原bcp需要修改处
k = integer(int(g**(pp * qq))-1) / N % N
MK = {"pp":pp,"qq":qq}

tmp = N2 / 2
sk = random(tmp) % N2
pk = (g**sk) % N2

plaintext = 100122
r = random(N/4) % N2
A = (g**r) % N2
B1 = (N*plaintext+1)% N2
B2 = (pk**r) % (N2)
B = B1*B2 % N2
ciphertext = {"A":A,"B":B}


# 5- 原bcp需要修改处
t1 = integer(int(ciphertext['B']*((ciphertext['A']**-1)**sk))-1) % N2
# t1 = (ciphertext['B']*((ciphertext['A']**-1)**sk)-1)% N2
# m = integer(t1) / N
m = integer(t1) / N
# print(type(m))
print(m)


# print(ciphertext)

# k_1 = k**-1
# tmp = (pk**(MK['pp']*MK['qq']))

k_1 = k**-1
tmp = (int(pk**(MK['pp']*MK['qq']))-1) % N2
tmp = integer(tmp) / N
a = tmp * integer(k_1) % N

tmp = (int(ciphertext['A']**(MK['pp']*MK['qq']))-1) % N2
tmp = integer(tmp) / N
r = tmp * integer(k_1) % N

gama = a*r % N
sig = ((MK['pp']*MK['qq'])%N)**-1

tmp = (g**-1)**gama
tmp = ciphertext['B'] *tmp
tmp = (int(tmp**(MK['pp']*MK['qq']))-1) % N2
tmp = integer(tmp) / N

m = integer(tmp) * integer(sig) %N
m = integer(m)
print(m)