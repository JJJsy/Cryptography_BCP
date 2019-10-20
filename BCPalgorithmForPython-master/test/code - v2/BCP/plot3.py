import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#t=np.arange(0.,5.,0.2)
#plt.plot(t,t,'r-',t,t**2,'bs',t,t**3,'g^')
#x=np.arange(0,11000,1000)
xmajorLocator=MultipleLocator(10)
xmajorFormatter=FormatStrFormatter('%1i')
xminorLocator=MultipleLocator(5)


ymajorLocator=MultipleLocator(1)
ymajorFormatter=FormatStrFormatter('%1.1f')
yminorLocator=MultipleLocator(0.5)

ymajorLocator1=MultipleLocator(4)
ymajorFormatter1=FormatStrFormatter('%1.1f')
yminorLocator1=MultipleLocator(2)

#ymajorLocator2=MultipleLocator(6)
ymajorLocator2=MultipleLocator(16)
ymajorFormatter2=FormatStrFormatter('%1.1f')
#yminorLocator2=MultipleLocator(3)
yminorLocator2=MultipleLocator(8)

###########################################
plt.figure(1)
'''
#ax3=plt.subplot(121)
ax3=plt.subplot(111)
x1=[10,20,30,40,50,60,70,80,90,100,110]
y1=[4.2,7.9,11.72,14.54,17.76,20.21,24.09,25.94,29.53,32.66,34.75]
y2=[5,9,16,18,19,20,25,31,32,34,38]
xlim(0,110)
#ylim(0,36)
ylim(0,40)
plot(x1,y1,'rh-',label='The Scheme of this Paper')
plot(x1,y2,'cD:',label='The Scheme of [10]')
plt.legend()
ax3.xaxis.set_major_locator(xmajorLocator)
ax3.xaxis.set_major_formatter(xmajorFormatter)

ax3.yaxis.set_major_locator(ymajorLocator1)
ax3.yaxis.set_major_formatter(ymajorFormatter1)


ax3.xaxis.set_minor_locator(xminorLocator)
ax3.yaxis.set_minor_locator(yminorLocator1)

ax3.xaxis.grid(True, which='major',ls='-.')
ax3.yaxis.grid(True, which='minor',ls='-')
ax3.set_xlabel("Data Size (100 Bytes)")
ax3.set_ylabel("Time Consumption (Seconds)")
###########################################
'''
#ax4=plt.subplot(122)
ax4=plt.subplot(111)
x1=[10,20,30,40,50,60,70,80,90,100,110]
y1=[7.35,14.08,20.6,26.09,31.0,35.87,42.1,46.49,52.57,57.11,62.39]
y2=[25.67,41.39,56.85,72.26,87.31,101.04,118.09,133.29,148.28,164.76,179.87]
xlim(0,110)
#ylim(0,66)
ylim(0,184)
plot(x1,y1,'rh-',label='The Scheme of this Paper')
plot(x1,y2,'cD:',label='The Scheme of [10]')
plt.legend()
ax4.xaxis.set_major_locator(xmajorLocator)
ax4.xaxis.set_major_formatter(xmajorFormatter)

ax4.yaxis.set_major_locator(ymajorLocator2)
ax4.yaxis.set_major_formatter(ymajorFormatter2)


ax4.xaxis.set_minor_locator(xminorLocator)
ax4.yaxis.set_minor_locator(yminorLocator2)

ax4.xaxis.grid(True, which='major',ls='-.')
ax4.yaxis.grid(True, which='minor',ls='-')
font2 = {'family' : 'Times New Roman','weight' : 'normal'}

ax4.set_xlabel("Data Size (100 Bytes)",font2)
ax4.set_ylabel("Time Consumption (Seconds)")
#'''
plt.show()
