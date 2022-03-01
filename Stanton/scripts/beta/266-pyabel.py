import numpy as np
import abel
import matplotlib.pyplot as plt

sz = 1024
sf = 1.19e-5
zoom = sz/2048

expt = np.loadtxt(f'../../C2H_ANU_PES/C2H-266nm.dat', unpack=True)

#im = np.loadtxt(f'../../C2H_ANU_PES/C2H-266nm.txt')
im = np.loadtxt(f'stg121/C2H-25M16CMb1024.txt')

# inverse Abel transform
aim = abel.Transform(im, method='basex', 
                     transform_options=dict(reg=100),
                     center='slice', angular_integration=True)

I, beta = abel.tools.vmi.Ibeta(aim.transform, window=9)

R, Iint = aim.angular_integration

# convert radius, intensity to eBE, PES
eBEbas, PESbas = abel.tools.vmi.toPES(R[:len(I)], I, 
                           energy_cal_factor=sf,
                           photon_energy=1.0e7/266, Vrep=-2000,
                           zoom=zoom)

eBEint, PESint = abel.tools.vmi.toPES(R, Iint, 
                           energy_cal_factor=sf,
                           photon_energy=1.0e7/266, Vrep=-2000,
                           zoom=zoom)


# plot ------------------
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 8))

ax0.plot(eBEint, PESint/PESint.max(), label='basex angular', lw=1)
ax0.plot(*expt, label='ANUVMI', lw=1)
ax0.legend(labelspacing=0.5, fontsize='small')
ax0.axis(xmin=11700, xmax=31400)
ax0.set_xlabel(r'eBE (cm$^{-1}$)')

ax1.plot(I*2/I.max(), label='basex PES', lw=1)
ax1.plot(beta*I*2/I.max(), 'C3', label=r'basex $\beta$ $\times$ I', lw=1)
ax1.axis(ymin=-1.5, ymax=2.5)
ax1.set_xlabel(r'radius (pixels)')
ax1.set_ylabel('anisotropy parameter')
ax1.legend(labelspacing=0.5, fontsize='small')

plt.savefig('266-pyabel.png', dpi=75, bb_inches='tight')
plt.show()

width=3.487
height=width/1.4
one_col = (2*width, 2*height)
fig=plt.figure(figsize=one_col)

plt.plot(I*2/I.max(), 'k--', label='basex PES', lw=1.5)
plt.plot(beta*I*2/I.max(), 'C3', label=r'basex $\beta$ $\times$ I', lw=1.5)
plt.xlabel('radius (pixels)',fontsize=15)
plt.ylabel('intensity (arb. u.)',fontsize=15)
plt.yticks([])
#plt.xticklabels(['0','100','200','300','400'])
plt.legend(labelspacing=0.5, fontsize=10)
plt.savefig('266-pyabel.pdf', dpi=300, bb_inches='tight')
plt.show()

np.savetxt('266-radial.dat',I*2/I.max())
