#!/usr/bin/python

import os

pset = [2,3,4]

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
    f.write('-physics RoeTurbSA2D\n')
    f.write('-d %d\n' % (d))
    f.write('-mesh_type c\n')
    f.write('-mach 0.2\n')
    f.write('-reynolds 9e6\n')
    f.write('-angle 16\n')
    # f.write('-turbsa3d_problem_data flat_plate\n')
        
    f.write('\n# --------------------------------- SOLVER OPTIONS\n')

    f.write('-ksp_type gmres\n')
    f.write('-ksp_norm_type preconditioned\n')
    f.write('-ksp_rtol 1e-3\n')
    f.write('-ksp_gmres_preallocate\n')
    f.write('-ksp_gmres_restart 100\n')
    f.write('-ksp_max_it 500\n')
    f.write('-pc_type bjacobi\n')
    f.write('-sub_pc_type ilu\n')
    f.write('-sub_pc_factor_levels 3\n')
    f.write('-sub_pc_factor_mat_ordering_type qmd\n')


    f.write('-recon_condition\n')
    f.write('-C 0.01\n')
    f.write('-jacobian_type recanalytic\n')
    f.write('-pseudolts_fixed\n')
    if(p==2): f.write('-max_iter 130\n')
    else:     f.write('-max_iter 100 \n')
    f.write('-no_distance_weight\n')
    f.write('-exnut 0\n')

        
    f.write('\n# --------------------------------- FILE NAMES\n')
    f.write('-f   MESH/badpart/multi \n')
    f.write('-fec MESH/badpart/multi \n')
    f.write('-B   MESH/badpart/multi \n')
                
    if (p > 2):
        comname2 = 'D' + `d` + '_p' + `p - 1`
        f.write('-sol sol/' + comname2 + '\n')
    f.write('-sol_out sol/' + comname + '\n')
        
    f.write('-ita_history_name pp_data/' + comname + '_qmd.hst\n')
    # f.write('-turbsa3d_pp_file pp_data/%s.postproc\n' % comname)
    
    f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
    f.write('-a ' + `p` + '\n')
    f.write('-ita_target_residual 1e-5\n')
    # f.write('-mcell3d_old_initrecon\n')

    f.close()
