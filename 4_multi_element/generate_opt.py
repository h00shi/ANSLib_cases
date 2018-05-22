#!/usr/bin/python

import os

pset = [2,3,4]
hset = [1]

if not os.path.exists('pp_data'):
    os.makedirs('pp_data')
if not os.path.exists('options'):
    os.makedirs('options')
if not os.path.exists('sol'):
    os.makedirs('sol')

# ----------------------------------------------------------------
# Curved
# ----------------------------------------------------------------
d = 2
for p in pset:
    comname = 'D' + `d` + '_p' + `p`
    file_name = 'options/' + comname + '.opt'
    f = open(file_name, 'w')

    f.write('#---------------------------------- PHYSICS\n')
    f.write('-physics TurbSA3D\n')
    f.write('-d %d\n' % (d))
    f.write('-mesh_type e\n')
    f.write('-mext_nlayer %d \n' % (7*2**(h-1)) )
    f.write('-mext_btag 2 \n' )
    f.write('-mext_length 7 \n' )
    f.write('-mach 0.2\n')
    f.write('-reynolds 9e6\n')
    f.write('-angle 16\n')
    # f.write('-turbsa3d_problem_data flat_plate\n')
        
    f.write('\n# --------------------------------- SOLVER OPTIONS\n')
    f.write('-ksp_type fgmres\n')
    f.write('-ksp_norm_type unpreconditioned\n')
    f.write('-ksp_rtol 1e-3\n')
    f.write('-ksp_gmres_preallocate\n')
    f.write('-ksp_gmres_restart 100\n')
    f.write('-ksp_max_it 500\n')
    f.write('-pre_order 1\n')
    f.write('-ksp_gmres_preallocate\n')
        
    f.write('-pc_type ksp\n')
    f.write('-ksp_ksp_max_it 20\n')
    f.write('-ksp_ksp_type gmres\n')
    f.write('-ksp_pc_type bjacobi\n')
    f.write('-ksp_sub_pc_type ilu\n')
    f.write('-ksp_sub_pc_factor_levels 2\n')
    f.write('-ksp_sub_pc_factor_mat_ordering_type rcm\n')
    f.write('-ksp_sub_ksp_gmres_preallocate\n')
  
        
    f.write('\n# --------------------------------- FILE NAMES\n')
    f.write('-f MESH/plate_m%d \n' % h)
    f.write('-mcell3d_part_file MESH/plate_m%d\n' % h)
                
    if (p > 2):
        comname2 = 'h' + `h` + '_p' + `p - 1`
        f.write('-sol sol/' + comname2 + '\n')
    f.write('-sol_out sol/' + comname + '\n')
        
    f.write('-ita_history_name pp_data/' + comname + '.hst\n')
    f.write('-turbsa3d_pp_file pp_data/%s.postproc\n' % comname)
    
    f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
    f.write('-a ' + `p` + '\n')
    f.write('-ita_target_residual 1e-5\n')
    # f.write('-mcell3d_old_initrecon\n')

    f.close()
