#!/usr/bin/python

import os


# ----------------------------------------------------------------
# Functions
# ----------------------------------------------------------------


def write_file(exectype, fname, nodes, ppn, walltime, mem, command):
    "Write the header of a pbs file"

    ff = open(fname, "w")

    ff.write('#!/bin/bash\n')
    ff.write('#PBS -S /bin/bash\n')
    ff.write('#PBS -l nodes=' + nodes + ':ppn=' + ppn + '\n')
    ff.write('#PBS -l walltime=' + walltime + '\n')
    ff.write('#PBS -l mem=' + mem + '\n')
    ff.write('#PBS -M s.hoshyari@gmail.com\n')
    ff.write('#PBS -m abe\n\n')

    ff.write('. ~/scripts/setenv.sh \n\n')

    ff.write('cd $PBS_O_WORKDIR\n')
    ff.write('echo \"Current working directory is `pwd`\"\n\n')

    ff.write('echo \"Node file: $PBS_NODEFILE :\"\n')
    ff.write('echo \"---------------------\"\n')
    ff.write('cat $PBS_NODEFILE\n')
    ff.write('echo \"---------------------\"\n\n')

    ff.write('# On many WestGrid systems a variable PBS_NP is automatically\n')
    ff.write('# assigned the number of cores requested of the batch system\n')
    ff.write('# and one could use\n')
    ff.write('# echo "Running on $PBS_NP cores."\n')
    ff.write('# On systems where $PBS_NP is not available, one could use:\n\n')

    ff.write('CORES=`/bin/awk \'END {print NR}\' $PBS_NODEFILE`\n')
    ff.write('echo \"Running on $CORES cores.\"\n\n')

    ff.write('echo \"Starting run at: `date`\"\n\n')

    ff.write('# On most WestGrid systems, mpiexec will automatically start\n')
    ff.write('# a number of MPI processes equal to the number of cores\n')
    ff.write('# requested. The -n arugment can be used to explicitly\n')
    ff.write('# use a specific number of cores.\n\n')

    ff.write('NPMAX=${CORES}\n')
    ff.write('MPI_BINDING=\'--bysocket --bind-to-socket --report-bindings\'\n')
    ff.write('MPIEXEC=mpiexec\n')
    ff.write('\n\n')

    if (exectype == 0):
        ff.write('${MPIEXEC} ${MPI_BINDING} -np ${CORES} ~/code/ANSLib/hooshi/apps/solver/Solver ' + command + '\n\n')
    else:
        ff.write('${MPIEXEC} ${MPI_BINDING} -np ${CORES} ~/code/ANSLib/hooshi/shayans_playground/turbsa3d_post_processor ' + command + '\n\n')

    ff.write('echo \"' + fname + ' finished at: `date`\"\n')

    ff.close()

# ----------------------------------------------------------------
# Create folders
# ----------------------------------------------------------------

if not os.path.exists('pbs'):
    os.makedirs('pbs')
if not os.path.exists('pbs/parallel'):
    os.makedirs('pbs/parallel')
if not os.path.exists('vtu'):
    os.makedirs('vtu')
if not os.path.exists('sol'):
    os.makedirs('sol')

# ----------------------------------------------------------------
# Do the curves for h1
# ----------------------------------------------------------------
write_file(0,'pbs/h1_p1_facet.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p1_facet.opt |& tee pp_data/h1_p1_facet.out')
write_file(0,'pbs/h1_p2_facet.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p2_facet.opt |& tee pp_data/h1_p2_facet.out')
write_file(0,'pbs/h1_p3_facet.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p3_facet.opt |& tee pp_data/h1_p3_facet.out')
write_file(0,'pbs/h1_p4_facet.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p4_facet.opt |& tee pp_data/h1_p4_facet.out')

write_file(0,'pbs/h2_p1_facet.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p1_facet.opt |& tee pp_data/h2_p1_facet.out')
write_file(0,'pbs/h2_p2_facet.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p2_facet.opt |& tee pp_data/h2_p2_facet.out')
write_file(0,'pbs/h2_p3_facet.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p3_facet.opt |& tee pp_data/h2_p3_facet.out')
write_file(0,'pbs/h2_p4_facet.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p4_facet.opt |& tee pp_data/h2_p4_facet.out')

write_file(0,'pbs/h3_p1_facet.pbs', '8', '1', '02:00:00', '40gb',
           ' -opt options/h3_p1_facet.opt |& tee pp_data/h3_p1_facet.out')
write_file(0,'pbs/h3_p2_facet.pbs', '8', '1', '03:00:00', '40gb',
           ' -opt options/h3_p2_facet.opt |& tee pp_data/h3_p2_facet.out')
write_file(0,'pbs/h3_p3_facet.pbs', '8', '1', '04:00:00', '40gb',
           ' -opt options/h3_p3_facet.opt |& tee pp_data/h3_p3_facet.out')
write_file(0,'pbs/h3_p4_facet.pbs', '8', '1', '05:00:00', '40gb',
           ' -opt options/h3_p4_facet.opt |& tee pp_data/h3_p4_facet.out')


write_file(0,'pbs/h4_p1_facet.pbs', '8', '1', '02:00:00', '96gb',
           ' -opt options/h4_p1_facet.opt |& tee pp_data/h4_p1_facet.out')
