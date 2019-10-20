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
file=open('data1','w')
for i in range(1,1000):
  file.write(str(20))
  file.write("\n")
file.close()
###################
