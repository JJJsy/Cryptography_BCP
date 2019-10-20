'''
@Descripttion: 本文件分为2个实验，实验一：验证若干个SVM模型参数聚合的结果
               实验二：在实验一的基础上增加多密钥功能。
@version: V1.0
@Author: HuiKwok
@Date: 2019-10-09 01:43:53
@LastEditors: HuiKwok
@LastEditTime: 2019-10-09 07:42:19
'''
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import numpy as np
import MulKeysAdd as mlk

# 实验一

## 加载数据

iris = load_iris()
features = iris.data
target = iris.target
# print(type(features))
# print(features.shape)
# print(type(target))
# print(target.shape)
x_train,x_test,y_train,y_test = train_test_split(features,target,test_size = 0.6,random_state = 10)
model = LinearSVC()
model.fit(x_train,y_train)
print("model's coefficient:",model.coef_)
# print(type(model.coef_))
print("model's intercept:",model.intercept_)
# print(type(model.intercept_))
print("model's classes:",model.classes_)
# print(type(model.classes_))
y_predict = model.predict(x_test)
score = accuracy_score(y_test,y_predict)
print("model's accuracy score:",score)
print("######################################")
print("######################################")

## 训练两个SVM模型，对这两个SVM模型的参数进行聚合
x_train_1,x_test_1,y_train_1,y_test_1 = train_test_split(features,target,test_size = 0.8,random_state = 3)
model_1 = LinearSVC()
model_1.fit(x_train_1,y_train_1)
score1 = accuracy_score(y_test,model_1.predict(x_test))
print("model_1's coefficient:",model_1.coef_)
print("model_1's intercept:",model_1.intercept_)
print("model_1's classes:",model_1.classes_)
print("model_1's accuracy score:",score1)

print("######################################")
print("######################################")

x_train_2,x_test_2,y_train_2,y_test_2 = train_test_split(features,target,test_size = 0.8,random_state =100)
model_2 = LinearSVC()
model_2.fit(x_train_2,y_train_2)
score2 = accuracy_score(y_test,model_2.predict(x_test))
print("model_2's coefficient:",model_2.coef_)
print("model_2's intercept:",model_2.intercept_)
print("model_2's classes:",model_2.classes_)
print("model_2's accuracy score:",score2)
print("######################################")
print("######################################")


## 构建聚合后的模型
new_coef = (model_1.coef_+model_2.coef_)/2
new_intercept = (model_1.intercept_+model_2.intercept_)/2
classes = model_1.classes_

model_integrate = LinearSVC()
model_integrate.coef_ = new_coef
model_integrate.intercept_ = new_intercept
model_integrate.classes_ = classes
score3 = accuracy_score(y_test,model_integrate.predict(x_test))
print("model_intg's coefficient:",model_integrate.coef_)
print("model_intg's intercept:",model_integrate.intercept_)
print("model_intg's classes:",model_integrate.classes_)
print("model_intg's accuracy score:",score3)
print("######################################")
print("######################################")

