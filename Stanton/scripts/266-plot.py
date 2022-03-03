import numpy as np
import matplotlib.pyplot as plt

def Gauss (E0,FWHM,E):
    alpha = FWHM/2/np.sqrt(np.log(2.0))
    return np.exp(-((E-E0)/alpha)**2)
FWHM = 80
#FWHM = 80
amp = 1

fn1 = '../C2H_all.dat'
fn2 = '../C2H_ANU_PES/C2H-266nm.dat'

EA = 23956.4-31
ofs = 1220
cut = 4534
cut = 3471

b,a = np.loadtxt(fn1,usecols=(1,2),unpack=True)
x,y = np.loadtxt(fn2,unpack=True)

x = x-EA

#Plotting Settings
width = 3.487*2
height = width/1.4
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)


Ev = np.arange(-630,12000,0.5)
spec = np.zeros(np.size(Ev))

for i in range(0,np.size(a)):
    aa = a[i]
    if a[i] > cut:
        aa = a[i]-ofs
    spec += b[i]*amp*Gauss(aa,FWHM,Ev)
    #plt.plot((aa,aa),(0,-b[i]),'C0')

#plt.plot(Ev,-spec,'C2',label=r'Simulates Spectrum')
plt.plot(x,y,'k',label=r'C$_2$H$^-$ at 266 nm')
plt.plot(Ev,-spec,'C2',label=r'Simulated Spectrum')
plt.xlim(-630,8000)

#Labelling
#plt.plot((27320-EA,31000-EA),(0.215,0.215),color='k')
#plt.plot((27320-EA,27320-EA),(0.22,0.21),color='k')
#plt.plot((28060-EA,28060-EA),(0.22,0.21),color='k')
#plt.plot((28960-EA,28960-EA),(0.22,0.21),color='k')
#plt.plot((29620-EA,29620-EA),(0.22,0.21),color='k')

plt.plot((3553,7000),(0.4,0.4),'k')
plt.plot((3553,3553),(0.42,0.38),'k')
plt.plot((4055,4055),(0.42,0.38),'k')
plt.plot((5174,5174),(0.42,0.38),'k')
plt.plot((5606,5606),(0.42,0.38),'k')
plt.annotate(r'$0^0_0$',(3804,0.44),ha='center',color='k')
plt.annotate(r'$3^1_0$',(5390,0.44),ha='center',color='k')
plt.annotate(r'$\tilde{A}$ $^2\Pi$',(2870,0.40),va='center',fontsize=12)
plt.annotate('f',(4396,0.105),ha='center')
plt.annotate('g',(4566,0.12),ha='center')
plt.annotate('j',(4812,0.1),ha='center')
plt.annotate('k',(4944,0.11),ha='center')
plt.annotate('l',(5184,0.173),ha='center')
plt.annotate('n',(5385,0.146),ha='center')
plt.annotate('o',(5587,0.131),ha='center')

#Plot settings
plt.legend(loc=1,fontsize=10,frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.yticks([])
plt.xticks([0,2000,4000,6000,8000])
ax.set_xticklabels(['0','2000','4000','6000','8000'],fontsize=14)
plt.minorticks_on()
plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=14)
ax.tick_params(width=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)


plt.savefig('266-plot.pdf', dpi=600,bbox_inches='tight')
plt.show()

