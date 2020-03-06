import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq


SamplingFrequency = 1000;    # in Hz
#N = 2*SamplingFrequency;
x = np.linspace(0,2,2*SamplingFrequency)


# wave amplitudes
amplitude = 3
amplitude2 =2

#declare omega
omega1 = 500
omega2 = 1000
omega3 = 2000

#setup of each wave
y1 = amplitude * np.cos(omega1 *math.pi *x)
y2 = amplitude2*np.cos(omega2*math.pi*x)
y3 = amplitude*np.cos(omega3*math.pi*x)

#declare the function of the wave
y = 2 + y1 + y2 + y3

#now we need to plot function
plt.figure(1)
plt.plot(x[0:100],y[0:100])
plt.title('Continuous Period Signal in Time Domain')
plt.xlabel('Time [S]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

#Use imported fftfreq
frequencys= fftfreq(2*SamplingFrequency)

#filter out the complex conjugates
mask = frequencys>0

fftvalues = fft(y)

ffttheoretical = 2*np.abs(fftvalues/2*SamplingFrequency)

#frequency = np.linspace(0,SamplingFrequency, int(N/2))


#Use fourier transform to convert im to amplitude vs SamplingFrequency
#y = 2/N*np.abs(frequencyfunction[0:np.int(N/2)])

#Now plot this new frequencyfunction
plt.figure(2)
plt.plot(frequencys[0:1000],ffttheoretical[0:1000])
plt.title('Continuous Period Signal in Frequency Domain')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.show()
