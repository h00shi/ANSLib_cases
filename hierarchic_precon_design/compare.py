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
    labels = ['1', '2', '3', '4', '5', '6', '7']
    jobs = []

    # jobs.append(hst.ConvergenceHistory("hst/a3_medium_qmd3.hst"))
    # jobs.append(hst.ConvergenceHistory("hst/a4_medium_full_qmd.hst"))
    jobs.append(hst.ConvergenceHistory("hst/a4_medium_fullr_qmd.hst"))
    jobs.append(hst.ConvergenceHistory("hst/a4_medium_fullr_lines.hst"))
    jobs.append(hst.ConvergenceHistory("hst/a4_medium_fullr_rcm.hst"))

    # jobs.append(hst.ConvergenceHistory("hst/a4_medium_full_lines.hst"))
    # jobs.append(hst.ConvergenceHistory("hst/a4_medium_full_rcm.hst"))

    jobs.append(hst.ConvergenceHistory("hst/a4_medium_ansksp_qmd.hst"))
    # jobs.append(hst.ConvergenceHistory("hst/a4_medium_ksp_lines.hst"))
    # jobs.append(hst.ConvergenceHistory("hst/a4_medium_ansksp_lines.hst"))

    for j, c, l, s in zip(jobs, colors, labels, symbols):
        j.init_axis()

        plt.figure(1)
        plt.semilogy(j.yaxis_cpu, j.yaxis_res_nl[0], c + s + '-', label=l)
        # plt.semilogy(j.xaxis_l_cpu, j.yaxis_res_l, c + '-')

        plt.figure(2)
        plt.semilogy(j.xaxis_nl, j.yaxis_res_nl[0], c + s + '--', label=l)
        # plt.semilogy(j.xaxis_l, j.yaxis_res_l, c + '-')

        plt.figure(3)
        plt.semilogy(j.yaxis_cpu, j.yaxis_cumul, c + '--', label=l)

        plt.figure(4)
        plt.semilogy(j.xaxis_nl, j.yaxis_l, c + s + '--', label=l)

    # -------
    plt.figure(1)
    # plt.title(file_title)
    plt.legend(loc='upper right', fontsize=10)
    plt.xlabel('CPU time')
    plt.ylabel('Residuals')

   # plt.savefig(file_name + '-time.png')

    # -------
    plt.figure(2)
    # plt.title(file_title)
    plt.legend(loc='upper right', fontsize=10)
    plt.xlabel('# NLI')
    plt.ylabel('Residuals')

    # plt.savefig(file_name + '-it.png')

    plt.show()
