# -*- coding: utf-8 -*- 

import Tkinter as tk
import tkFileDialog
import pandas as pd
import pickle
import tkMessageBox
from save_model import save_model
from train_gui import train_svm,train_lr,train_cart
from fed_gui import fed_integrate_model_svm,fed_integrate_model_cart,fed_integrate_model_lr
from sklearn.metrics import accuracy_score

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

para_dict = {}

window = tk.Tk()
mode = tk.IntVar()
loc = tk.StringVar()
window.title('联邦学习测试系统')
window.geometry('500x500')

def load_file(file_loc):
    with open(file_loc) as f:
        data = pd.read_csv(f)
    return data

def open_file():
    filename = tkFileDialog.askopenfilename(title='打开数据集文件', filetypes=[('csv', '*.csv')])
    loc.set(filename)
    label_1.config(text = '数据集文件: ' + filename)
    with open(filename) as f:
        data = pd.read_csv(f)
    data_num = data.shape[0]
    tkMessageBox.showinfo(title = '提示', message = '已成功读入'+str(data_num)+'条数据！')
    return filename

def train_model():
    data = load_file(loc.get())
    #label_1.config(text = mode.get())
    if mode.get() == 0:
        result_coef = train_svm(data)
    elif mode.get() == 1:
        result_coef = train_cart(data)
    else:
        result_coef = train_lr(data)
    label_1.config(text = '准确率为: '+str(result_coef[0]))
    para_dict['result'] = result_coef
    save_model(result_coef[1],'model_B.pickle')

def integrate_model():
    with open("model_A.pickle","rb") as f:
        model_A = pickle.load(f)
    with open("model_B.pickle","rb") as f:
        model_B = pickle.load(f)
    if mode.get() == 0:
        test_data = pd.read_csv('test_svm.csv') 
        inte_model = fed_integrate_model_svm(model_A,model_B)
        print test_data.head(6)
    elif mode.get() == 1:
        test_data = pd.read_csv('test_cart.csv') 
        inte_model = fed_integrate_model_cart(model_A,model_B)
    else:
        test_data = pd.read_csv('test_lr.csv') 
        inte_model = fed_integrate_model_lr(model_A,model_B)
        
    x_test=test_data.iloc[:,:-1].drop('Unnamed: 0',axis=1)
    # print x_test.columns
    # print x_test.shape
    y_test=test_data.iloc[:,-1]
    y_pre=inte_model.predict(x_test)
    # print y_test
    # print y_pre
    label_1.config(text = '准确率为: '+str(accuracy_score(y_pre,y_test)))
        
    

tk.Label(window,text = '欢迎使用联邦学习系统').pack()

button_1 = tk.Button(window, text="导入文件",command=open_file)
button_1.pack()

tk.Label(window, text = '\n').pack()

tk.Label(window,text = '请选择所使用的机器学习算法：').pack()
radio_1 = tk.Radiobutton(window, text = 'SVM', variable = mode, value = 0)
radio_1.pack()
radio_2 = tk.Radiobutton(window, text = 'CART', variable = mode, value = 1)
radio_2.pack()
radio_3 = tk.Radiobutton(window, text = 'LR', variable = mode, value = 2)
radio_3.pack()

button_2 = tk.Button(window, text = "训练模型", command=train_model)
button_2.pack()

tk.Label(window, text = '\n').pack()

button_3 = tk.Button(window, text = "聚合模型", command=integrate_model)
button_3.pack()

tk.Label(window, text = '\n').pack()

label_1 = tk.Label(window, bg = 'grey', text = '\n', width = 45, height = 4)
label_1.pack()


window.mainloop()