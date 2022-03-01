import numpy as np
import abel
import matplotlib.pylab as plt

imagefile = 'stg121/C2H-25M16CMb1024.txt' # 'NO2-001M1CM2048.txt'

IM = np.loadtxt(imagefile)
zoom = IM.shape[-1]/1024

# radial range of peak X origin intensity used for image centering
# rr = (int(1500*zoom), int(1700*zoom))
rr = (int(710*zoom), int(810*zoom))

# Abel transform - rbasex ------------------------------------------
AIM = abel.Transform(IM, method='rbasex', origin='slice',
                     transform_options=dict(reg=('diff', 10),
                     basis_dir='./'),
                     center_options=dict(radial_range=rr))

r, I, beta = AIM.distr.rIbeta()   # I, beta directly from basis fit

# convert intensity to PES
eBE, PES = abel.tools.vmi.toPES(r, I,
                                energy_cal_factor=1.20e-5,
                                photon_energy=1.0e7/266, Vrep=-2000,
                                zoom=zoom)
sube = eBE < 39000
EA = eBE[sube][(PES[sube]).argmax()]
# eBE -= EA
print(f'EA = {EA}')
# normalize intensity to X origin
PES /= PES.max()
beta = beta[::-1]

np.savetxt(f'{imagefile[:-4]}_rbasex.dat', np.column_stack((eBE, PES, beta)),
           fmt='%8.3f   %10.5f    %10.5f',
           header='eBE(cm-1)  int. (rel. X0)  beta')

# plots ----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(eBE, PES, lw=1, label=r'PES')
ax.plot(eBE, PES*beta, lw=1, label=r'PES$\times\beta$')
ax.plot((eBE[0], eBE[-1]), (0, 0), 'C7--')

ax.legend()
ax.set_xlabel(r'eBE (cm$^{-1}$)')
ax.set_ylabel(r'intensity')
ax.set_title(r'NO$_2^-$ photodetachment at 468.88 nm')
#ax.axis(xmin=17500, xmax=21350, ymin=-0.05, ymax=1.8)

#plt.subplots_adjust(left=0.15)
plt.savefig('beta-rbasex-PES.png')
plt.show()
