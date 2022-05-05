import numpy as np
import matplotlib.pyplot as plt

fn1 = '../C2D.dat'
fn2 = '../C2D-355nm.dat'
fn3 = '../C2D.dat'

EA = 23956.4+36.4
ofs = 1220
#ofs = 1500+36
ofs = 1030.3352249+50
cut = 4534
cut = 3471
#cut = 100000


b,a = np.loadtxt(fn1,usecols=(1,2),unpack=True)
d,c = np.loadtxt(fn3,usecols=(1,2),unpack=True)
x,y = np.loadtxt(fn2,unpack=True)

x = x#-EA

#Plotting Settings
width = 3.487*2
height = width/1.4
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)


for i in range(0,np.size(c)):
    aa = c[i]
    if c[i] > cut:
        aa = c[i]-ofs
#    plt.plot((aa,aa),(0,-d[i]),'w',lw='2.5')
#    plt.plot((aa,aa),(0,-d[i]),'C0',lw='1.5')

plt.plot(x,y,'k',label=r'C$_2$D$^-$ PES')
plt.xlim(23000,28400)

#plt.plot((0,0),(0,0),'C0',label=r'$\Sigma$ Symmetry')
#plt.plot((0,0),(0,0),'C1',label=r'$\Pi$ Symmetry')
#plt.legend(loc=9,fontsize=10,frameon=False)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.yticks([])
plt.xticks([23000,24000,25000,26000,27000,28000])
ax.set_xticklabels(['23000','24000','25000','26000','27000','28000'],fontsize=14)
plt.minorticks_on()
plt.xlabel('Excitation Energy (cm$^{-1}$)',fontsize=14)
ax.tick_params(width=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)


#Annotating spectrum
plt.annotate(r'$\tilde{X}$ $^2\Sigma^+$',(400+EA,0.975),ha='center',fontsize=14)
plt.annotate(r'$\tilde{A}$ $^2\Pi$',(3300+EA,0.58),ha='center',fontsize=14)
plt.annotate(r'$0^0_0$',(-120+EA,0.955),ha='center')
plt.annotate(r'$2^1_1$',(-120+EA,0.22),ha='center')
plt.annotate(r'$2^1_0$',(278+EA,0.10),ha='center')
plt.annotate(r'$3^1_0$',(1740+EA,0.19),ha='center')
plt.annotate(r'$2^1_03^1_0$',(1952+EA,0.125),ha='center')
plt.annotate(r'$2^3_03^1_0$',(2607+EA,0.125),ha='center')
plt.annotate(r'a',(27253,0.11),ha='center')
plt.annotate(r'b',(3376+EA,0.201),ha='center')
plt.annotate(r'c',(3468+EA,0.320),ha='center')
plt.annotate(r'e',(3798+EA,0.859),ha='center')
plt.annotate(r'd',(27571,0.0859),ha='center')
plt.annotate(r'f',(27898,0.159),ha='center')
#plt.annotate(r'd',(4028,0.228),ha='center')
#plt.annotate(r'e',(4118,0.287),ha='center')

plt.savefig('SM2-plot.pdf', dpi=600,bbox_inches='tight')
plt.show()

