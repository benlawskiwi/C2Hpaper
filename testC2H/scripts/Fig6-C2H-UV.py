import numpy as np
import matplotlib.pyplot as plt

x,y = np.loadtxt("C2H-6S1CMbI1024PESBE.dat",unpack=True)

#Plotting Settings
width = 3.487*2
height = width/1.4
one_col = (width,height)
fig,ax = plt.subplots(figsize=one_col)


plt.plot(x,y,color='k')

plt.axis(xmin=27000,xmax=30500,ymin=-0.02,ymax=0.25)

plt.annotate(r'$\tilde{A}\,^2\Pi$ $0^0_0$',(27750,0.225),ha='center',color='k',fontsize=14)
plt.annotate(r'$\tilde{X}\,^2\Sigma^+$',(28600,0.225),ha='center',color='k',fontsize=14)
plt.annotate(r'$\tilde{A}\,^2\Pi$ $3^1_0$',(29250,0.225),ha='center',color='k',fontsize=14)
plt.plot((27320,31000),(0.215,0.215),color='k')
plt.plot((27320,27320),(0.22,0.21),color='k')
plt.plot((28060,28060),(0.22,0.21),color='k')
plt.plot((28960,28960),(0.22,0.21),color='k')
plt.plot((29620,29620),(0.22,0.21),color='k')

plt.annotate('a', (27460,0.181), ha = 'center', color='k', fontsize=12)
plt.annotate('b', (27565,0.105), ha = 'center', color='k', fontsize=12)
plt.annotate('c', (27642,0.080), ha = 'center', color='k', fontsize=12)
plt.annotate('d', (27851,0.114), ha = 'center', color='k', fontsize=12)
plt.annotate('e', (27941,0.167), ha = 'center', color='k', fontsize=12)
plt.annotate('f', (28200,0.025), ha = 'center', color='k', fontsize=12)
plt.annotate('g', (28349,0.035), ha = 'center', color='k', fontsize=12)
plt.annotate('h', (28423,0.044), ha = 'center', color='k', fontsize=12)
plt.annotate('i', (28562,0.031), ha = 'center', color='k', fontsize=12)
plt.annotate('j', (28714,0.047), ha = 'center', color='k', fontsize=12)
plt.annotate('k', (28834,0.048), ha = 'center', color='k', fontsize=12)
plt.annotate('l', (29049,0.085), ha = 'center', color='k', fontsize=12)
plt.annotate('m', (29227,0.047), ha = 'center', color='k', fontsize=12)
plt.annotate('n', (29283,0.070), ha = 'center', color='k', fontsize=12)
plt.annotate('o', (29484,0.075), ha = 'center', color='k', fontsize=12)
plt.annotate('p', (29740,0.041), ha = 'center', color='k', fontsize=12)
plt.annotate('q', (29844,0.039), ha = 'center', color='k', fontsize=12)
plt.annotate('r', (30021,0.045), ha = 'center', color='k', fontsize=12)
plt.annotate('s', (30086,0.045), ha = 'center', color='k', fontsize=12)


ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.yticks([])
plt.xticks([27000,28000,29000,30000])
ax.set_xticklabels(['27000','28000','29000','30000'],fontsize=14)
plt.minorticks_on()

plt.xlabel('Binding Energy (cm$^{-1}$)',fontsize=14)
ax.tick_params(width=1.5)
plt.setp(ax.spines.values(), linewidth=1.5)


plt.savefig("FigS1.eps",dpi=600,bb_inches="tight")
plt.show()

