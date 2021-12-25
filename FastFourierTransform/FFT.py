%matplotlib inline 
import matplotlib.pyplot as plt
import numpy as np

N = 300 
x = np.linspace(0,2*np.pi,N)


#making sine function
A1 = 10
f1 = 10
y1 = A1*np.sin(f1*x)
plt.axis()
plt.plot(x,y1)

#second sine function
A2 = 3
f2 = 100
y2 = A2*np.sin(f2*x)
plt.plot(x,y2)

#combining the signal 
plt.plot(x,y1+y2)

#creating noise 
e = np.random.rand(N)*5
plt.plot(x,y1+y2+e)

#Applying the FFT
Fs = np.fft.fft(y1+y2+e)

#Applying an inverse FFT
Fs2 = np.zeros(N)
Fs2[2] = 120
Fs2[-2] = 120
Fs2[30] = 60
Fs2[-30] = 60
plt.plot(Fs2)
yy = np.fft.ifft(Fs2)
plt.plot(x,yy)

#Adjusting for spikes in data
# Put your code here
Fs2 = np.zeros(N)
Fs2[2] = 120
Fs2[-2] = 120
Fs2[30] = 60
Fs2[-30] = 60
Fs2[100] = 40
Fs2[-100] = 40
plt.plot(Fs2)
