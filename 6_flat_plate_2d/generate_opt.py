#!/usr/bin/python

# WRITE THE FILE TO SOLVE THE a3 case:
import sys; sys.path.insert(0, '../')
import os

import anslib_plot_tools.io as io

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def write_hst(f, name):
    # name = '{}/{}'.format(os.getcwd(),name)
    name = io.append_number_to_name(name)
    # print name, ": ", os.path.isfile(name)
    f.write( '-ita_history_name {}\n'.format(name) )


def _write_opt_file(_a, _reordertype, _msize, _mode):
    # if((_msize == 3) and (_mode != 'ksp') and (_reordertype  != 'lines')):
    #     return
    
    commname = hst_name[_msize] + '_' + _mode + '_' + _reordertype 
    file_name = 'options/a{}_{}.opt'.format(_a, commname)
    f = open(file_name, 'w')

    f.write('\n# --------------------------- MESH\n')
    f.write('-f ' + mesh_name[_msize] + '\n')
    # f.write('-B ' + mesh_name[_msize] + '\n')
    # f.write('-fec ' + mesh_name[_msize] + '\n')

    f.write('\n# -------------------- HISTORY AND SOLUTION FILE NAME\n')
    if(_a > 2):
        f.write('-sol  sol/a{}_{}\n'.format(_a-1, hst_name[_msize]) )
    f.write('-sol_out  sol/a{}_{}\n'.format(_a, hst_name[_msize]) )
    # f.write('-ita_history_name  hst/a4_' + commname + '.hst\n')
    write_hst(f,'hst/a{}_{}.hst'.format(_a, commname) )
    
    f.write('-unstructured_mesh_2d_flat_plate_distance \n')

    f.write('\n# --------------------------- ACCURACY\n')
    f.write('-a {}\n'.format(_a))

    f.write('\n# --------------------------- PHYSICS\n')
    f.write('-mesh_type c\n')
    f.write('-recon_condition\n')
    f.write('-physics RoeTurbSA2D\n')
    f.write('-d 2\n')
    f.write('-reynolds 5e6\n')
    f.write('-mach 0.2\n')
    f.write('-angle 0\n')

    f.write('\n# --------------------------- SOLVER OPTIONS\n')
    f.write('-exnut 0\n')
    f.write('-C 0.1\n')
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
        f.write('-ksp_pc_side right\n')
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

if __name__ == '__main__':

    
    # mode = ['ho-ilu-left', 'ho-ilu-right',
    #         'lo-ilu-left', 'lo-ilu-right',
    #         'gmres-lo-ilu',
    #         'lo-lu-mumps-left', 'lo-lu-mumps-right',
    #         'lo-lu-petsc-left', 'lo-lu-petsc-right']

    mode = ['lo-lu-petsc-right']

    # reordertype = ['rcm', 'qmd', 'lines']

    reordertype = ['rcm']

    ksp_inner_it = ['', '10', '10', '40']
    mesh_name = ['',
                 'MESH/flatplate_new_61x35',
                 'MESH/flatplate_new_121x69',
                 'MESH/flatplate_new_241x137',
                 '']
    hst_name = ['', 'coarse', 'medium', 'fine', 'superfine']

    mkdir('options')
    mkdir('hst')
    mkdir('sol')

    for a in [2,3,4]:
        for _msize in [1, 2, 3]:
            for _mode in mode:
                for _reordertype in reordertype:
                    _write_opt_file(a, _reordertype, _msize, _mode)
