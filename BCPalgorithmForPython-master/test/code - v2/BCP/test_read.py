from BCPEncrypt.BCP import *
from BCPEncrypt.KeyGenAndRead import *
from charm.core.math.integer import serialize,deserialize
import random

######            setup                #####
keyGen(secparam = 1024,paramPath = 'BCPEncrypt/param',mkPath = 'BCPEncrypt/mk')
MK = readMKFromFile(mkPath = 'BCPEncrypt/mk')
#with open('data')as f:
f=open('data')
lines=f.readlines()
L=len(lines)
#print lines[2]
i=0
while i<L:
 m=int(lines[i])
 i+=1
 if i<L:
   m1=int(lines[i])
 else:
   m1=m
 i+=1
 print m
 print m1
#for line in lines:
  # m1=int(line)
  # print m1
f.close()
############################################


