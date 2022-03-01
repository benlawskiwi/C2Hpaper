import numpy as np
import matplotlib.pyplot as plt

fn1 = '../C2D_all.dat'
fn2 = '../C2H_ANU_PES/C2D-355nm.dat'
fn3 = '../C2D_sigma.dat'

EA = 23956.4+36.4
ofs = 1220
ofs = 1500+36
cut = 4534
cut = 3471
#cut = 100000

b,a = np.loadtxt(fn1,usecols=(1,2),unpack=True)
d,c = np.loadtxt(fn3,usecols=(1,2),unpack=True)
x,y = np.loadtxt(fn2,unpack=True)

x = x-EA

for i in range(0,np.size(a)):
    aa = a[i]
    if a[i] > cut:
        aa = a[i]-ofs
    plt.plot((aa,aa),(0,-b[i]),'C0')

for i in range(0,np.size(c)):
    aa = c[i]
    if c[i] > cut:
        aa = c[i]-ofs
    plt.plot((aa,aa),(0,-d[i]),'C1')

plt.plot(x,y,'C2')
plt.xlim(-630,4225)
plt.show()

