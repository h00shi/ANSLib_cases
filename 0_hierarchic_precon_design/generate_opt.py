#!/usr/bin/python

# WRITE THE FILE TO SOLVE THE a3 case:
import sys; sys.path.insert(0, '../')
import history as hst
import os

def write_hst(f, name):
    # name = '{}/{}'.format(os.getcwd(),name)
    name = hst.append_number_to_name(name)
    # print name, ": ", os.path.isfile(name)
    f.write( '-ita_history_name {}\n'.format(name) )

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
        #f.write('-ita_history_name hst/a3_coarse.hst\n')
        write_hst(f,'hst/a3_coarse.hst')

    elif (ii == 2):
        f = open('options/a3_medium.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/225-65/n0012_225-65\n')
        f.write('-B   MESH/225-65/n0012_225-65\n')
        f.write('-fec MESH/225-65/n0012_225-65\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_medium\n')
        #f.write('-ita_history_name hst/a3_medium.hst\n')
        write_hst(f,'hst/a3_medium.hst')

    elif (ii == 3):
        f = open('options/a3_fine.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/449-129/n0012_449-129\n')
        f.write('-B   MESH/449-129/n0012_449-129\n')
        f.write('-fec MESH/449-129/n0012_449-129\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_fine\n')
        # f.write('-ita_history_name hst/a3_fine.hst\n')
        write_hst(f,'hst/a3_fine.hst')

    elif (ii == 4):
        f = open('options/a3_sfine.opt', 'w')
        f.write('\n# --------------------------- MESH\n')
        f.write('-f   MESH/897-257/n0012_897-257\n')
        f.write('-B   MESH/897-257/n0012_897-257\n')
        f.write('-fec MESH/897-257/n0012_897-257\n')
        f.write('\n# --------------------------- HISTORY AND SOLUTION FILE NAME\n')
        f.write('-sol_out          sol/a3_sfine\n')
        # f.write('-ita_history_name hst/a3_sfine.hst\n')
        write_hst(f,'hst/a3_fine.hst')

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


# OS: only source, it seems useless.
#mode = ['full', 'fullr', 'ksp', 'ansksp', 'onlyone', 'exact']
mode = ['ho-ilu-left', 'ho-ilu-right',
        'lo-ilu-left', 'lo-ilu-right',
        'gmres-lo-ilu',
        'lo-lu-mumps-left', 'lo-lu-mumps-right',
        'lo-lu-petsc-left', 'lo-lu-petsc-right']

reordertype = ['rcm', 'qmd', 'lines']

ksp_inner_it = ['', '10', '10', '40']
mesh_name = ['', 'MESH/225-65/n0012_225-65',
             'MESH/449-129/n0012_449-129', 'MESH/897-257/n0012_897-257']
hst_name = ['', 'medium', 'fine', 'sfine']

def _write_opt_file(_reordertype, _msize, _mode):
    # if((_msize == 3) and (_mode != 'ksp') and (_reordertype  != 'lines')):
    #     return
    
    commname = hst_name[_msize] + '_' + _mode + '_' + _reordertype 
    file_name = 'options/a4_' + commname + '.opt'
    f = open(file_name, 'w')

    f.write('\n# --------------------------- MESH\n')
    f.write('-f ' + mesh_name[_msize] + '\n')
    f.write('-B ' + mesh_name[_msize] + '\n')
    f.write('-fec ' + mesh_name[_msize] + '\n')

    f.write('\n# -------------------- HISTORY AND SOLUTION FILE NAME\n')
    f.write('-sol  sol/a3_' + hst_name[_msize] + '\n')
    f.write('-sol_out sol/xxx\n')
    # f.write('-ita_history_name  hst/a4_' + commname + '.hst\n')
    write_hst(f,'hst/a4_{}.hst'.format(commname) )

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

    ## We want left preconditioning.
    if('left' in _mode):
        f.write('-ksp_type gmres\n')
    ## We want right preconditioning with memory conservation.
    elif('right' in _mode):
        f.write('-ksp_type gmres\n')
        f.write('-ksp_norm_type unpreconditioned\n')
    ## We want right preconditioning, but we have to pay the penalty of
    ## the double memory consumption of fgmres.
    else:
        f.write('-ksp_type fgmres\n')

        
    f.write('\n# --------------------------------- PC\n')
    if(_reordertype  == 'lines'):
        f.write('-mu 1e-5\n')
        f.write('-vv 1\n')

    if('gmres-lo-ilu' == _mode):
        f.write('-pre_order 1\n')
        f.write('-pc_type   ksp\n')
        f.write('-ksp_ksp_type gmres\n')
        f.write('-ksp_ksp_max_it ' + ksp_inner_it[_msize] + '\n')
        f.write('-ksp_pc_type ilu\n')
        f.write('-ksp_pc_factor_levels 0\n')
        f.write('-pc_factor_mat_ordering_type {} \n'.format(_reordertype))
    elif('ho-ilu-' in _mode):
        f.write('-pc_type ilu\n')
        f.write('-pc_factor_levels 3\n')
        f.write('-pc_factor_mat_ordering_type {} \n'.format(_reordertype))
    elif('lo-ilu-' in _mode):
        f.write('-pre_order 1\n')
        f.write('-pc_type ilu\n')
        f.write('-pc_factor_levels 0\n')
        f.write('-pc_factor_mat_ordering_type {} \n'.format(_reordertype))
    elif('lo-lu-petsc-' in _mode):
        f.write('-pre_order 1\n')
        f.write('-pc_type lu\n')
        f.write('-pc_factor_mat_ordering_type {} \n'.format(_reordertype))
    elif('lo-lu-mumps-' in _mode):
        f.write('-pre_order 1\n')
        f.write('-pc_type lu\n')
        f.write('-pc_factor_mat_solver_type mumps \n')
        f.write('-pc_factor_mat_ordering_type {} \n'.format(_reordertype))
    else:
        assert(0)
      
    # Garbage
    # elif(_mode == 'osexact'):
    #     f.write('-only_source_recon 1\n')
    #     f.write('-pre_order 2\n')
    #     f.write('-pc_type lu\n')
    #     f.write('-pc_factor_mat_ordering_type ' + _reordertype  + '\n')
    # elif(_mode == 'osksp'):
    #     f.write('-only_source_recon 1\n')
    #     f.write('-pre_order 2\n')
    #     f.write('-pc_type   ksp\n')
    #     f.write('-ksp_ksp_type gmres\n')
    #     f.write('-ksp_ksp_max_it ' + ksp_inner_it[_msize] + '\n')
    #     f.write('-ksp_pc_type ilu\n')
    #     f.write('-ksp_pc_factor_levels 0\n')
    #     f.write('-ksp_pc_factor_mat_ordering_type ' + _reordertype  + '\n')
    
    f.close()

for _msize in [1, 2, 3]:
    for _mode in mode:
        for _reordertype in reordertype:
            _write_opt_file(_reordertype, _msize, _mode)
