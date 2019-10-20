# coding=utf-8
'''
'''
import time
from BCP import *
from KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize
print 'begin()'

# start = time.clock()
# keyGen()
# print 'generator done, cost %s seconds',time.clock() - start

start = time.clock()
bcp = genBCPContext(paramPath = 'param')
# pk,sk = genKeyPair(bcp, keyPairPath = 'keyPair')

pk,sk = readKeyPairFromFile(keyPairPath = 'keyPair')

ciphertext1 = bcp.Encrypt(pk, 12)
file=open('Cipher','w')
file.write(serialize(ciphertext1['A']))
#file.write(serialize(ciphertext1['A'])+'\n'+'\n')
file.write(serialize(ciphertext1['B']))
ciphertext2 = bcp.Encrypt(pk, 18)
#for index in range(1000):
ciphertext1 = bcp.multiply(ciphertext1,ciphertext2)
m = bcp.Decrypt(ciphertext1,sk)
print 'm is ',m
print 'generator done, cost %s seconds'%(time.clock() - start)
start1=time.clock()
pk,sk=genKeyPair(bcp,keyPairPath='keyPair')
print 'The time of generate keypair is: %s'%(time.clock()-start1)
start2=time.clock()
bcp=BCP(1024)
mk=bcp.GetMK()
print 'The time of generate Mainkey is: %s'%(time.clock()-start2)
