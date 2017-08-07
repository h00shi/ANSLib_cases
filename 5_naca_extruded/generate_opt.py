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
d = 3
for p in pset:
    comname = 'D' + `d` + '_p' + `p`
    file_name = 'options/' + comname + '_lines.opt'
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

    ksptype = 'ksp'
    
    # f.write('-mu 1e-5\n')
    # f.write('-vv 1\n')
    f.write('-pc_type %s\n' % ksptype)
    f.write('-%s_ksp_max_it 10\n' % ksptype)
    f.write('-%s_ksp_type gmres\n' % ksptype)
    f.write('-%s_pc_type bjacobi\n' % ksptype)
    f.write('-%s_sub_pc_type ilu\n' % ksptype)
    f.write('-%s_sub_pc_factor_levels 2\n' % ksptype)
    f.write('-%s_sub_pc_factor_mat_ordering_type rcm\n' % ksptype)
    f.write('-%s_sub_ksp_gmres_preallocate\n' % ksptype)

    f.write('-recon_condition\n')
    f.write('-C 0.01\n')
    f.write('-jacobian_type recanalytic\n')
    f.write('-pseudolts_fixed\n')
    f.write('-max_iter 150 \n')
    f.write('-no_distance_weight\n')
    if(p==2): f.write('-exnut 0\n')
    else:     f.write('-exnut 1\n') 
        
    f.write('\n# --------------------------------- FILE NAMES\n')
    f.write('-f   MESH/airfoil1 \n')
    f.write('-fec MESH/airfoil1 \n')
    f.write('-B   MESH/airfoil1 \n')
                
    if (p > 2):
        comname2 = 'D' + `d` + '_p' + `p - 1`
        f.write('-sol sol/' + comname2 + '\n')
    f.write('-sol_out sol/' + comname + '\n')
        
    f.write('-ita_history_name pp_data/' + comname + '_lines.hst\n')
    # f.write('-turbsa3d_pp_file pp_data/%s.postproc\n' % comname)
    
    f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
    f.write('-a ' + `p` + '\n')
    f.write('-ita_target_residual 1e-5\n')
    # f.write('-mcell3d_old_initrecon\n')

    f.close()
