#!/usr/bin/python

import os
import sys
import inspect
sys.path.insert(0, '/home/hooshi/code/ANSLib/ANSLib_cases/')

import history as hst
import matplotlib.pyplot as plt

if __name__ == "__main__":

    colors = ['b', 'g', 'r', 'm', 'k']
    jobs = []

    #jobs.append(hst.ConvergenceHistory("pp_data/D2_p2.hst"))
    #jobs.append(hst.ConvergenceHistory("pp_data/D2_p3.hst"))
    jobs.append(hst.ConvergenceHistory("pp_data/D2_p2.hst"))
    jobs.append(hst.ConvergenceHistory("pp_data/D2_p2_qmd.hst"))
    jobs.append(hst.ConvergenceHistory("pp_data/D2_p2_lines.hst"))

    #jobs.append(hst.ConvergenceHistory("pp_data/D3_p2.hst"))

    labels = ['a2', 'a3', 'a4', 'a4', 'x']

    # file_name = 'img/rusanov_un-hst-' + sys.argv[1]
    cv_no = ['28608', '36630', '87155']
    # file_title = 'Rusanov(Lax), #CV =' + cv_no[int(sys.argv[1]) - 1] + ', a4'

    for j, c, l in zip(jobs, colors, labels):
        j.init_axis()

        plt.figure(1)
        plt.semilogy(j.yaxis_cpu, j.yaxis_res_nl[0],
                     c + 'o--', label=l)
        # plt.semilogy(j.xaxis_l_cpu, j.yaxis_res_l, c + '-')

        plt.figure(2)
        plt.semilogy(j.xaxis_nl, j.yaxis_res_nl[0], c + 'o--', label=l)
        plt.semilogy(j.xaxis_l, j.yaxis_res_l, c + '-')

    # -------
    plt.figure(1)
    # plt.title(file_title)
    plt.legend(loc='upper right')
    plt.xlabel('CPU time')
    plt.ylabel('Residuals')

   # plt.savefig(file_name + '-time.png')

    # -------
    plt.figure(2)
    # plt.title(file_title)
    plt.legend(loc='upper right')
    plt.xlabel('# NLI')
    plt.ylabel('Residuals')

    # plt.savefig(file_name + '-it.png')

    plt.show()
