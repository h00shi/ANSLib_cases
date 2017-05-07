#!/usr/bin/python

import os

for h in [4]:
    for p in [2,3,4]:
        
        comm = '~/code/ANSLib/hooshi/apps/shayans_playground/turbsa3d_post_processor  -physics Euler3D -a ' + `p` + ' -f MESH/sphere_m' + `h` + ' -sol sol/h'+ `h`+'_p' + `p`+ '_curve -out vtu/h' +`h` + '_p'+`p`+'_curve -mcell3d_sphere_hack 0 -mcell3d_extraq_cell 0 -mcell3d_extraq_face 0'

        os.system(comm)
