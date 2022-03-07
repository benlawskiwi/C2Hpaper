import numpy as np
import abel
import matplotlib.pyplot as plt

imagefile = 'stg121/C2H-25M16CMb1024.txt'
imagefile = '../../C2H_ANU_PES/C2H-300nm.txt'

IM = np.loadtxt(imagefile)
zoom = IM.shape[-1]/1024

rr = (int(710*zoom), int(810*zoom))

AIM = abel.Transform(IM, method='rbasex', origin='slice',
                     transform_options=dict(reg=('diff', 10),
                     basis_dir='./'),
                     center_options=dict(radial_range=rr))

r, I, beta = AIM.distr.rIbeta()

eBE, PES = abel.tools.vmi.toPES(r, I,
                                energy_cal_factor=1.20e-5,
                                photon_energy=1.0e7/266, Vrep=-2000,
                                zoom=zoom)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(eBE, PES, lw=1, label=r'PES')
ax.plot(eBE, PES*beta, lw=1, label=r'PES$\times\beta$')

plt.show()
