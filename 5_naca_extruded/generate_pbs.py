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
    #ff.write('MPI_BINDING=\'--bysocket --bind-to-socket --report-bindings\'\n')
    ff.write('MPI_BINDING=\n')
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
if not os.path.exists('vtu'):
    os.makedirs('vtu')
if not os.path.exists('sol'):
    os.makedirs('sol')

# ----------------------------------------------------------------
# BJACOBI PRECON
# ----------------------------------------------------------------
write_file(0,'pbs/D3_p2_lines.pbs', '8', '1', '06:00:00', '16gb',
           ' -opt options/D3_p2_lines.opt |& tee pp_data/D3_p2_lines.out')

write_file(0,'pbs/D3_p3_lines.pbs', '8', '1', '06:00:00', '16gb',
           ' -opt options/D3_p3_lines.opt |& tee pp_data/D3_p3_lines.out')
write_file(0,'pbs/D3_p3_nut.pbs', '8', '1', '06:00:00', '16gb',
           ' -opt options/D3_p3_nut.opt |& tee pp_data/D3_p3_nut.out')

write_file(0,'pbs/D3_p4_lines.pbs', '8', '1', '06:00:00', '16gb',
           ' -opt options/D3_p4_lines.opt |& tee pp_data/D3_p4_lines.out')
write_file(0,'pbs/D3_p4_nut.pbs', '8', '1', '06:00:00', '16gb',
           ' -opt options/D3_p4_nut.opt |& tee pp_data/D3_p4_nut.out')
