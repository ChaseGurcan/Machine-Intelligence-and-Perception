# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq
from scipy import signal


Fsample = 499 #microseconds
y = np.linspace(0,2,Fsample)
time = np.arange(0,500,1)
axis =np.zeros(500)
axis[0:500]=20

noise = np.random.normal(0,1,500)

sum = axis + noise

plt.figure(1)
plt.plot(time,sum)
plt.title('Discrete Signal')
plt.xlabel('Time [microS]')
plt.ylabel('Amplitude')
#plt.legend()
plt.show()

#print(sum)
#print(len(sum))
kernal3 = np.array([0.27901, 0.44198, 0.27901])
kernal11  =np.array([0.000003, 0.000229, 0.005977, 0.060598, 0.24173, 0.382925, 0.24173, 0.060598, 0.005977, 0.000229,0.000003])
convolve3 = np.convolve(sum,kernal3)
convolve11 = np.convolve(sum,kernal11)
#filtered3=[]
#filtered11=[]
#for i in range(len(sum))
plt.figure(2)
plt.plot(time,convolve3[0:500])
plt.title('Discrete Signal')
plt.xlabel('Time [microS]')
plt.ylabel('Amplitude')
#plt.legend()
plt.show()

plt.figure(3)
plt.plot(time,convolve11[0:500])
plt.title('Discrete Signal')
plt.xlabel('Time [microS]')
plt.ylabel('Amplitude')
#plt.legend()
plt.show()
