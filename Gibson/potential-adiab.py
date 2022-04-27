import numpy as np
import cse
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib as mpl

def adiabatic(VSp, VPp, V12):
     W = np.array([[VSp, V12], [V12, VPp]])

     Ae, Av = np.linalg.eigh(W.T)

     return Ae.T, Av.T

def Va(q1, q2, q3, Ca):
    s = 0
    for ii, jj, kk, C in Ca:
        s += C*(q1**ii)*(q2**jj)*(q3**kk)

    return s

def V12(q1, q2, q3, C12):
    s = 0
    for ii, jj, kk, C in C12:
        s += C*q1**ii*q2**jj*q3**kk

    return np.sin(q3)*(1-np.tanh(q1))*(1-np.tanh(q2))*s

H2cm = 27.2*8065.541

# Expansion coefficients Tarroni & Carter JCP 119, 12878 (2003)
i, j, k, CSp, CPp, CPm, C12 = np.loadtxt('Cijk', unpack=True)
# restructure for easy transport to generating function
CSp = np.column_stack((i, j, k, CSp))
CPm = np.column_stack((i, j, k, CPm))
CPp = np.column_stack((i, j, k, CPp))
C12 = np.column_stack((i, j, k, C12))

# Rcc, RCH, bond angle - equilibrium values
eq = {'Sp':(2.283737, 2.00787, np.pi), 'Pp':(2.432753, 2.021043, np.pi),
      'Pm':(2.432753, 2.021043, np.pi), '12':(2.5, 2.0, np.pi)}

# coordinates, relative to quilibrium values, in Angstroms
cc = np.linspace(-0.2, 0.2, 101)
ch = np.linspace(-0.2, 0.2, 101)
bar = np.linspace(-1, 1, 101)

CC, BAR = np.meshgrid(cc, bar, indexing='ij')

CH = 0 # equilibrium


Vsp = Va(CC, CH, BAR, CSp)*H2cm
Vpm = Va(CC, CH, BAR, CPm)*H2cm
Vpp = Va(CC, CH, BAR, CPp)*H2cm
VV = V12(CC, CH, BAR, C12)*H2cm

# diagonalize
(Asp, App), Av = adiabatic(Vsp, Vpp, VV)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.view_init(elev=6, azim=13)  # 30, 25
ax.view_init(elev=19, azim=12)  # 30, 25
ax.view_init(elev=20, azim=18)  # 30, 25
ax.plot_surface(CC*0.529177, BAR, App/1000+24, linewidth=0, color='C1')
ax.plot_surface(CC*0.529177, BAR, Asp/1000+24, linewidth=0, color='C0')
ax.plot_surface(CC*0.529177, BAR, Vpm/1000+24, linewidth=0, color='C2')

ax.set_xlabel(r'CC stretch ($\AA$)')
ax.set_ylabel(r'$\angle$ CCH bend (rad.)')
ax.set_xticks([-0.1, 0, 0.1])
ax.set_yticks([-1, 0, 1])
ax.set_zlabel(r'potential energy (1000 cm$^{-1}$)')

'''
sigma = mpl.lines.Line2D([0],[0], linestyle="none", c='C0', marker = 'o')
pip = mpl.lines.Line2D([0],[0], linestyle="none", c='C2', marker = 'o')
#pim = mpl.lines.Line2D([0],[0], linestyle="none", c='C1', marker = 'o')
ax.legend([pip, sigma], [r'$\tilde{A}\, ^2\Pi$', r'$\tilde{X}\, ^2\Sigma^+$'], numpoints = 1)
'''

#ax.text(0.0, 1.1, 28, r'$\tilde{X}\, ^2\Sigma^+$', color='C0', fontsize=16) 
#ax.text(0.0, 1.2, 39, r'$\tilde{A}\, ^2\Pi^+$', color='C1', fontsize=16) 
#ax.text(0.0, 1.2, 36, r'$\tilde{A}\, ^2\Pi^-$', color='C2', fontsize=16) 

ax.text(0.0, 1.3, 28, r'$\tilde{X}\, ^2\Sigma^+$', color='C0', fontsize=16)
ax.text(0.0, 1.3, 39, r'$\tilde{A}\, ^2\Pi^+$', color='C1', fontsize=16)
ax.text(0.0, 1.3, 36, r'$\tilde{A}\, ^2\Pi^-$', color='C2', fontsize=16)

plt.savefig('potential-adiab.pdf', dpi=300, bbox_inches='tight')
plt.show()
