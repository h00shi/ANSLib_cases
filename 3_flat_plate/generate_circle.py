#!/usr/bin/python

import numpy as np

n_points = 100

f = open('circle.vtk', 'w')

f.write('# vtk DataFile Version 2.0\n')
f.write('Unit Circle\n')
f.write('ASCII\n')
f.write('DATASET POLYDATA\n')

f.write('\nPOINTS %d float\n' % n_points)
for p in range(0, n_points):
    theta = np.pi * 2. * p / n_points
    xp = np.cos(theta)
    yp = np.sin(theta)
    f.write('%lf %lf 0\n' % (xp, yp) )
    
f.write('\nPOLYGONS 1 %d\n' % (n_points+1) )
f.write('%d ' % n_points)
for p in range(0, n_points):
    f.write('%d ' % p)

f.write('\n')    
f.close()
