import numpy as np
import matplotlib.pyplot as plt

fn1 = '../C2H_all.dat'
fn2 = '../C2H_ANU_PES/C2H-355nm.dat'
fn3 = '../C2H_sigma.dat'

EA = 23956.4
ofs = 1220
cut = 4534
cut = 3471

b,a = np.loadtxt(fn1,usecols=(1,2),unpack=True)
d,c = np.loadtxt(fn3,usecols=(1,2),unpack=True)
x,y = np.loadtxt(fn2,unpack=True)

x = x-EA

#Plotting Settings
width = 3.487*2
height = width/1.4
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)

for i in range(0,np.size(a)):
    aa = a[i]
    if a[i] > cut:
        aa = a[i]-ofs
    plt.plot((aa,aa),(0,-b[i]),'C1')

for i in range(0,np.size(c)):
    aa = c[i]
    if c[i] > cut:
        aa = c[i]-ofs
    plt.plot((aa,aa),(0,-d[i]),'w',lw='2.5')
    plt.plot((aa,aa),(0,-d[i]),'C0',lw='1.5')

plt.plot(x,y,'k',label=r'C$_2$H$^-$ PES')
plt.xlim(-630,4225)

plt.plot((0,0),(0,0),'C0',label=r'$\Sigma$ Symmetry')
plt.plot((0,0),(0,0),'C1',label=r'$\Pi$ Symmetry')
plt.legend(loc=1,fontsize=10,frameon=False)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.yticks([])
plt.xticks([0,1000,2000,3000,4000])
ax.set_xticklabels(['0','1000','2000','3000','4000'],fontsize=14)
plt.minorticks_on()
plt.xlabel('Wavenumber (cm$^{-1}$)',fontsize=14)
ax.tick_params(width=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)


#Annotating spectrum
plt.annotate(r'$\tilde{X}$ $^2\Sigma^+$',(400,0.975),ha='center',fontsize=14)
plt.annotate(r'$\tilde{A}$ $^2\Pi$',(3800,0.58),ha='center',fontsize=14)
plt.annotate(r'$0^0_0$',(-137,0.955),ha='center')
plt.annotate(r'$2^1_1$',(-137,0.17),ha='center')
plt.annotate(r'$2^1_0$',(361,0.10),ha='center')
plt.annotate(r'$3^1_0$',(1840,0.19),ha='center')
plt.annotate(r'$2^1_03^1_0$',(2093,0.145),ha='center')
plt.annotate(r'$2^3_03^1_0$',(2943,0.145),ha='center')
plt.annotate(r'a',(3607,0.455),ha='center')
plt.annotate(r'b',(3692,0.279),ha='center')
plt.annotate(r'c',(3788,0.228),ha='center')
plt.annotate(r'd',(4028,0.228),ha='center')
plt.annotate(r'e',(4118,0.287),ha='center')

plt.savefig('C2H-plot.pdf', dpi=600,bbox_inches='tight')
plt.show()

