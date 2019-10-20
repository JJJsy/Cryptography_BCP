from BCPEncrypt.BCP import *
from BCPEncrypt.KeyGenAndRead import *
from add import *
from multi import *
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
pk1,sk1=genKeyPair(bcp,keyPairPath = 'keyPair')
pk2,sk2=genKeyPair(bcp,keyPairPath='keyPair1')
#next time directly read pk,sk from file
#pk,sk = readKeyPairFromFile(keyPairPath = 'BCPEncrypt/keyPair')
# print pk,sk
#############################################

######            Encrypt               #####
#############################################
m1=[1,4]
m2=[3,2]
#print m1[0]
#print m2[1]
m3=int(multi(m1[0],m2[0]))
m4=int(multi(m1[1],m2[1]))
print(float(m3)/m4)
#print multi(m1[1],m2[0])
'''
f=open('data')
file=open('Cipher_Enc','w')
lines=f.readlines()
L=len(lines)
#print lines[2]
start=time.clock()
i=0
while i<L:
 m1=int(lines[i])
 i+=1
 if i>=L:
   break
 print'The original data is:',m1
 ciphertext1 = bcp.Encrypt(pk, m1)
 file.write(serialize(ciphertext1['A'])+'\n')
 file.write(serialize(ciphertext1['B']))
 #print ciphertext1
 m=bcp.Decrypt(ciphertext1,sk)
 print'After decryption, the data is:', m
 m2=bcp.DecryptMK(ciphertext1,MK,pk)
 print 'After Decryption by MK, the data is:',m2
 print'\n'
print'The time of computation is:',time.clock()-start
f.close()
file.close()
'''
