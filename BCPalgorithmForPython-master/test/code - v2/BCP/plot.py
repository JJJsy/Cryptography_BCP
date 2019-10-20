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
xlim(0,12000)
ylim(0,10)
#plt.plot(x,y,'g^',x,y1,'bs')
#plot(x,y,'g^--')
ax.bar(x,y,width=0.3,color='b')
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
#ax.show()
##########################################
ax1=plt.subplot(222)
x1=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000]
y1=[1.03,1.96,2.81,3.78,4.42,5.08,5.88,6.44,7.33,7.99,8.70]
xlim(0,12000)
ylim(0,10)
plot(x1,y1,'bs-.')
ax1.xaxis.set_major_locator(xmajorLocator)
ax1.xaxis.set_major_formatter(xmajorFormatter)

ax1.yaxis.set_major_locator(ymajorLocator)
ax1.yaxis.set_major_formatter(ymajorFormatter)


ax1.xaxis.set_minor_locator(xminorLocator)
ax1.yaxis.set_minor_locator(yminorLocator)

ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='minor')
ax1.set_xlabel("Data Size(Bytes)")
ax1.set_ylabel("Time Consumption(Seconds)")
################################
ax3=plt.subplot(223)
x1=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000]
y1=[4.2,7.9,11.72,14.54,17.76,20.21,24.09,25.94,29.53,32.66,34.75]
xlim(0,12000)
ylim(0,38)
plot(x1,y1,'cD:')
ax3.xaxis.set_major_locator(xmajorLocator)
ax3.xaxis.set_major_formatter(xmajorFormatter)

ax3.yaxis.set_major_locator(ymajorLocator1)
ax3.yaxis.set_major_formatter(ymajorFormatter1)


ax3.xaxis.set_minor_locator(xminorLocator)
ax3.yaxis.set_minor_locator(yminorLocator1)

ax3.xaxis.grid(True, which='major')
ax3.yaxis.grid(True, which='minor')
ax3.set_xlabel("Data Size(Bytes)")
ax3.set_ylabel("Time Consumption(Seconds)")
###########################################
ax4=plt.subplot(224)
x1=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000]
y1=[7.35,14.08,20.6,26.09,31.0,35.87,42.1,46.49,52.57,57.11,62.39]
xlim(0,12000)
ylim(0,65)
plot(x1,y1,'rh-')
ax4.xaxis.set_major_locator(xmajorLocator)
ax4.xaxis.set_major_formatter(xmajorFormatter)

ax4.yaxis.set_major_locator(ymajorLocator2)
ax4.yaxis.set_major_formatter(ymajorFormatter2)


ax4.xaxis.set_minor_locator(xminorLocator)
ax4.yaxis.set_minor_locator(yminorLocator2)

ax4.xaxis.grid(True, which='major')
ax4.yaxis.grid(True, which='minor')
ax4.set_xlabel("Data Size(Bytes)")
ax4.set_ylabel("Time Consumption(Seconds)")

plt.show()
