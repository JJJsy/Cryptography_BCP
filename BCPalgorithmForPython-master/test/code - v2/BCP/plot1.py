import numpy as np
import matplotlib.pyplot as plt
 
N = 5
y1 = [20, 10, 30, 25, 15]
y2 = [15, 14, 34 ,10,5]
#index = np.arange(5)
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#t=np.arange(0.,5.,0.2)
#plt.plot(t,t,'r-',t,t**2,'bs',t,t**3,'g^')
#x=np.arange(0,11000,1000)
xmajorLocator=MultipleLocator(1500)
xmajorFormatter=FormatStrFormatter('%5.1f')
xminorLocator=MultipleLocator(500)


ymajorLocator=MultipleLocator(1)
ymajorFormatter=FormatStrFormatter('%1.1f')
yminorLocator=MultipleLocator(0.5)

ymajorLocator1=MultipleLocator(4)
ymajorFormatter1=FormatStrFormatter('%1.1f')
yminorLocator1=MultipleLocator(2)

ymajorLocator2=MultipleLocator(7)
ymajorFormatter2=FormatStrFormatter('%1.1f')
yminorLocator2=MultipleLocator(5)

###########################################
plt.figure(1)
ax=plt.subplot(221)
x=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000]
y=[1.01,1.95,2.83,3.57,4.22,4.93,5.88,6.47,7.32,7.88,8.69]
#xlim(0,12000)
#ylim(0,10)
#plt.plot(x,y,'g^',x,y1,'bs')
#plot(x,y,'g^--')
#ax.bar(x,y,width=0.3,color='b')
'''
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)


ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='minor')
ax.set_xlabel("Data Size(Bytes)")
ax.set_ylabel("Time Consumption(Seconds)")
'''
#index=[1,2,3,4,5]
 
#bar_width = 0.3
ax.bar(x, y, width=0.1 , color='y')

plt.show()
