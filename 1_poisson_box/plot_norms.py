#!/usr/bin/python

import os
import sys
import inspect
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 

def read_norms(fname):
    array=np.loadtxt(fname, dtype='float')
    return array[1] 

fig, axs = plt.subplots(1, 2, sharey=True, figsize=(10,8))
# ---------------------------------------------
#  Initialize the Sets
# ---------------------------------------------

set_p = [2,3,4]
set_ele = ['hex', 'tet', 'wedge', 'pyramid']
set_hcons = [1,2,3]
set_hname = [5,10,20,40,80]
lines=[[],[]]

for ele in ['wedge', 'tet', 'hex', 'pyramid']:
    
    if (ele=='hex'):
        set_p = [2, 4]
        set_mark = ['o', 'o']
        set_color = ['b','b']
        set_msize = [8,8]
        set_line = ['-','-']
    elif (ele=='wedge'):
        set_p = [2, 4]
        set_mark = ['^', '^']
        set_color = ['r','r']
        set_msize = [12,8]
        set_line = ['-','-']
    elif (ele=='tet'):
        set_p = [2, 4]
        set_mark = ['v', 'v']
        set_color = ['g','g']
        set_msize = [8,12]
        set_line = ['-','-']
    elif (ele=='pyramid'):
        set_p = [2, 4]
        set_mark = ['>', '>']
        set_color = ['c','c']
        set_msize = [9,9]
        set_line = ['-','-']

    for ip, p in enumerate(set_p):

        # ---------------------------------------------
        #  Read all the norms
        # ---------------------------------------------

        xvals = []
        yvals = []

        for h in set_hcons:
            comname = '%s_h%d_p%d' % (ele, h, p)
            fname = 'pp_data/%s.postproc' % comname
            xvals.append( set_hname[h] / set_hname[set_hcons[0]] )
            yvals.append( read_norms(fname) )

        # ---------------------------------------------
        #  Plot all the norms
        # ---------------------------------------------
        print xvals, yvals
        ln, = axs[ip].loglog(xvals, yvals,
                   marker=set_mark[ip],
                   markersize=set_msize[ip],
                   color= set_color[ip],
                   linewidth=2,
                   linestyle=set_line[ip])
        lines[ip].append(ln)

# ---------------------------------------------
#  Plot the reference line
# ---------------------------------------------
ln, = axs[0].loglog([1, xvals[-1]], [0.035, 0.035/xvals[-1]**2],
               color='k', linestyle='--', linewidth=1.5)
lines[0].append(ln)

axs[1].loglog([1, xvals[-1]], [0.01, 0.01/xvals[-1]**4],
               color='k', linestyle='--', linewidth=1.5)


# ---------------------------------------------
#  Text in plot
# ---------------------------------------------

axs[0].text(0.3, 0.1, r'$1$-exact',transform=axs[0].transAxes, fontsize=20)
axs[1].text(0.3, 0.1, r'$3$-exact',transform=axs[1].transAxes, fontsize=20)

# ---------------------------------------------
#  Nice plot
# ---------------------------------------------

ax = plt.gca()
for ax in axs:
    ax.set_xlim([0, 4])
    ax.set_ylim([1e-6, 1e-1])
    ax.tick_params(axis='x',which='minor',labelsize=20)
    ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter("%.0f"))
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.0f"))
    ax.tick_params(labelsize=20)
    ax.set_xlabel(r'$h/h_0$', fontsize=20)

axs[0].set_ylabel(r'$\|u-u_h\|_2$', fontsize=20)
fig.legend([lines[0][2], lines[0][3], lines[1][0], lines[0][1], lines[0][-1]],
           ['Hex', 'Prism', 'Pyramid+Tet', 'Tet', r'$h^{k+1}$'],
           fontsize=20)    

plt.show()
