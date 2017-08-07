#!/usr/bin/python

import os

set_p = [2,3,4]
set_ele = ['hex', 'tet', 'wedge', 'pyramid']
set_hname = ['5','10','20','40','80']

if not os.path.exists('pp_data'):
    os.makedirs('pp_data')
if not os.path.exists('options'):
    os.makedirs('options')
if not os.path.exists('sol'):
    os.makedirs('sol')

# ----------------------------------------------------------------
# Curved
# ----------------------------------------------------------------
for ele in set_ele:
    for p in set_p:
        for h in range(len(set_hname)):
            comname = '%s_h%d_p%d' % (ele, h, p)
            file_name = 'options/%s.opt' % comname
            f = open(file_name, 'w')
            
            f.write('#---------------------------------- PHYSICS\n')
            f.write('-physics Poisson\n')
            f.write('-d 3\n')
            f.write('-mesh_type c\n')
            f.write('-poisson_problem_data sinhsin\n')
    
            f.write('\n# --------------------------------- SOLVER OPTIONS\n')
            f.write('-ksp_type gmres\n')
            f.write('-ksp_norm_type preconditioned\n')
            f.write('-ksp_rtol 1e-12\n')
            f.write('-ksp_gmres_preallocate\n')
            f.write('-ksp_gmres_restart 50\n')
            f.write('-ksp_max_it 300\n')
            f.write('-pre_order 1\n')
            f.write('-ksp_gmres_preallocate\n')
            f.write('-pc_type sor\n')
            f.write('-pc_sor_its 10\n')

            f.write('-recon_condition\n')
            f.write('-C 1e10\n')
            f.write('-jacobian_type recanalytic\n')
            f.write('-pseudolts_fixed\n')
            f.write('-max_iter 3 \n')
            f.write('-no_distance_weight\n')
            
            f.write('\n# --------------------------------- FILE NAMES\n')
            f.write('-f   MESH/%s_%s \n' % (ele, set_hname[h]))
            f.write('-sol_out sol/%s\n' % comname)
            f.write('-ita_history_name pp_data/%s.hst\n' % comname)
            f.write('-poisson_norm_file pp_data/%s.postproc\n' % comname)
            
            f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
            f.write('-a %d\n' % p)
            f.write('-ita_target_residual 1e-10\n')
            f.write('-mcell3d_old_initrecon\n')
        
            f.close()
