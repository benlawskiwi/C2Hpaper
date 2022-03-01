import numpy as np
import abel
import matplotlib.pyplot as plt

sz = 1024
sf = 1.19e-5
zoom = sz/2048

expt = np.loadtxt(f'C2D-22M1CMI{sz}PESBE.dat', unpack=True)

im = np.loadtxt(f'C2D-22M1CM{sz}.txt')

# inverse Abel transform
aim = abel.Transform(im, method='basex', 
                     transform_options=dict(reg=100),
                     center='slice', angular_integration=True)

I, beta = abel.tools.vmi.Ibeta(aim.transform, window=9)

R, Iint = aim.angular_integration

# radial ranges for integration
eBE_range = np.array([
                   (18245,18600), (19020,19276), (19560,19740), (19740,20100),
                   (20310,20500), (20500,20800), (21050,21240), (21240,21550),
                   (21500,21760), (21760,21975), (21975,22152), (22348,22495),
                   (22520,22708), (22740,22822), (23080,23240), (23250,23460),
                   (23805,24003), (24005,24188), (24533,24755), (25273,25470)])

eKE_range = 1e7/355 - eBE_range
r_range = np.flip(np.sqrt(eKE_range/1.19e-5/600)*zoom)
r_range = np.concatenate(
            (np.array([(60, 98), (80, 143), (185, 240), (270, 303)])*zoom,
                         r_range))

# anisotropy parameter from image for each tuple r_range
Beta, Amp, Rmid, Ivstheta, theta =\
              abel.tools.vmi.radial_integration(aim.transform, r_range)

BetaT = np.transpose(Beta)

# convert radius, intensity to eBE, PES
eBEbas, PESbas = abel.tools.vmi.toPES(R[:len(I)], I, 
                           energy_cal_factor=sf,
                           photon_energy=1.0e7/355, Vrep=-600,
                           zoom=zoom)

eBEint, PESint = abel.tools.vmi.toPES(R, Iint, 
                           energy_cal_factor=sf,
                           photon_energy=1.0e7/355, Vrep=-600,
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
ax1.errorbar(Rmid, BetaT[0], BetaT[1], fmt='o', mfc='w', color='C2',
             label='specific radii')
ax1.axis(ymin=-1.5, ymax=2.5)
ax1.set_xlabel(r'radius (pixels)')
ax1.set_ylabel('anisotropy parameter')
ax1.legend(labelspacing=0.5, fontsize='small')

plt.savefig('C2D-pyabel2.png', dpi=75, bb_inches='tight')
plt.show()

width=3.487
height=width/1.4
one_col = (2*width, 2*height)
fig=plt.figure(figsize=one_col)

plt.plot(I*2/I.max(), 'k--', label='basex PES', lw=1.5)
plt.plot(beta*I*2/I.max(), 'C3', label=r'basex $\beta$ $\times$ I', lw=1.5)
plt.axis(xmin=0,xmax=400)
plt.annotate(r'$0^0_0$',(355,3.0), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'$2^1_1$',(355,0.45), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'$2^1_0$',(323,0.205), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$2^2_0$',(308,0.126), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'$2^3_0$',(293,0.091), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$a^*$',(270,0.111), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'$3^1_0$',(255,0.52), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'$2^1_03^1_0$',(244,0.28), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$2^2_03^1_0$',(225,0.10), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'$2^3_03^1_0$',(206,0.38), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$1^1_02^1_0$',(194,0.191), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$b$',(156,0.158), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$c$',(146,0.41), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$d$',(138,0.74), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$e^*$',(127,0.25), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$f$',(101,2.14), ha='center', color='C0', fontsize=11, fontweight='bold')
plt.annotate(r'$g$',(73,0.226), ha='center', color='C1', fontsize=11, fontweight='bold')
plt.annotate(r'+ve $\beta$',(25,2.5),ha='center', color = 'C1', fontsize=14)
plt.annotate(r'-ve $\beta$',(25,2.3),ha='center', color = 'C0', fontsize=14)
plt.xlabel('radius (pixels)',fontsize=15)
plt.ylabel('intensity (arb. u.)',fontsize=15)
plt.xticks([0,100,200,300,400],['0','100','200','300','400'],fontsize=12)
plt.yticks([])
#plt.xticklabels(['0','100','200','300','400'])
plt.legend(labelspacing=0.5, fontsize=10)
plt.savefig('C2D-pyabel3.pdf', dpi=300, bb_inches='tight')
plt.show()

np.savetxt('C2D-radial.dat',I*2/I.max())
