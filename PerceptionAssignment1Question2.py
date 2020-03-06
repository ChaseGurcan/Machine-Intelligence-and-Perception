import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

Fsample = 1e6 #1M Hz
Length =1000
y = np.linspace(0,2,Length)
time = np.arange(0,1000,1)
axis =np.zeros(1000)
axis[500:]=1



plt.figure(1)
plt.plot(time,axis)
plt.title('Discrete Signal')
plt.xlabel('Time [microS]')
plt.ylabel('Amplitude')
#plt.legend()
plt.show()

#now apply fourier transform
#first normalize the amplitude
amp = np.fft.fft(axis)/len(axis)
#now remove the sampling freq
amp = amp[range(int(len(axis)/2))]


count = len(axis)
values = np.arange(int(count/2))
timeperiod = count/Fsample
freqs = values/timeperiod

plt.figure(2)
plt.plot(freqs,abs(amp))
plt.plot(time,axis)
plt.title('FFT Amplitude Spectrum')
plt.xlabel('Freq [Hz]')
plt.ylabel('Amplitude')
plt.show()


# bw = powerbw(X, Fs)
[bw,f_low,f_high,power] = powerbw(axis, Fsample);
f_low
f_high
