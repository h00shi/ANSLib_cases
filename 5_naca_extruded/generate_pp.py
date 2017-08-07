#!/usr/bin/python

import os

pset = [2,3,4]
mtype = [0,1]

if not os.path.exists('pp_data'):
    os.makedirs('pp_data')
if not os.path.exists('options'):
    os.makedirs('options')
if not os.path.exists('sol'):
    os.makedirs('sol')

# ----------------------------------------------------------------
# Curved
# ----------------------------------------------------------------
d = 3
for m in mtype:
    for p in pset:

        if(m==1):
            comname = 'T%d_p%d' % (d,p)
            file_name = 'options/' + comname + '_pptri.opt'
            meshname  = 'MESH/airfoilt'
        else:
            comname = 'D%d_p%d' % (d,p)
            file_name = 'options/' + comname + '_ppline.opt'
            meshname  = 'MESH/airfoil1'
            
        f = open(file_name, 'w')

        f.write('#---------------------------------- PHYSICS\n')
        f.write('-physics TurbSA3D\n')
        f.write('-d %d\n' % (d))
        f.write('-mesh_type e\n')
        f.write('-mext_nlayer %d \n' % (7) )
        f.write('-mext_btag 2 \n' )
        f.write('-mext_length 7 \n' )
        f.write('-mach 0.15\n')
        f.write('-reynolds 6e6\n')
        f.write('-angle 10\n')
        f.write('-turbsa3d_problem_data naca0012\n')
        if((m==1) and (p==4)): f.write('-mext_stencil_size 0,0,6,15,30\n')
        
        
        f.write('\n# --------------------------------- FILE NAMES\n')
        f.write('-f  %s \n'  % meshname)
        f.write('-fec %s \n' % meshname) 
        f.write('-B   %s \n' % meshname)                
        f.write('-sol sol/' + comname + '\n')
        f.write('-sol_out sol/alaki \n')
        
        f.write('-turbsa3d_pp_file pp_vtu/%s.postproc\n' % comname)
        
        f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
        f.write('-a ' + `p` + '\n')
        f.write('-mext_old_initrecon\n')
        
        f.close()
