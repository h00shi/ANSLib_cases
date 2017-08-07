#!/usr/bin/python

import os
import sys
import inspect
sys.path.insert(0, '../')

import history as hst
import matplotlib.pyplot as plt

if __name__ == "__main__":

    colors = ['b', 'g', 'r', 'm', 'k', 'c', 'y']
    symbols = ['o', '^', 'v', 's', 'd', 'p', 'h']
    labels = ['precon_1', 'precon_2', '3', '4', '5', '6', '7']
    jobs = []

    jobs.append(hst.ConvergenceHistory("hst/a4_fine_ksp_lines.hst"))
    jobs.append(hst.ConvergenceHistory("hst/a4_fine_osksp_lines.hst"))
    
    for j, c, l, s in zip(jobs, colors, labels, symbols):
        j.init_axis()

        ## LU CASE
        plt.figure(1)
        plt.semilogy(j.xaxis_nl, j.yaxis_l, c + '-', label=l,linewidth=2)
        plt.legend(loc='lower left', fontsize=10)
        plt.xlabel('PTC iteration')
        plt.ylabel('Number of GMRES iterations')
        plt.savefig('png/ilu1.png')
    
     
        plt.figure(2)
        plt.semilogy(j.yaxis_cumul, j.yaxis_res_nl[0], c + '-', label=l,linewidth=2)
        plt.legend(loc='lower left', fontsize=10)
        plt.xlabel('Total GMRES iterations')
        plt.ylabel('Nonlinear residual')
        plt.savefig('png/ilu2.png')

        plt.figure(3)
        plt.semilogy(j.yaxis_cpu, j.yaxis_res_nl[0], c + s + '-', label=l,linewidth=2)
        plt.legend(loc='lower left', fontsize=10)
        plt.xlabel('Time')
        plt.ylabel('Nonlinear residual')
        plt.savefig('png/ilu3.png')
  
    plt.show()
