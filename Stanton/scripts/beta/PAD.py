import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


aa1,bb1 = np.loadtxt('betaS.txt',usecols=(0,4),unpack=True)
aa2,bb2 = np.loadtxt('betaP.txt',usecols=(0,4),unpack=True)


def bet(E,A,f):
    Z = (8*(1-f))/(3*f)
    num = 2*Z*E+2*A*E**2-4*E
    den = 1/A+2*A*E**2+Z*E
    return num/den


with open('beta-raw.json') as json_file:
    data = json.load(json_file)
    
peaks = [211,0,210,310,210310,230310,'G','H','I','J','K','B1','B2','B3']
col = ['C0','C0','C0','C0','C0','C0','C1','C1','C1','C1','C1','C3','C3','C3']

width = 3.487
height = width/1.4
one_col = (2*width,2*height)

fig = plt.figure(figsize=one_col)
ax = plt.subplot(111)

n = np.size(peaks)
for j in range (0,n):
    x = peaks[j]
    eKE = []
    b = []
    err = []
    c = col[j]
    for i in data:
        p = i['Peak']
        if x != p: continue
        pea = str(p)
        b.append(i['Beta'])
        eKE.append(i['eKE'])
        err.append(i['Error'])
    #plt.errorbar(eKE,b,yerr=err,fmt='o',markersize=8,color=c,label=pea)

xeKE = []
xb = []
xerr = []
xhteKE =[]
xhtb = []
xhterr = []
aeKE = []
ab = []
aerr = []

for i in data:
    p = i['Peak']
    if p in (211,0,310):
        xeKE.append(i['eKE']/8065.74)
        xb.append(i['Beta'])
        xerr.append(i['Error'])
    if p in (210,210310,230310):
        xhteKE.append(i['eKE']/8065.74)
        xhtb.append(i['Beta'])
        xhterr.append(i['Error'])
    if p in ('G','H','I','J','K','B1','B2','B3'):
        aeKE.append(i['eKE']/8065.74)
        ab.append(i['Beta'])
        aerr.append(i['Error'])

popt, pcov = curve_fit(bet,xeKE,xb,sigma=xerr)
perr = np.sqrt(np.diag(pcov))
print ('A=',popt[0],'+/-',perr[0])
print ('f=',popt[1],'+/-',perr[1])

popt2, pcov2 = curve_fit(bet,xhteKE,xhtb,sigma=xhterr)
perr2 = np.sqrt(np.diag(pcov2))
print ('A=',popt2[0],'+/-',perr2[0])
print ('f=',popt2[1],'+/-',perr2[1])

popt3, pcov3 = curve_fit(bet,aeKE,ab,sigma=aerr)
perr3 = np.sqrt(np.diag(pcov3))
print ('A=',popt3[0],'+/-',perr3[0])
print ('f=',popt3[1],'+/-',perr3[1])


with open('C2D-beta.json') as json_file:
    data = json.load(json_file)

dex = []
dbx = []
ddbx = []
dexh = []
dbxh = []
ddbxh = []
dea = []
dba = []
ddba = []

for k in data:
    if k['Peak'] in (211,0,310):
        dex.append(k['eKE']/8065.74)
        dbx.append(k['Beta'])
        ddbx.append(k['Error'])
    if k['Peak'] in (210310,230310):
        dexh.append(k['eKE']/8065.74)
        dbxh.append(k['Beta'])
        ddbxh.append(k['Error'])
    if k['Peak'] in ('A','B','C','D'):
        dea.append(k['eKE']/8065.74)
        dba.append(k['Beta'])
        ddba.append(k['Error'])


plt.errorbar(xeKE,xb,yerr=xerr,fmt='o',markersize=6,color='C0',elinewidth=0.5,mfc='white',label=r'$\tilde{X}\,^2\Sigma^+$')
plt.errorbar(xhteKE,xhtb,yerr=xhterr,fmt='d',markersize=6,color='C4',elinewidth=0.5,mfc='white',label=r'$\tilde{X}\,^2\Sigma^+ - $HT')
plt.errorbar(aeKE,ab,yerr=aerr,fmt='s',markersize=6,color='C1',elinewidth=0.5,mfc='white',label=r'$\tilde{A}\,^2\Pi$')

grid = np.arange(0,1.7,0.01)

plt.plot(grid,bet(grid,popt[0],popt[1]),'k:', lw=2)
#plt.plot(grid,bet(grid,popt2[0],popt2[1]),'C1--', lw=2,label='89% p')
plt.plot(grid,bet(grid,popt3[0],popt3[1]),'k--', lw=2)

A0 = bet(grid,popt[0],popt[1])[-1]
A1 = bet(grid,popt3[0],popt3[1])[-1]
A2 = grid[-1]

#plt.errorbar(dex,dbx,yerr=ddbx,fmt='s',markersize=8,color='C1',mfc='white',label=r'C$_2$D $^2\Sigma^+$')
#plt.errorbar(dexh,dbxh,yerr=ddbxh,fmt='s',markersize=8,color='C1',mfc='white',label=r'C$_2$D $^2\Sigma^+$-HT')
#plt.errorbar(dea,dba,yerr=ddba,fmt='s',markersize=8,color='C0',mfc='white',label=r'C$_2$D $^2\Pi$')

#plt.annotate(r'$A$ = 1.5(4) eV$^{-1}$',(1.15,1.200),color='C1',fontsize=13)
plt.annotate(r'$A_1$ = 0.66(4) eV$^{-1}$',(1.15,0.18),color='k',fontsize=13)
#plt.annotate(r'$A$ = 0.66(4) eV$^{-1}$',(1.45,-0.68),color='C0',fontsize=10)

plt.annotate(r'$\gamma_p$ = 0.9',(A2+0.05,A1),va='center',fontsize=12)
plt.annotate(r'$\gamma_p$ = 0.1',(A2+0.05,A2-0.1),va='center',fontsize=12)

plt.xlabel('Electron Kinetic Energy (eV)',fontsize=14)
plt.ylabel(r'Anisotropy Parameter ($\beta$)',fontsize=14)

plt.xticks([0,0.5,1,1.5],[0.0,0.5,1.0,1.5],fontsize=13)
plt.yticks([-1,0,1,2],[-1.0,0.0,1.0,2.0],fontsize=13)
plt.minorticks_on()
plt.axis(ymin=-1,ymax=2)
#chartBox = ax.get_position()
#ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.85, chartBox.height])
#ax.legend(loc='upper center', bbox_to_anchor=(1.16, 0.61),fontsize=11)
plt.legend(loc='upper center',ncol=3,frameon=False)

ax.spines['top'].set_visible(False)
#ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.setp(ax.spines.values(), linewidth=1.5)

plt.plot(aa1-3,bb1*0.93)
plt.plot((aa2-3)/2,bb2*0.9)

plt.savefig("Fig5.eps", dpi=400, bbbox_inches="tight")
#plt.legend()
plt.show()
