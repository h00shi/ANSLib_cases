#!/usr/bin/python

pset = [1, 2, 3, 4]
hset = [1, 2, 3]

for p in pset:
    for h in hset:
        comname = 'h' + `h` + '_p' + `p`
        file_name = 'options/sphere_' + comname + '.opt'
        f = open(file_name, 'w')

        f.write('#---------------------------------- PHYSICS\n')
        f.write('-physics Euler3D\n')
        f.write('-d 3\n')
        f.write('-mesh_type c\n')
        f.write('-mach 0.38\n')
        f.write('-angle 0\n')

        f.write('\n# --------------------------------- SOLVER OPTIONS\n')
        f.write('-ksp_type fgmres\n')
        f.write('-ksp_gmres_preallocate\n')
        f.write('-ksp_gmres_restart 100\n')
        f.write('-ksp_max_it 500\n')
        f.write('-pre_order 1\n')
        f.write('-pc_type ansksp\n')
        f.write('-ansksp_ksp_norm_type unpreconditioned\n')
        f.write('-ansksp_ksp_max_it 5\n')
        f.write('-ansksp_pc_type sor\n')
        f.write('-ansksp_pc_sor_its 5\n')
        f.write('-recon_condition\n')
        f.write('-C 10\n')
        f.write('-jacobian_type recanalytic\n')
        f.write('-pseudolts_fixed\n')
        f.write('-max_iter 20\n')

        f.write('\n# --------------------------------- FILE NAMES\n')
        f.write('-f MESH/sphere_m' + `h` + '\n')
        if (p > 1):
            comname2 = 'h' + `h` + '_p' + `p - 1`
            f.write('-sol_out sol/sphere_' + comname2 + '\n')
        f.write('-sol_out sol/sphere_' + comname + '\n')
        f.write('-ita_history_name hst/' + comname + '.hst\n')

        f.write('\n# --------------------------------- ACCURACY AND STENCIL\n')
        f.write('-a ' + `p` + '\n')
        f.write('-ita_target_residual 1e-7\n')
        f.write('-mcell3d_stencil_size 0,0,6,15,30\n')

        f.close()
