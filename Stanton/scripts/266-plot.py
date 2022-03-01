import numpy as np
import matplotlib.pyplot as plt

def Gauss (E0,FWHM,E):
    alpha = FWHM/2/np.sqrt(np.log(2.0))
    return np.exp(-((E-E0)/alpha)**2)
FWHM = 80
amp = 1

fn1 = '../C2H_all.dat'
fn2 = '../C2H_ANU_PES/C2H-266nm.dat'

EA = 23956.4
ofs = 1220
cut = 4534
cut = 3471

b,a = np.loadtxt(fn1,usecols=(1,2),unpack=True)
x,y = np.loadtxt(fn2,unpack=True)

x = x-EA

Ev = np.arange(-630,12000,0.5)
spec = np.zeros(np.size(Ev))

for i in range(0,np.size(a)):
    aa = a[i]
    if a[i] > cut:
        aa = a[i]-ofs
    spec += b[i]*amp*Gauss(aa,FWHM,Ev)
    #plt.plot((aa,aa),(0,-b[i]),'C0')

plt.plot(Ev,-spec)
plt.plot(x,y,'C2')
plt.xlim(-630,12000)
plt.show()

