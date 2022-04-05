import numpy as np
import matplotlib.pyplot as plt

width = 3.487*2
height = width/1.4
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)

x1,y1 = np.loadtxt('C2H-355nm.dat',unpack=True)
x2,y2 = np.loadtxt('C2D-355nm.dat',unpack=True)

plt.plot(x1,y1,label=r'C$_2$H$^-$')
plt.plot(x2,-y2-0.1,label=r'C$_2$D$^-$')
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.yticks([])
plt.xlim(23500,28300)
plt.xticks([23000,24000,25000,26000,27000,28000])
ax.set_xticklabels(['23000','24000','25000','26000','27000','28000'],fontsize=14)
plt.minorticks_on()
ax.tick_params(width=1.5)
plt.xlabel('Binding Energy (cm$^{-1}$)',fontsize=14)
plt.annotate(r'$\tilde{X}$ $^2\Sigma^+$',(24400,0.825),ha='center',fontsize=14)
plt.annotate(r'$\tilde{A}$ $^2\Pi$',(27800,0.43),ha='center',fontsize=14)
plt.setp(ax.spines.values(), linewidth=1.5)
plt.legend(loc=1,fontsize=14,frameon=False)
plt.subplots_adjust(top = 1, bottom = 0.12, right = 0.95, left = 0.05, 
            hspace = 0, wspace = 0)

plt.savefig('Fig1c.pdf',bbbox_inches='tight')
plt.show()
