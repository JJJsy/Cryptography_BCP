#################################################  
# svm: support vector machine  
# Author :   
# Date   :   
# HomePage :
# Email  :  
#################################################  
  
from numpy import *
from SVM import *  
import svm  
  
################## test svm #####################  
## step 1: load data  
print ("step 1: load data...")  
dataSet = []  
labels = []  
fileIn = open('testSet.txt')  
for line in fileIn.readlines():  
	lineArr = line.strip().split('\t')  
	dataSet.append([float(lineArr[0]), float(lineArr[1])])  
	labels.append(float(lineArr[2]))  
#transfer the data to matrix.
dataSet = mat(dataSet)  
labels = mat(labels).T 
#choose the first 80 samples of testset.txt as the training set, and the last is test set.  
train_x = dataSet[0:81, :]  
train_y = labels[0:81, :]  
test_x = dataSet[80:101, :]  
test_y = labels[80:101, :] 

  
## step 2: training...  
print ("step 2: training..." ) 
C = 0.6  
toler = 0.001  
maxIter = 50  
svmClassifier = svm.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0))  
  
## step 3: testing  
print ("step 3: testing..." ) 
accuracy = svm.testSVM(svmClassifier, test_x, test_y)  
  
## step 4: show the result  
print ("step 4: show the result...")    
print ('The classify accuracy is: %.3f%%' % (accuracy * 100) )
show()
#svm.showSVM(svmClassifier)  