write_file(0,'pbs/h4_p2_facet.pbs', '8', '1', '10:00:00', '96gb',
           ' -opt options/h4_p2_facet.opt |& tee pp_data/h4_p2_facet.out')
write_file(0,'pbs/h4_p3_facet.pbs', '8', '1', '10:00:00', '96gb',
           ' -opt options/h4_p3_facet.opt |& tee pp_data/h4_p3_facet.out')
write_file(0,'pbs/h4_p4_facet.pbs', '8', '1', '10:00:00', '96gb',
           ' -opt options/h4_p4_facet.opt |& tee pp_data/h4_p4_facet.out')

# ----------------------------------------------------------------
# Do the curves for h1
# ----------------------------------------------------------------
write_file(0,'pbs/h1_p1_curve.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p1_curve.opt |& tee pp_data/h1_p1_curve.out')
write_file(0,'pbs/h1_p2_curve.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p2_curve.opt |& tee pp_data/h1_p2_curve.out')
write_file(0,'pbs/h1_p3_curve.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p3_curve.opt |& tee pp_data/h1_p3_curve.out')
write_file(0,'pbs/h1_p4_curve.pbs', '8', '1', '00:10:00', '10gb',
           ' -opt options/h1_p4_curve.opt |& tee pp_data/h1_p4_curve.out')

write_file(0,'pbs/h2_p1_curve.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p1_curve.opt |& tee pp_data/h2_p1_curve.out')
write_file(0,'pbs/h2_p2_curve.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p2_curve.opt |& tee pp_data/h2_p2_curve.out')
write_file(0,'pbs/h2_p3_curve.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p3_curve.opt |& tee pp_data/h2_p3_curve.out')
write_file(0,'pbs/h2_p4_curve.pbs', '8', '1', '00:40:00', '10gb',
           ' -opt options/h2_p4_curve.opt |& tee pp_data/h2_p4_curve.out')

write_file(0,'pbs/h3_p1_curve.pbs', '8', '1', '01:00:00', '40gb',
           ' -opt options/h3_p1_curve.opt |& tee pp_data/h3_p1_curve.out')
write_file(0,'pbs/h3_p2_curve.pbs', '8', '1', '01:00:00', '40gb',
           ' -opt options/h3_p2_curve.opt |& tee pp_data/h3_p2_curve.out')
write_file(0,'pbs/h3_p3_curve.pbs', '8', '1', '01:00:00', '40gb',
           ' -opt options/h3_p3_curve.opt |& tee pp_data/h3_p3_curve.out')
write_file(0,'pbs/h3_p4_curve.pbs', '8', '1', '01:00:00', '40gb',
           ' -opt options/h3_p4_curve.opt |& tee pp_data/h3_p4_curve.out')


write_file(0,'pbs/h4_p1_curve.pbs', '8', '1', '02:00:00', '96gb',
           ' -opt options/h4_p1_curve.opt |& tee pp_data/h4_p1_curve.out')
write_file(0,'pbs/h4_p2_curve.pbs', '8', '1', '08:00:00', '96gb',
           ' -opt options/h4_p2_curve.opt |& tee pp_data/h4_p2_curve.out')
write_file(0,'pbs/h4_p3_curve.pbs', '8', '1', '08:00:00', '96gb',
           ' -opt options/h4_p3_curve.opt |& tee pp_data/h4_p3_curve.out')
write_file(0,'pbs/h4_p4_curve.pbs', '8', '1', '08:00:00', '96gb',
           ' -opt options/h4_p4_curve.opt |& tee pp_data/h4_p4_curve.out')


# ----------------------------------------------------------------
# PostProcessing
# ----------------------------------------------------------------


for h in [2, 4]:
    for p in [2,3,4]:
        
        strcommand = ' -physics Euler3D -a ' + `p` + ' -f MESH/sphere_m' + `h` + ' -sol sol/h'+ `h`+'_p' + `p`+ '_curve -out vtu/h' +`h` + '_p'+`p`+'_curve -mcell3d_sphere_hack 1 -mcell3d_extraq_cell 1 -mcell3d_extraq_face 1'
        strcase = 'h' +`h` +'_' + 'p' + `p` + '_curve'

write_file(0,'pbs/'+strcase+'_postprocess.pbs', '8', '1', '00:10:00', '10gb', strcommand + ' |& tee pp_data/' + strcase+'_postprocess.out')
        
# ----------------------------------------------------------------
# Runtimes
# ----------------------------------------------------------------

tset = ['08:00:00', '8:00:00', '04:00:00', '04:00:00', '02:00:00', '02:00:00', '01:00:00', '01:00:00', '01:00:00', '01:00:00' ]
procset = [1,2,3,4,5,6,7,8,9,10]
pset = [2,3,4]

for p in pset:
    for proc in procset:
        cname = 'P'+ `proc` + '_h3_' + 'p' + `p` + '_curve'
        pbname = 'pbs/' + cname + '.pbs'
        cmand = '-opt options/h3_' + 'p' + `p` + '_curve.opt -ita_histoy_name pp_data/' + cname + '.hst |& tee pp_data/' + cname + '.out'

        write_file(0,pbname, `proc`, '1', tset[proc-1], '40gb', cmand)
        
