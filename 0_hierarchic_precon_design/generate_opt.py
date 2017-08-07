#!/usr/bin/python

# WRITE THE FILE TO SOLVE THE a3 case:

for ii in [1, 2, 3, 4]:

    if (ii == 1):
        f = open('options/a3_coarse.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/113-33/n0012_113-33\n')
        f.write('-B   MESH/113-33/n0012_113-33\n')
        f.write('-fec MESH/113-33/n0012_113-33\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_coarse\n')
        # f.write('-sol          sol/a3_coarse\n')
        f.write('-ita_history_name hst/a3_coarse.hst\n')

    elif (ii == 2):
        f = open('options/a3_medium.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/225-65/n0012_225-65\n')
        f.write('-B   MESH/225-65/n0012_225-65\n')
        f.write('-fec MESH/225-65/n0012_225-65\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_medium\n')
        f.write('-ita_history_name hst/a3_medium.hst\n')

    elif (ii == 3):
        f = open('options/a3_fine.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/449-129/n0012_449-129\n')
        f.write('-B   MESH/449-129/n0012_449-129\n')
        f.write('-fec MESH/449-129/n0012_449-129\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_fine\n')
        f.write('-ita_history_name hst/a3_fine.hst\n')

    elif (ii == 4):
        f = open('options/a3_sfine.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/897-257/n0012_897-257\n')
        f.write('-B   MESH/897-257/n0012_897-257\n')
        f.write('-fec MESH/897-257/n0012_897-257\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_sfine\n')
        f.write('-ita_history_name hst/a3_sfine.hst\n')

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
    if(ii == 4):
        f.write('-ksp_ksp_max_it 40\n')
    else:
        f.write('-ksp_ksp_max_it 5\n')
        f.write('-ksp_pc_type ilu\n')
        f.write('-ksp_pc_factor_levels 0\n')
        f.write('-ksp_pc_factor_mat_ordering_type lines\n')

    f.close()

# The cases that have to be generated:
# A^3 - QMD ILU(3)
# A^0 - (RCM, LINES, QMD) x (ksp, ansksp, only one)
#

#mode = ['full', 'fullr', 'ksp', 'ansksp', 'onlyone', 'exact']
mode = ['full',  'exact', 'osexact', 'ksp', 'osksp']
ilutype = ['rcm', 'qmd', 'lines']

ksp_inner_it = ['', '10', '10', '40']
mesh_name = ['', 'MESH/225-65/n0012_225-65',
             'MESH/449-129/n0012_449-129', 'MESH/897-257/n0012_897-257']
hst_name = ['', 'medium', 'fine', 'sfine']

for msize in [1, 2, 3]:
    for mm in mode:
        for ii in ilutype:

            if((msize == 3) and (mm != 'ksp') and (ii != 'lines')):
                continue

            commname = hst_name[msize] + '_' + mm + '_' + ii
            file_name = 'options/a4_' + commname + '.opt'
            f = open(file_name, 'w')

            f.write('\n# --------------------------- MESH\n')
            f.write('-f ' + mesh_name[msize] + '\n')
            f.write('-B ' + mesh_name[msize] + '\n')
            f.write('-fec ' + mesh_name[msize] + '\n')

            f.write('\n# -------------------- HISTORY AND SOLUTION FILE NAME\n')
            f.write('-sol  sol/a3_' + hst_name[msize] + '\n')
            f.write('-sol_out sol/xxx\n')
            f.write('-ita_history_name  hst/a4_' + commname + '.hst\n')

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
            f.write('-exnut 1\n')
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

            if((mm == 'osksp') or (mm == 'ksp')):
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
            elif(mm == 'exact'):
                f.write('-pre_order 1\n')
                f.write('-pc_type lu\n')
                f.write('-pc_factor_mat_ordering_type ' + ii + '\n')
            elif(mm == 'osexact'):
              f.write('-only_source_recon 1\n')
              f.write('-pre_order 2\n')
              f.write('-pc_type lu\n')
              f.write('-pc_factor_mat_ordering_type ' + ii + '\n')
            elif(mm == 'ksp'):
                f.write('-pre_order 1\n')
                f.write('-pc_type   ksp\n')
                f.write('-ksp_ksp_type gmres\n')
                f.write('-ksp_ksp_max_it ' + ksp_inner_it[msize] + '\n')
                f.write('-ksp_pc_type ilu\n')
                f.write('-ksp_pc_factor_levels 0\n')
                f.write('-ksp_pc_factor_mat_ordering_type ' + ii + '\n')
            elif(mm == 'osksp'):
                f.write('-only_source_recon 1\n')
                f.write('-pre_order 2\n')
                f.write('-pc_type   ksp\n')
                f.write('-ksp_ksp_type gmres\n')
                f.write('-ksp_ksp_max_it ' + ksp_inner_it[msize] + '\n')
                f.write('-ksp_pc_type ilu\n')
                f.write('-ksp_pc_factor_levels 0\n')
                f.write('-ksp_pc_factor_mat_ordering_type ' + ii + '\n')
            elif(mm == 'onlyone'):
                f.write('-pre_order 1\n')
                f.write('-pc_type ilu\n')
                f.write('-pc_factor_levels 0\n')
                f.write('-pc_factor_mat_ordering_type ' + ii + '\n')

            f.close()
