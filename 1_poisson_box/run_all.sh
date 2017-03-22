#!/bin/bash 

# set -x 
## INPUT
## $1 -> order of accuracy
## $2 -> element type tet, wedge, pyramid, hex

## SET THE LOCATION FOR THE SOLVER
EXEC=~/code/ANSLib/hooshi/apps/solver/Solver
EXEC="mpirun -np 2 ${EXEC}"

# SET THE OPTIONS AND THE PROBLEM DATA
OPT='-pseudolts_fixed -C 1e20 -ita_cfl_max 1e20 -physics Poisson -d 3 -JC 1 -bJC 1 -mesh_type c -ksp_type fgmres -ksp_rtol 1e-15 -ksp_atol 1e-10 -ita_target_residual 1e-8 -pre_order 1 -pc_type ansksp -ansksp_ksp_type gmres -ansksp_ksp_its 5 -ansksp_pc_type sor -ansksp_pc_sor_its 5'
PD='-poisson_problem_data sinhsin'

## READ THE ORDER OF ACCURACY FROM THE INPUT
ACCU="$1"
ELE="$2"
UNAME="pp_data/${ELE}_a${ACCU}"

ORDER="-a ${ACCU} -poisson_norm_file pp_data/${ELE}_a${ACCU}.dat -sol_out sol/tmp.sol -ita_history_name "
rm -f ${UNAME}.dat
rm -f ${UNAME}.out

#echo "$EXEC $OPT $PD $ORDER"

echo $EXEC $OPT $PD $ORDER -f MESH/${ELE}_5 -ita_history_name ${UNAME}_5.hst
$EXEC $OPT $PD $ORDER -f MESH/${ELE}_5  -ita_history_name ${UNAME}_5.hst >> ${UNAME}.out

echo $EXEC $OPT $PD $ORDER -f MESH/${ELE}_10 -ita_history_name ${UNAME}_10.hst
$EXEC $OPT $PD $ORDER -f MESH/${ELE}_10 -ita_history_name ${UNAME}_10.hst >> ${UNAME}.out

echo $EXEC $OPT $PD $ORDER -f MESH/${ELE}_20 -ita_history_name ${UNAME}_20.hst
$EXEC $OPT $PD $ORDER -f MESH/${ELE}_20 -ita_history_name ${UNAME}_20.hst >> ${UNAME}.out

# echo $EXEC $OPT $PD $ORDER -f MESH/${ELE}_40 -ita_history_name ${UNAME}_40.hst
# $EXEC $OPT $PD $ORDER -f MESH/${ELE}_40 -ita_history_name ${UNAME}_40.hst >> ${UNAME}.out

# echo $EXEC $OPT $PD $ORDER -f MESH/${ELE}_80 -ita_history_name ${UNAME}_80.hst
# $EXEC $OPT $PD $ORDER -f MESH/${ELE}_80 -ita_history_name ${UNAME}_80.hst >> ${UNAME}.out
