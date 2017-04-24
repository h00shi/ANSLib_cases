#!/usr/bin/python

# WRITE THE FILE TO SOLVE THE a3 case:

for ii in [1, 2]:

    if (ii == 1):
        f = open('options/a3_medium.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/225-65/n0012_225-65\n')
        f.write('-B   MESH/225-65/n0012_225-65\n')
        f.write('-fec MESH/225-65/n0012_225-65\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_medium\n')
        f.write('-ita_history_name hst/a3_medium.hst\n')

    else:
        f = open('options/a3_coarse.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/113-33/n0012_113-33\n')
        f.write('-B   MESH/113-33/n0012_113-33\n')
        f.write('-fec MESH/113-33/n0012_113-33\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_coarse\n')
        # f.write('-sol          sol/a3_coarse\n')
        f.write('-ita_history_name hst/a3_coarse.hst\n')

    f.write('\n# --------------------------- ACCURACY\n')
    f.write('-a 3\n')

    f.write('\n# --------------------------- PHYSICS\n')
    f.write('-mesh_type c\n')
    f.write('-recon_condition\n')
    f.write('-physics RoeTurbSA2D\n')
    f.write('-d 2\n')
    f.write('-reynolds 6000000\n')
    f.write('-mach 0.15\n')
    f.write('-angle 10\n')

    f.write('\n# --------------------------- SOLVER OPTIONS\n')
    f.write('-C 0.01\n')
    f.write('-no_distance_weight\n')
    f.write('-pseudolts_fixed\n')
    f.write('-max_iter 100\n')
    f.write('-jacobian_type recanalytic\n')

    f.write('\n# --------------------------- KSP\n')
    f.write('-exnut 0\n')
    f.write('-ksp_max_it 500\n')
    f.write('-ksp_type fgmres\n')
    f.write('-ksp_converged_reason\n')
    f.write('-ksp_rtol 1e-3\n')
    f.write('-ita_target_residual 1e-5\n')

    f.write('\n# --------------------------- PC\n')
    f.write('-mu 1e-5\n')
    f.write('-vv 1\n')
    f.write('-pre_order 1\n')
    f.write('-pc_type   ksp\n')
    f.write('-ksp_ksp_type gmres\n')
    f.write('-ksp_ksp_max_it 5\n')
    f.write('-ksp_pc_type ilu\n')
    f.write('-ksp_pc_factor_levels 0\n')
    f.write('-ksp_pc_factor_mat_ordering_type lines\n')

    f.close()

# The cases that have to be generated:
# A^3 - QMD ILU(3)
# A^0 - (RCM, LINES, QMD) x (ksp, ansksp, only one)
#

mode = ['full', 'fullr', 'ksp', 'ansksp', 'onlyone']
ilutype = ['rcm', 'qmd', 'lines']

for mm in mode:
    for ii in ilutype:
        # if((mm == 'full') and (ii != 'qmd')):
        #    continue
        commname = mm + '_' + ii
        file_name = 'options/a4_medium_' + commname + '.opt'
        f = open(file_name, 'w')

        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/225-65/n0012_225-65\n')
        f.write('-B   MESH/225-65/n0012_225-65\n')
        f.write('-fec MESH/225-65/n0012_225-65\n')

        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol  sol/a3_medium\n')
        f.write('-sol_out sol/xxx\n')
        f.write('-ita_history_name ' + 'hst/a4_medium_' + commname + '.hst\n')

        f.write('\n# --------------------------- ACCURACY\n')
        f.write('-a 4\n')

        f.write('\n# --------------------------- PHYSICS\n')
        f.write('-mesh_type c\n')
        f.write('-recon_condition\n')
        f.write('-physics RoeTurbSA2D\n')
        f.write('-d 2\n')
        f.write('-reynolds 6000000\n')
        f.write('-mach 0.15\n')
        f.write('-angle 10\n')

        f.write('\n# --------------------------- SOLVER OPTIONS\n')
        f.write('-exnut 0\n')
        f.write('-C 0.01\n')
        f.write('-no_distance_weight\n')
        f.write('-pseudolts_fixed\n')
        f.write('-max_iter 80\n')
        f.write('-jacobian_type recanalytic\n')

        f.write('\n# --------------------------- KSP\n')
        f.write('-ksp_max_it 500\n')
        f.write('-ksp_converged_reason\n')
        f.write('-ksp_rtol 1e-3\n')
        f.write('-ita_target_residual 1e-5\n')
        if((mm == 'ansksp') or (mm == 'ksp')):
            f.write('-ksp_type fgmres\n')
        elif(mm == 'fullr'):
            f.write('-ksp_type gmres\n')
            f.write('-ksp_norm_type unpreconditioned\n')
        else:
            f.write('-ksp_type gmres\n')

        f.write('\n# --------------------------------- PC\n')

        if(ii == 'lines'):
            f.write('-mu 1e-5\n')
            f.write('-vv 1\n')

        if((mm == 'full') or (mm == 'fullr')):
            f.write('-pc_type ilu\n')
            f.write('-pc_factor_levels 3\n')
            f.write('-pc_factor_mat_ordering_type ' + ii + '\n')
        elif(mm == 'ksp'):
            f.write('-pre_order 1\n')
            f.write('-pc_type   ksp\n')
            f.write('-ksp_ksp_type gmres\n')
            f.write('-ksp_ksp_max_it 5\n')
            f.write('-ksp_pc_type ilu\n')
            f.write('-ksp_pc_factor_levels 0\n')
            f.write('-ksp_pc_factor_mat_ordering_type ' + ii + '\n')
        elif(mm == 'ansksp'):
            f.write('-pre_order 1\n')
            f.write('-pc_type   ansksp\n')
            f.write('-ansksp_ksp_type fgmres\n')
            f.write('-ansksp_ksp_max_it 5\n')
            f.write('-ansksp_pc_type ilu\n')
            f.write('-ansksp_pc_factor_levels 0\n')
            f.write('-ansksp_pc_factor_mat_ordering_type ' + ii + '\n')
        elif(mm == 'onlyone'):
            f.write('-pre_order 1\n')
            f.write('-pc_type ilu\n')
            f.write('-pc_factor_levels 0\n')
            f.write('-pc_factor_mat_ordering_type ' + ii + '\n')

        f.close()
