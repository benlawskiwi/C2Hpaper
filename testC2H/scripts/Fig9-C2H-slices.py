import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image

width = 3.487
height = 2*width/1.4
one_col = (2*width, 2*height)

x1, y1 = np.loadtxt("C2H-6S1CMbI1024PESBE.dat", unpack=True)
x2, y2  = np.loadtxt("C2H-6S1CMI512PESBE.dat", unpack=True)
x3, y3  = np.loadtxt("C2H-6S1CMI512Am0Ax30PESBE.dat", unpack=True)
x4, y4  = np.loadtxt("C2H-6S1CMI512Am60Ax90PESBE.dat", unpack=True)
VMI1 = np.loadtxt("C2H-12D1CMb512.txt")
VMI2 = np.loadtxt("C2D-22M1CM1024.txt")

fig=plt.figure(figsize=one_col)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212, sharex=ax1)

ax1.plot(x1,y1,color='k')
ax2.plot(x2,y2*3.2,color='k',label='512x512 PES')
ax2.plot(x3,y3*3,color='C2',label = r'$\theta=0^{\circ}-30^{\circ}$')
ax2.plot(x4,y4,color='C0',label=r'$\theta=60^{\circ}-90^{\circ}$')

ax1.annotate('a', (27460,0.181), ha = 'center', color='k', fontsize=12)
ax1.annotate('b', (27565,0.105), ha = 'center', color='k', fontsize=12)
ax1.annotate('c', (27642,0.080), ha = 'center', color='k', fontsize=12)
ax1.annotate('d', (27851,0.114), ha = 'center', color='k', fontsize=12)
ax1.annotate('e', (27941,0.167), ha = 'center', color='k', fontsize=12)
ax1.annotate('f', (28200,0.025), ha = 'center', color='k', fontsize=12)
ax1.annotate('g', (28349,0.035), ha = 'center', color='k', fontsize=12)
ax1.annotate('h', (28423,0.044), ha = 'center', color='k', fontsize=12)
ax1.annotate('i', (28562,0.031), ha = 'center', color='k', fontsize=12)
ax1.annotate('j', (28714,0.047), ha = 'center', color='k', fontsize=12)
ax1.annotate('k', (28834,0.048), ha = 'center', color='k', fontsize=12)
ax1.annotate('l', (29049,0.085), ha = 'center', color='k', fontsize=12)
ax1.annotate('m', (29227,0.047), ha = 'center', color='k', fontsize=12)
ax1.annotate('n', (29283,0.070), ha = 'center', color='k', fontsize=12)
ax1.annotate('o', (29484,0.075), ha = 'center', color='k', fontsize=12)
ax1.annotate('p', (29740,0.041), ha = 'center', color='k', fontsize=12)
ax1.annotate('q', (29844,0.039), ha = 'center', color='k', fontsize=12)
ax1.annotate('r', (30021,0.045), ha = 'center', color='k', fontsize=12)
ax1.annotate('s', (30086,0.045), ha = 'center', color='k', fontsize=12)

ax2.annotate('+', (28199,0.12), ha='center', color='k', fontsize=14)
ax2.annotate('+', (28327,0.18), ha='center', color='k', fontsize=14)
ax2.annotate('+', (29223,0.25), ha='center', color='k', fontsize=14)
ax2.annotate('+', (29861,0.15), ha='center', color='k', fontsize=14)

ax1.axis(ymax=0.25,ymin=-0.02)
ax2.axis(ymax=0.8,ymin=-0.02)
plt.axis(xmin=26250,xmax=30500)
ax2.legend()
ax1.plot((27320,31000),(0.215,0.215),color='k')
ax1.plot((27320,27320),(0.22,0.21),color='k')
ax1.plot((28060,28060),(0.22,0.21),color='k')
ax1.plot((28960,28960),(0.22,0.21),color='k')
ax1.plot((29620,29620),(0.22,0.21),color='k')

ax1.annotate(r'$\tilde{A}\,^2\Pi$ $0^0_0$',(27750,0.225),ha='center',color='k',fontsize=14)
#ax1.annotate(r'$\tilde{X}\,^2\Sigma^+$',(28600,0.225),ha='center',color='k',fontsize=14)
ax1.annotate(r'$\tilde{A}\,^2\Pi$ $3^1_0$',(29250,0.225),ha='center',color='k',fontsize=14)

#sub_axes=plt.axes([.60,.745,.15,.15])
#sub_axes.imshow(VMI1, extent=[-256, 256, -256, 256], vmin=0, cmap='jet', vmax=VMI1.max()/1)
#sub_axes.set_xticks([0, 256])
#sub_axes.set_xticklabels(["0", "256"], fontsize="smaller")
#sub_axes.set_yticks([])
#sub_axes.set_yticklabels([])

#sub_axes=plt.axes([.60,.325,.15,.15])
#sub_axes.imshow(VMI2, extent=[-256, 256, -256, 256], vmin=0, cmap='jet', vmax=VMI2.max()/1)
#sub_axes.set_xticks([0, 256])
#sub_axes.set_xticklabels(["0", "256"], fontsize="smaller")
#sub_axes.set_yticks([])
#sub_axes.set_yticklabels([])

ax2.set_xlabel(r'electron binding energy (cm$^{-1}$)')
ax2.set_ylabel(r'intensity (arb. u.)')
ax1.set_ylabel(r'intensity (arb. u.)')

plt.savefig("Fig9-C2H-slices.pdf", dpi=300, bb_inches='tight')
plt.show()
