#!/usr/bin/python

import sys
import getopt
import numpy as np
import matplotlib.pyplot as plt


def skip_comments(lines, nline):
    " Get the next line from a set of commented lines "

    success = 0

    # get the first uncommented line
    for line in lines[nline:]:
        line = line.split('#', 1)[0]
        line = line.rstrip()
        nline = nline + 1
        if line == '':
            continue
        success = 1
        return line, nline

    if (success == 0):
        return None, -1


class ConvergenceHistory:
    "Class to store convergence history data"

    def __init__(self, inputfile):

        # -----------------------
        # members
        # ----------------------

        self.n_unknowns = 0
        self.n_sum_linear = 0
        self.n_nonlinear = 0
        self.res_nonlinear = [[], [], [], [], [], [], [], [], [], []]
        self.cfl = []
        self.cpu = []
        self.x_linear = [0]
        self.n_linear = []
        self.res_linear = []

        self.xaxis_nl = []
        self.xaxis_l = []
        self.xaxis_l_cpu = []
        self.yaxis_cfl = []
        self.yaxis_cpu = []
        self.yaxis_res_l = []
        self.yaxis_res_nl = []
        self.yaxis_l = []

        # -----------------------
        # open the file and start reading
        # ----------------------

        # open
        f = open(inputfile, "r")
        lines = f.readlines()
        nline = 0

        # read for every non-linear
        while (1):

            # read cfl, cpu and nonlinear residual
            # and check if we have finished reading the file
            line, nline = skip_comments(lines, nline)
            if(nline == -1):
                break
            line = line.split(" ")
            self.cfl.append(float(line[0]))

            line, nline = skip_comments(lines, nline)
            line = line.split(" ")
            self.cpu.append(float(line[0]))

            line, nline = skip_comments(lines, nline)
            line = line.split(" ")
            self.n_unknowns = int(line[0])
            for i in range(0, self.n_unknowns + 1):
                self.res_nonlinear[i].append(float(line[i + 1]))

            # read number of iteration
            line, nline = skip_comments(lines, nline)
            line = line.split(" ")
            niter = int(line[0])
            self.n_linear.append(niter)
            self.x_linear.append(self.x_linear[-1] + niter)

            # read the linear iterations
            for il in range(0, niter):
                line, nline = skip_comments(lines, nline)
                line = line.split(" ")
                self.res_linear.append(float(line[0]))

            # close
            f.close()

        # calculate the linear and nonlinear total
        self.n_nonlinear = len(self.res_nonlinear[0])
        self.n_sum_linear = len(self.res_linear)

    def init_axis(self):
        "Create data for plots"

        # non linear residual
        self.xaxis_nl = np.arange(1, self.n_nonlinear + 1)
        for i in range(0, self.n_unknowns + 1):
            self.yaxis_res_nl.append(np.array(self.res_nonlinear[i]))

        # linear residual
        self.xaxis_l = np.zeros(self.n_sum_linear)
        self.xaxis_l_cpu = np.zeros(self.n_sum_linear)

        cnt = 0
        for i in range(0, self.n_nonlinear):

            if (i == 0):
                cpu_prev = 0
            else:
                cpu_prev = self.cpu[i - 1]
            cpu_diff = self.cpu[i] - cpu_prev

            for j in range(self.x_linear[i], self.x_linear[i + 1]):

                prog = (float(j) - self.x_linear[i]) / self.n_linear[i]
                self.xaxis_l_cpu[cnt] = cpu_prev + prog * cpu_diff
                self.xaxis_l[cnt] = float(i) + prog
                cnt = cnt + 1

        self.yaxis_res_l = np.array(self.res_linear)

        # number of iterations
        self.yaxis_l = np.array(self.n_linear)

        # CFL
        self.yaxis_cfl = np.array(self.cfl)

        # CPU
        self.yaxis_cpu = np.array(self.cpu)

    def plot(self):
        "Draw the plots"

        plt.figure(1)
        plt.hold(1)
        plt.xlabel('cpu time')
        plt.ylabel('residual')
        plt.semilogy(self.xaxis_nl,  self.yaxis_res_nl, 'o-')
        plt.semilogy(self.xaxis_l,  self.yaxis_res_l, 'r--')

        plt.figure(2)
        plt.xlabel('cpu time')
        plt.ylabel('# LI per # NLI')
        plt.plot(self.yaxis_cpu, self.yaxis_l, 'o--')

        # plt.figure(3)
        # plt.title('CFL')
        # plt.semilogy(self.xaxis_nl, self.yaxis_cfl, 'o--')

        # plt.figure(4)
        # plt.title('CPU time')
        # plt.plot(self.xaxis_nl, self.yaxis_cpu, 'o--')

        plt.show()


def main(argv):
    " The main function "

    # -----------------------
    #  get the file name from command line
    # ----------------------

    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "i:", ["input="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
    print 'Input file is ', inputfile

    # -----------------------
    #  get the history
    # -----------------------
    hist = ConvergenceHistory(inputfile)
    hist.init_axis()
    hist.plot()

if __name__ == "__main__":
    main(sys.argv[1:])
