#!/usr/bin/python

import os

for h in [3]:
    for p in [3,4]:
        
        comm = 'mpiexec -np 7 ~/code/ANSLib/hooshi/apps/shayans_playground/turbsa3d_post_processor -d 3 -physics TurbSA3D -a %d -f MESH/plate_m%d -sol sol/h%d_p%d -turbsa3d_pp_file pp_data/h%d_p%d.serial.postproc -turbsa3d_problem_data flat_plate -mach 0.2 -reynolds 5e6 -mcell3d_old_initrecon' % (
            p, h, h,p, h,p)
        print comm
        os.system(comm)
