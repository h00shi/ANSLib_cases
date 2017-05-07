#!/usr/bin/python

import os

pset = [1, 2, 3, 4]
hset = [1, 2, 3, 4]

if not os.path.exists('pp_data'):
    os.makedirs('pp_data')
if not os.path.exists('options'):
    os.makedirs('options')
if not os.path.exists('sol'):
    os.makedirs('sol')

# ----------------------------------------------------------------
# Curved
# ----------------------------------------------------------------

for p in pset:
    for h in hset:
        comname = 'h' + `h` + '_p' + `p`
        file_name = 'options/' + comname + '_curve.opt'
        f = open(file_name, 'w')

        f.write('#---------------------------------- PHYSICS\n')
        f.write('-physics Euler3D\n')
        f.write('-d 3\n')
        f.write('-mesh_type c\n')
        f.write('-mach 0.38\n')
        f.write('-angle 0\n')

        f.write('\n# --------------------------------- SOLVER OPTIONS\n')
        f.write('-ksp_type fgmres\n')
        f.write('-ksp_norm_type unpreconditioned\n')
        f.write('-ksp_rtol 1e-3\n')
        f.write('-ksp_gmres_preallocate\n')
        f.write('-ksp_gmres_restart 100\n')
        f.write('-ksp_max_it 500\n')
        f.write('-pre_order 1\n')

        # f.write('-pc_type ansksp\n')
        # f.write('-ansksp_ksp_norm_type preconditioned\n')
        # f.write('-ansksp_ksp_max_it 5\n')
        # f.write('-ansksp_pc_type sor\n')
        # f.write('-ansksp_pc_sor_its 5\n')

        f.write('-pc_type sor\n')
        f.write('-pc_sor_its 4\n')
        f.write('-pc_sor_lits 4\n')

        f.write('-recon_condition\n')
        f.write('-C 10\n')
        f.write('-jacobian_type recanalytic\n')
        f.write('-pseudolts_fixed\n')
        f.write('-max_iter 25\n')

        f.write('\n# --------------------------------- FILE NAMES\n')
        f.write('-f MESH/sphere_m' + `h` + '\n')
        # if (p > 1):
        #     comname2 = 'h' + `h` + '_p' + `p - 1`
        #     f.write('-sol sol/' + comname2 + '_curve\n')
        f.write('-sol_out sol/' + comname + '_curve\n')
        f.write('-ita_history_name pp_data/' + comname + '_curve.hst\n')

        f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
        f.write('-a ' + `p` + '\n')
        f.write('-ita_target_residual 1e-10\n')
        f.write('-mcell3d_sphere_hack 1\n')
        f.write('-mcell3d_extraq_face 1\n')
        f.write('-mcell3d_extraq_cell 1\n')

        f.close()
