import numpy as np
import matplotlib.pyplot as plt

def Gauss (E0,FWHM,E):
    alpha = FWHM/2/np.sqrt(np.log(2.0))
    return np.exp(-((E-E0)/alpha)**2)

FWHM = 40
amp = 1
hv = 1e7/300

#Plotting Settings
width = 3.487*2
height = width/1.4
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)

x,y = np.loadtxt('300nm.dat',unpack=True)

b,em,ex,er,ep = np.loadtxt('300.dat',skiprows=1,unpack=True)
ym = []
by = []
xx = []

for i in range(0,np.size(b)):
    subr = np.logical_and(x>em[i],x<ex[i])
    suby = y[subr]
    subx = x[subr]
    yx = max(suby)
    for j in range(0,np.size(suby)):
        if suby[j] == yx:
            xx.append(subx[j])
    ym.append(max(suby))
    by.append(b[i]*max(suby))

fd = np.column_stack((ep,ym,b,by))
np.savetxt('300BetaData.txt',fd)

#Now we can plot the data

Ev = np.arange(15000,30000,0.5)
spec = np.zeros(np.size(Ev))

for i in range(0,np.size(b)):
    spec+= by[i]*amp*Gauss(xx[i],FWHM,Ev)

plt.plot(hv-x,y,'k',label='C$_2$H$^-$ at 300nm')
plt.plot(hv-Ev,spec,'C3',label = r'Anisotropy $\beta\times$I')

#Plotting
plt.xlim(hv-27000,hv-15000)
#plt.ylim(-0.18,1.61)
plt.ylim(-0.18,0.6)

col = ['C0','C0','C1','C0','C0','C1','C1','C1','C1','C1','C1','C1','C0','C1','C1','C1','C1','C1','C1','C1']

lab = ['$2^1_1$','0$^0_0$','$2^1_0$','$2^2_0$','$3^1_0$','$2^1_03^1_0$','$2^3_03^1_0$','a','b','c','d','e','f','h','i','j','k','l','n','o']
for i in range(0,np.size(lab)):
    if i == 1: continue
    if i ==0:
        plt.annotate(lab[i],(hv-xx[i]+100,max(ym[i],by[i])+0.03),ha='center',color=col[i])
        continue
    if i ==14:
        plt.annotate(lab[i],(hv-xx[i]-100,max(ym[i],by[i])+0.03),ha='center',color=col[i])
        continue
    plt.annotate(lab[i],(hv-xx[i],max(ym[i],by[i])+0.03),ha='center',color=col[i])
plt.annotate('$0^0_0$',(16548,0.56),ha='center')

ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.setp(ax.spines.values(), linewidth=1.5)
plt.xlabel('Electron Kinetic Energy (cm$^{-1}$)',fontsize=14)
plt.ylabel(r'Intensity (arb. u.)',fontsize=14)
plt.legend(loc='upper left',fontsize=10,frameon=False)
ax.set_xticklabels(np.arange(6000,20000,2000),fontsize=14)
ax.set_yticklabels([-0.2,-0.1,0.0,0.1,0.2,0.3,0.4,0.5,0.6],fontsize=14)
plt.minorticks_on()

plt.savefig('plotBeta.pdf', dpi=600,bbox_inches='tight')

plt.show()
