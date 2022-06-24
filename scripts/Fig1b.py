import numpy as np
import matplotlib.pyplot as plt

width = 3.487*1.5
#height = width/1.618 #golden ratio
height = width/1
one_col = (width, height)

VMI = np.loadtxt("C2D-22M1CM512.txt")
rows, cols = VMI.shape
trim = 46
#r2 = rows//2 - trim
#c2 = cols//2 - trim
r2 = rows//2
c2 = cols//2


VMI = VMI[trim:-trim, trim:-trim]

fig, ax = plt.subplots()

vmi = ax.imshow(VMI, extent=[-r2, r2, -c2, c2], vmin=-0, cmap="jet")
#ax.set_xlabel(r"radius (pixels)", ha='left')
ax.axes.get_yaxis().set_ticks([])
plt.setp(ax.spines.values(), linewidth=1.5)
label = ax.set_xlabel("Radius (pixels)", fontsize='18')
ax.xaxis.set_label_coords(0.7, -0.08)
ax.set_xticks([0, 256])
ax.set_xticklabels(["0", "1024"],fontsize=16)
# colour bar
cbaxes = fig.add_axes([0.82, 0.5, 0.018, 0.38])
cbaxes.yaxis.set_label_coords(2, 0.5)
plt.colorbar(vmi, cax=cbaxes, ticks=[0, int(VMI.max()/1.1/10)*10])
cbaxes.tick_params(labelsize=16)
cbaxes.set_ylabel("Electrons", fontsize='18')

ax.annotate('', xy=(-0.1, 0.2), xycoords='axes fraction', xytext=(-0.1, 0.8), 
            arrowprops=dict(arrowstyle="<-", color='k',lw=1.5))
ax.annotate('Laser Polarisation',xy=(-0.1, 0.2), rotation=90, xycoords='axes fraction', xytext=(-0.15, 0.5),fontsize=18, ha='center', va='center')

plt.setp(ax.spines.values(), linewidth=1.5)
ax.tick_params(width=1.5)

plt.savefig("Fig1b.pdf", dpi=600, bbox_inches='tight')
plt.show()
print('old version')

