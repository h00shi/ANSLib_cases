#!/usr/bin/python

import os

# clevel
# n_ez
# out

fpd =  '/home/hooshi/code/threed_quadrature/flat_plate_opt '
os.system( fpd + ' clevel=2 n_ez=7 out=plate_m3x7 ')
os.system( fpd + ' clevel=3 n_ez=7 out=plate_m2x7 ')
os.system( fpd + ' clevel=4 n_ez=7 out=plate_m1x7 ')

os.system( fpd + ' clevel=2 n_ez=14 out=plate_m3x14 ')
os.system( fpd + ' clevel=3 n_ez=14 out=plate_m2x14 ')
os.system( fpd + ' clevel=4 n_ez=14 out=plate_m1x14 ')

os.system( fpd + ' clevel=2 n_ez=28 out=plate_m3x28 ')
os.system( fpd + ' clevel=3 n_ez=28 out=plate_m2x28 ')
os.system( fpd + ' clevel=4 n_ez=28 out=plate_m1x28 ')
