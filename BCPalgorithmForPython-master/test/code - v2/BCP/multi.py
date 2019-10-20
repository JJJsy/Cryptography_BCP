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
pk1,sk1=genKeyPair(bcp,keyPairPath='keyPair')
pk2,sk2=genKeyPair(bcp,keyPairPath='keyPair1')
pk3,sk3=genKeyPair(bcp,keyPairPath='keyPair2')
#next time directly read pk,sk from file
#pk,sk = readKeyPairFromFile(keyPairPath = 'BCPEncrypt/keyPair')
# print pk,sk
#############################################

######            Encrypt               #####
#############################################
def multi(m1,m2):
 ciphertext1 = bcp.Encrypt(pk1, m1)
 r1=random.randint(1,100)
# print'm1=',m1
# print'r1=',r1
 ciphertext2 = bcp.Encrypt(pk1, r1)
 ciphertext3 = bcp.multiply(ciphertext1, ciphertext2)
 m3=bcp.DecryptMK(ciphertext3,MK,pk1) # 12+r1
# print'm1+r1=',m3
 ciphertext3=bcp.Encrypt(pk3,m3)
#########################################
 ciphertext4=bcp.Encrypt(pk2,m2)
 r2=random.randint(1,100)
# print'm2=',m2
# print'r2=',r2
 ciphertext5=bcp.Encrypt(pk2,r2)
 ciphertext6=bcp.multiply(ciphertext4,ciphertext5)#13+r2
 m4=bcp.DecryptMK(ciphertext6,MK,pk2)
# print'm2+r2=',m4
 ciphertext6=bcp.Encrypt(pk3,m4)
###########################################
 m5=m3*m4
 ciphertext7=bcp.Encrypt(pk3,m5)
 ciphertext8=bcp.exponentiate(ciphertext1,N-r2)
 temp=bcp.DecryptMK(ciphertext8,MK,pk1)
 ciphertext8=bcp.Encrypt(pk3,temp)
 ciphertext9=bcp.exponentiate(ciphertext4,N-r1)
 temp=bcp.DecryptMK(ciphertext9,MK,pk2)
 ciphertext9=bcp.Encrypt(pk3,temp)
 ciphertext10=bcp.Encrypt(pk3,r1*r2)
 ciphertext7=bcp.multiply(ciphertext7,ciphertext8)
 ciphertext7=bcp.multiply(ciphertext7,ciphertext9)
 ciphertext10=bcp.exponentiate(ciphertext10,N-1)
 ciphertext7=bcp.multiply(ciphertext7,ciphertext10)
 m=bcp.Decrypt(ciphertext7,sk3)
# print'm1*m2=',m
 return m
 #print'\n'
 #print'The time of multi is:',time.clock()-start
 #f.close()
#ciphertext3=bcp.exponentiate(ciphertext3,ciphertext3)
#print bcp.Decrypt(ciphertext3,sk)
###########################################

