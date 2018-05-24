#!/usr/bin/python

import sys; sys.path.insert(0, '../')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

import anslib_plot_tools.history as hst
import anslib_plot_tools.io as io
import anslib_plot_tools.ansplot as aplt

def plot_history_separate(ch, plt_options):
    """Plot the convergence history on separate plots. """

    ch.init_axis()
    plt_options_no_marker = plt_options.copy()
    plt_options_no_marker.pop('marker')
    
    plt.figure(1)
    plt.semilogy(ch.xaxis_nl, ch.yaxis_l, **plt_options_no_marker)
    plt.legend(loc='lower left', fontsize=10)
    plt.xlabel('PTC iteration')
    plt.ylabel('Number of GMRES iterations')
    plt.savefig('png/ilu1.png')
    
    plt.figure(2)
    plt.semilogy(ch.yaxis_cumul, ch.yaxis_res_nl[0], **plt_options_no_marker)
    plt.legend(loc='lower left', fontsize=10)
    plt.xlabel('Total GMRES iterations')
    plt.ylabel('Nonlinear residual')
    plt.savefig('png/ilu2.png')
    
    plt.figure(3)
    plt.semilogy(ch.yaxis_cpu, ch.yaxis_res_nl[0],  **plt_options)
    plt.legend(loc='lower left', fontsize=10)
    plt.xlabel('Time')
    plt.ylabel('Nonlinear residual')
    plt.savefig('png/ilu3.png')


def plot_history_combined(ch, ax=None, plt_options={}):
    """Plot the convergence history on a single plot.

* Input:

    ch, the convergence history object
    ax, axis to plot on
    plt_options, dictionary of options to be passed to matplotlib

* Axis with colors:

    https://matplotlib.org/examples/api/two_scales.html

* More than three axis:

    https://matplotlib.org/examples/axes_grid/demo_parasite_axes2.html

    https://stackoverflow.com/questions/9103166/multiple-axis-in-matplotlib-with-different-scales?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

    """
    ch.init_axis()
    plt_options_no_marker = plt_options.copy()
    plt_options_no_marker.pop('marker', 's')

    if(ax is None): ax = plt.gca()
    fig = ax.get_figure()

    c1 = plt.cm.viridis(0)
    c2 = plt.cm.viridis(0.3)
    c3 = plt.cm.viridis(.7)
    c4 = plt.cm.viridis(.9)

    ax1 = ax; aplt.change_axis_color(ax1, c1, 'y', 'left') 
    ax2 = aplt.add_axis_twinx(ax1, 0, c2)
    ax3 = aplt.add_axis_twinx(ax1, 60, c3)
    ax4 = aplt.add_axis_twinx(ax1, 120, c4)

    ax1.semilogy(ch.xaxis_nl, ch.yaxis_res_nl[0], color=c1)
    ax2.semilogy(ch.xaxis_nl, ch.yaxis_cfl, color=c2)
    ax3.plot(ch.xaxis_nl, ch.yaxis_cpu, color=c3)
    ax4.plot(ch.xaxis_nl, ch.yaxis_l, color=c4)
    
    ax1.set_xlabel("PTC iteration")
    ax1.set_ylabel("Residual", color=c1)
    ax1.tick_params(size=5)
    #
    ax2.set_ylabel("CFL", color=c2)
    # ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    ax2.tick_params(size=5)
    #
    ax3.set_ylabel("Time", color=c3)
    ax3.yaxis.set_major_formatter(FormatStrFormatter('%.1e'))
    ax3.tick_params(size=5)
    #
    ax4.set_ylabel("GMRES Iter", color=c4)
    ax4.tick_params(size=5)

    fig.tight_layout() # Works rather well.
    plt.savefig("pyplot_multiple_y-axis.png", bbox_inches='tight')    

## ========================================================
##    MAIN
## ========================================================
def main():
    
    colors = ['b', 'g', 'r', 'm', 'k', 'c', 'y']
    symbols = ['o', '^', 'v', 's', 'd', 'p', 'h']
    labels = ['precon_1', 'precon_2', '3', '4', '5', '6', '7']
    jobs = []

    # jobs.append(hst.ConvergenceHistory("hst/a4_fine_ksp_lines.hst"))
    jobs.append(hst.ConvergenceHistory("hst/a4_fine_lo-lu-mumps-right_rcm.0.hst"))
    
    for (j, c, l, s) in zip(jobs, colors, labels, symbols):
        # plot_history_separate(j, dict(color=c, label=l, marker=s) )
        plot_history_combined(ch=j, plt_options=dict(color=c, label=l, marker=s) )      
    plt.show()
    
if __name__ == "__main__":
    main()        
