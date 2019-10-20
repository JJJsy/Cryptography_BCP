'''
@Descripttion: 根据孙文礼师兄的代码，重写了python3下bcp算法的代码。主要改动是在一些地方加了强转，使其可以在charm0.43下运行
@version: V1.1
@Author: HuiKwok
@Date: 2019-09-21 02:42:58
@LastEditors: Please set LastEditors
@LastEditTime: 2019-10-11 06:35:31
'''

from charm.toolbox.integergroup import IntegerGroup
from charm.schemes.pkenc.pkenc_rsa import RSA_Enc, RSA_Sig
from charm.core.math.integer import integer,randomBits,random,randomPrime,isPrime,encode,decode,hashInt,bitsize,legendre,gcd,lcm,serialize,deserialize,int2Bytes,toInt


class Param():
    def __init__(self):
        pass
    def setParam(self,N2,N,g,k):
        self.N2 = N2
        self.N = N
        self.g = g
        self.k = k

class BCP():
    def __init__(self,secparam=1024,param = None):
        if param:
            self.N2 = param.N2
            self.N = param.N
            self.g = param.g
            self.k = param.k            
        else:
            self.p, self.q = randomPrime(int(secparam/2),True), randomPrime(int(secparam/2),True) 
            self.pp = (self.p -1)/2
            self.qq = (self.q - 1)/2
            self.N = self.p * self.q
            while True: # choose a good N
                if bitsize(self.N) ==secparam and len(int2Bytes(self.N)) == int(secparam/8) and int2Bytes(self.N)[0] &128 !=0:
                    break
                self.p, self.q = randomPrime(int(secparam/2),True), randomPrime(int(secparam/2),True) 
                self.pp = (self.p -1)/2
                self.qq = (self.q - 1)/2
                self.N = self.p * self.q
            self.N2 = self.N**2
            self.g = random(self.N2)
            one = integer(1)% self.N2
            while True: #choose a good g
                self.g = random(self.N2)
                self.g = integer((int(self.g)-1)*(int(self.g)-1))% self.N2
                if self.g == one:
                    continue
                tmp = self.g**self.p %self.N2
                if tmp == one:
                    continue
                tmp = self.g**self.pp % self.N2
                if tmp == one:
                    continue
                tmp = self.g**self.q %self.N2
                if tmp == one:
                    continue
                tmp = self.g**self.qq %self.N2
                if tmp == one:
                    continue
                tmp =self.g**(self.p*self.pp) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.p*self.q) %self. N2
                if tmp== one:
                    continue 
                tmp = self.g**(self.p*self.qq) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.pp*self.q) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.pp*self.qq) % self.N2
                if tmp == one:
                    continue 
                tmp = self.g**(self.q*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp = self.g**(self.q*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp = self.g**(self.p*self.pp*self.q) % self.N2
                if tmp == one:
                    continue   
                tmp =self.g**(self.p*self.pp*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp =self.g**(self.p*self.q*self.qq) % self.N2
                if tmp == one:
                    continue
                tmp =self.g**(self.pp*self.q*self.qq) % self.N2
                if tmp == one:
                    continue  
                break 
            self.k = integer((int(self.g**(self.pp*self.qq)) - 1)) / self.N % self.N
            self.MK ={"pp":self.pp,"qq":self.qq}
    
    def GetMK(self):
        return self.MK
    
    def GetParam(self):                         
        param = Param()
        param.setParam(self.N2, self.N, self.g, self.k)
        return param
    
    def KeyGen(self):                           #公私钥生成
        tmp = self.N2 /2
        sk = random(tmp) % self.N2
        pk = (self.g**sk) % self.N2
        return pk,sk
    
    def Encrypt(self,pk,plaintext):             #公钥加密
        r = random(self.N/4) % self.N2
        A = (self.g** r ) % self.N2 
        B1 = (self.N*plaintext+1)% (self.N2)
        B2 = (pk**r) % (self.N2)
        B = B1*B2 % self.N2
        ciphertext = {"A":A,"B":B}
        return ciphertext
    
    def Decrypt(self,ciphertext,sk):            #私钥解密
        t1 = integer(int(ciphertext['B']*((ciphertext['A']**-1)**sk)) -1) % self.N2
        m = integer(t1) / self.N
        return m
    
    def DecryptMK(self,ciphertext,MK,pk):       #主密钥解密
        k_1 = self.k ** -1
        tmp = (int(pk**(MK['pp']*MK['qq'])) -1) % self.N2
        tmp = integer(tmp) /self.N 
        a = tmp * integer(k_1) % self.N
        
        tmp = (int(ciphertext['A'] **(MK['pp']*MK['qq'])) -1) % self.N2
        tmp = integer(tmp) /self.N 
        r = tmp * integer(k_1) % self.N
        
        gama = a*r %self.N
        sig = ((MK['pp']*MK['qq'])%self.N) **-1
        
        tmp = (self.g **-1)**gama
        tmp = ciphertext['B'] *tmp    
        tmp = (int(tmp**(MK['pp']*MK['qq'])) -1)% self.N2
        tmp = integer(tmp) /self.N
        
        m = integer(tmp) * integer(sig) %self.N
        return integer(m) 

    def multiply(self,ciphertext1,ciphertext2):
        ciphertext={}
        ciphertext['A'] = ciphertext1['A'] * ciphertext2['A']
        ciphertext['B'] = ciphertext1['B'] * ciphertext2['B'] 
        return ciphertext

    def exponentiate(self,ciphertext,m):
        text={}    
        text['A'] = ciphertext['A'] **m % self.N2
        text['B'] = ciphertext['B'] **m % self.N2
        return text  
  



if __name__ == "__main__":
    bcp = BCP()
    mk = bcp.GetMK()
    param = bcp.GetParam()
    pk,sk = bcp.KeyGen()

    plaintext = 1024
    ciphertext = bcp.Encrypt(pk,plaintext)
    # 用自己的私钥解密
    m1 = bcp.Decrypt(ciphertext,sk)
    print(m1)
    # 用主密钥解密
    m2 = bcp.DecryptMK(ciphertext,mk,pk)
    print(m2)