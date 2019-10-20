# -*- coding: UTF-8 -*-
import sys   
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np

import matplotlib.pyplot as plt
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei']  
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
xmajorLocator=MultipleLocator(1.5)
xmajorFormatter=FormatStrFormatter('%1.1f')
xminorLocator=MultipleLocator(1)


#ymajorLocator=MultipleLocator(1)
#ymajorFormatter=FormatStrFormatter('%1.1f')
#yminorLocator=MultipleLocator(0.5)

ymajorLocator=MultipleLocator(2)
ymajorFormatter=FormatStrFormatter('%1.1f')
yminorLocator=MultipleLocator(1)

plt.figure(1)
'''
#ax=plt.subplot(131)
ax=plt.subplot(111)
#x_list=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
x_list1=[10,20,30,40,50,60,70,80,90,100]
x_list2=[8,18,28,38,48,58,68,78,88,98]
#y_list=[1.01,1.95,2.83,3.57,4.22,4.93,5.88,6.47,7.32,7.88]
y_list=[2.42,3.96,4.68,6.02,7.84,8.53,9.42,10.42,11.89,13.52]
y_list1=[26.03,41.34,56.61,72.42,87.67,101.16,118.12,133.36,148.12,164.11]
#plt.ylim([0.5,9])
#plt.ylim([2,165])
#plt.bar(range(10) , y_list,color='lawngreen',label='one')
#plt.bar(x_list1,y_list,width=2,color='red',label='Our Scheme')
plt.bar(x_list1,y_list,width=2,color='red',label='我们的方案')
#plt.bar(range(10), y_list1,color='purple',label='two')
plt.bar(x_list2,y_list1,width=2,color='purple',label='论文[10]的方案')
plt.legend()
#plt.xticks(range(10),['10','20','30','40','50','60','70','80','90','100'])
#ax.xaxis.set_major_locator(xmajorLocator)
#ax.xaxis.set_major_formatter(xmajorFormatter)

#ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)


ax.xaxis.set_minor_locator(xminorLocator)
#ax.yaxis.set_minor_locator(yminorLocator)

#ax.xaxis.grid(True, which='major',ls='-.')

ax.yaxis.grid(True, ls='-.')

#plt.grid(grid_linstyle='-.')
#ax.set_xlabel("Data Size (100 Bytes)")
ax.set_xlabel("数据大小 (100 Bytes)")
#ax.set_ylabel("Time Consumption (Seconds)")
ax.set_ylabel("时间(s)")
#plt.bar(range(1) , y_list, color='r')
#plt.xticks(range(11),['1000','2000','3000','4000','5000','6000','7000','8000','9000','10000','11000'])
#plt.grid(alpha=0.3)
'''
##############################################################
#ax1=plt.subplot(132)
ax1=plt.subplot(111)
x1=[10,20,30,40,50,60,70,80,90,100]
x2=[8,18,28,38,48,58,68,78,88,98]
#y1=[1.03,1.96,2.81,3.78,4.42,5.08,5.88,6.44,7.33,7.99]
y1=[2.13,3.98,4.51,5.89,6.85,7.79,8.93,10.94,11.72,13.11]
y2=[24.10,40.18,55.58,71.38,86.65,100.14,117.12,132.34,146.21,163.12]
#xlim(0,12000)
#ylim(0,10)
#plot(x1,y1,'bs-.')

#plt.ylim([0.5,9])

#plt.bar(range(10) , y1, color='purple')
#plt.xticks(range(10),['10','20','30','40','50','60','70','80','90','100'])

#ax1.xaxis.set_major_locator(xmajorLocator)
#ax1.xaxis.set_major_formatter(xmajorFormatter)

#ax1.yaxis.set_major_locator(ymajorLocator)
ax1.yaxis.set_major_formatter(ymajorFormatter)


ax1.xaxis.set_minor_locator(xminorLocator)
#ax1.yaxis.set_minor_locator(yminorLocator)

#ax1.xaxis.grid(True, which='major',ls='-.')
#ax1.yaxis.grid(True, which='minor',ls='-.')
ax1.yaxis.grid(True,ls='-.')
#plt.bar(range(10) , y1, color='purple')
plt.bar(x1,y1,width=2,color='lawngreen',label='The Scheme of this Paper')
plt.bar(x2,y2,width=2,color='blue',label='The scheme of [10]')
plt.legend()
ax1.set_xlabel('Data size (100 Bytes)')
ax1.set_ylabel('Time consume (s)')
##############################################
#'''
'''
#ax1=plt.subplot(133)
ax1=plt.subplot(111)
x1=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
y1=[2.04,3.96,5.51,7.48,8.61,10.17,11.73,13.10,14.49,16.14]
#xlim(0,12000)
#ylim(0,10)
#plot(x1,y1,'bs-.')
plt.ylim([0.5,17])
#plt.bar(range(10) , y1, color='purple')
plt.xticks(range(10),['10','20','30','40','50','60','70','80','90','100'])

#ax1.xaxis.set_major_locator(xmajorLocator)
#ax1.xaxis.set_major_formatter(xmajorFormatter)

ax1.yaxis.set_major_locator(ymajorLocator)
ax1.yaxis.set_major_formatter(ymajorFormatter)


ax1.xaxis.set_minor_locator(xminorLocator)
ax1.yaxis.set_minor_locator(yminorLocator)

#ax1.xaxis.grid(True, which='major',ls='-.')
ax1.yaxis.grid(True, which='minor',ls='-.')
plt.bar(range(10) , y1, color='orangered')
jorLocator=MultipleLocator(1)
ymajorFormatter=FormatStrFormatter('%1.1f')
yminorLocator=MultipleLocator(0.5)

'''
#'''
#plt.tick_params(labelsize=7)
#labels = ax.get_xticklabels() + ax.get_yticklabels()
#[label.set_fontname('Times New Roman') for label in labels]



#font2 = {'family' : 'Times New Roman','weight' : 'normal','size'   : 5,}
#plt.xlabel('round',font2)

#ax1.set_xlabel("Data Size (100 Bytes)")
#ax1.set_ylabel("Time Consumption (Seconds)")

plt.show()
