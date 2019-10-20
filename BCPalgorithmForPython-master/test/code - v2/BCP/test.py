#!/usr/bin/env python
# coding=utf-8
from BCPEncrypt.BCP import *
from BCPEncrypt.KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize
import random

######            setup                #####
keyGen(secparam = 1024,paramPath = 'BCPEncrypt/param',mkPath = 'BCPEncrypt/mk')
MK = readMKFromFile(mkPath = 'BCPEncrypt/mk')
############################################

##### get BCP context and generate pk,sk#####
########################################
bcp = genBCPContext(paramPath = 'BCPEncrypt/param')
param=readParamFromFile(paramPath='BCPEncrypt/param')
N=param.N
print "N=",N
pk,sk = genKeyPair(bcp,keyPairPath = 'keyPair')
pk1,sk1=genKeyPair(bcp,keyPairPath='keyPair1')
#next time directly read pk,sk from file
#pk,sk = readKeyPairFromFile(keyPairPath = 'BCPEncrypt/keyPair')
# print pk,sk
#############################################

######            Encrypt               #####
#############################################
ciphertext1 = bcp.Encrypt(pk, 12)
ciphertext2 = bcp.Encrypt(pk, 18)
ciphertext3=bcp.Encrypt(pk1,13)
print ciphertext1 #print two line ciphertext
############################################

######       Decrypt with sk            #####
#############################################
m = bcp.Decrypt(ciphertext1,sk)
m1=bcp.Decrypt(ciphertext3,sk1)
print m # m = 12
print m1
r1=random.randint(1,100)
print r1

############################################

#####        Decrypt with MK            #####
#############################################
m = bcp.DecryptMK(ciphertext1,MK,pk)
print m # m =12
#############################################

#####           Computation             #####
############################################
ciphertext3 = bcp.multiply(ciphertext1, ciphertext2)
print bcp.Decrypt(ciphertext3,sk) # 12+18 =30
#cihpertext3=bcp.exponentiate(ciphertext3,2)#30*2=60
N1=N-1
ciphertext3 = bcp.exponentiate(ciphertext1,N1)
ciphertext3=bcp.multiply(ciphertext2,ciphertext3)
print  bcp.Decrypt(ciphertext3,sk)
# 30 * 2 = 60

#ciphertext3=bcp.exponentiate(ciphertext3,ciphertext3)
#print bcp.Decrypt(ciphertext3,sk)
###########################################
