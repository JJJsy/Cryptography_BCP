# -*- coding: utf-8 -*- 
'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-20 15:08:08
@LastEditTime: 2019-10-20 15:08:08
@LastEditors: your name
'''
def save_model(clf,name):
    import pickle #pickle模块
    #保存Model(注:save文件夹要预先建立，否则会报错)
    with open(name, 'wb') as f:
        pickle.dump(clf, f)

#     #读取Model
#     with open('clf.pickle', 'rb') as f:
#         clf2 = pickle.load(f)
#         #测试读取后的Model
#         print(clf2.predict(X))