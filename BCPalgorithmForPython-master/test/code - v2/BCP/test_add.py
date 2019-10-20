#!/usr/bin/env python
# coding=utf-8
from BCPEncrypt.BCP import *
from BCPEncrypt.KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize
import random
import time
######            setup                #####
keyGen(secparam = 1024,paramPath = 'BCPEncrypt/param',mkPath = 'BCPEncrypt/mk')
MK = readMKFromFile(mkPath = 'BCPEncrypt/mk')
############################################

##### get BCP context and generate pk,sk#####
########################################
bcp = genBCPContext(paramPath = 'BCPEncrypt/param')
pa=readParamFromFile(paramPath='BCPEncrypt/param')
N=pa.N
print bitsize(N)
pk1,sk1=genKeyPair(bcp,keyPairPath='keyPair')
pk2,sk2=genKeyPair(bcp,keyPairPath='keyPair1')
pk3,sk3=genKeyPair(bcp,keyPairPath='keyPair2')
#next time directly read pk,sk from file
#pk,sk = readKeyPairFromFile(keyPairPath = 'BCPEncrypt/keyPair')
# print pk,sk
#############################################

######            Encrypt               #####
#############################################
f=open('data')
lines=f.readlines()
L=len(lines)
#print lines[2]
i=0
start=time.clock()
while i<L:
 m1=int(lines[i])
 i+=1
 if i<L:
   m2=int(lines[i])
 else:
   m2=m1
 i+=1
 print 'm1=',m1
 print 'm2=',m2
 print'The original m1+m2=',m1+m2
 ciphertext1 = bcp.Encrypt(pk1, m1)
 r1=random.randint(1,100)
 #print'm1=',m1
 #print'r1=',r1
 ciphertext2 = bcp.Encrypt(pk1, r1)
 ciphertext3 = bcp.multiply(ciphertext1, ciphertext2)
 m=bcp.Decrypt(ciphertext3,sk1) # 12+r1
 #print'm1+r1=',m1
#########################################
 ciphertext4=bcp.Encrypt(pk2,m2)
 r2=random.randint(1,100)
# print'm2=',m2
# print'r2=',r2
 ciphertext5=bcp.Encrypt(pk2,r2)
 ciphertext6=bcp.multiply(ciphertext4,ciphertext5)#13+r2
 m=bcp.Decrypt(ciphertext6,sk2)
 #print'm2+r2=',m
###########################################
 m1=bcp.DecryptMK(ciphertext3,MK,pk1)
 ciphertext3=bcp.Encrypt(pk3,m1)
 m2=bcp.DecryptMK(ciphertext6,MK,pk2)
 ciphertext6=bcp.Encrypt(pk3,m2)
################################################
 ciphertext2=bcp.Encrypt(pk3,r1)
 ciphertext5=bcp.Encrypt(pk3,r2)
 ciphertext7=bcp.multiply(ciphertext2,ciphertext5)
 ciphertext7=bcp.exponentiate(ciphertext7,N-1)
 ciphertext8=bcp.multiply(ciphertext3,ciphertext6)
 ciphertext8=bcp.multiply(ciphertext8,ciphertext7)
 m=bcp.Decrypt(ciphertext8,sk3)
 print'After decryption,m1+m2=',m
 print'\n'
print'The time of add is:',time.clock()-start
f.close()
#ciphertext3=bcp.exponentiate(ciphertext3,ciphertext3)
#print bcp.Decrypt(ciphertext3,sk)
###########################################

