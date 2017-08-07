EXEC=~/code/ANSLib/hooshi/apps/solver/Solver

# ${EXEC}   options/a3_coarse.opt
# ${EXEC}   options/a3_medium.opt
# ${EXEC}   options/a3_fine.opt

# ---------------

# ${EXEC}   options/a4_medium_full_qmd.opt | tee hst/a4_medium_full_qmd.out
# ${EXEC}   options/a4_medium_full_rcm.opt
# ${EXEC}   options/a4_medium_full_lines.opt

# ${EXEC}   options/a4_medium_fullr_qmd.opt  
# ${EXEC}   options/a4_medium_fullr_rcm.opt
# ${EXEC}   options/a4_medium_fullr_lines.opt

# ${EXEC}   options/a4_medium_onlyone_lines.opt | tee hst/a4_medium_onlyone_lines.out
# ${EXEC}   options/a4_medium_onlyone_rcm.opt | tee hst/a4_medium_onlyone_rcm.out
# ${EXEC}   options/a4_medium_onlyone_qmd.opt


# ${EXEC}   options/a4_medium_ksp_lines.opt | tee hst/a4_medium_ksp_lines.out
# ${EXEC}   options/a4_medium_ksp_rcm.opt | tee hst/a4_medium_ksp_rcm.out
# ${EXEC}   options/a4_medium_ksp_qmd.opt

# ${EXEC}   options/a4_medium_ansksp_lines.opt
# ${EXEC}   options/a4_medium_ansksp_rcm.opt
# ${EXEC}   options/a4_medium_ansksp_qmd.opt

# ${EXEC}   options/a4_medium_exact_lines.opt
# ${EXEC}   options/a4_medium_exact_rcm.opt
# ${EXEC}   options/a4_medium_exact_qmd.opt

# ---------------

# ${EXEC}   options/a4_fine_full_qmd.opt
# ${EXEC}   options/a4_fine_full_rcm.opt
# ${EXEC}   options/a4_fine_full_lines.opt

# ${EXEC}   options/a4_fine_fullr_qmd.opt
# ${EXEC}   options/a4_fine_fullr_rcm.opt
# ${EXEC}   options/a4_fine_fullr_lines.opt

# ${EXEC}   options/a4_fine_onlyone_lines.opt | tee hst/a4_fine_onlyone_lines.out
# ${EXEC}   options/a4_fine_onlyone_rcm.opt | tee hst/a4_fine_onlyone_rcm.out
# ${EXEC}   options/a4_fine_onlyone_qmd.opt


# ${EXEC}   options/a4_fine_ksp_lines.opt
# while :
# do
#     clear
#     ps faux | grep Solver >> hst/a4_fine_ksp_lines.mem
#     sleep 500s
# done

# ${EXEC}   options/a4_fine_ksp_rcm.opt
# ${EXEC}   options/a4_fine_ksp_qmd.opt

# ${EXEC}   options/a4_fine_ansksp_lines.opt
# ${EXEC}   options/a4_fine_ansksp_rcm.opt
# ${EXEC}   options/a4_fine_ansksp_qmd.opt

# ${EXEC}   options/a4_fine_exact_lines.opt
# ${EXEC}   options/a4_fine_exact_rcm.opt
# ${EXEC}   options/a4_fine_exact_qmd.opt

# ${EXEC}   options/a3_sfine.opt | tee hst/a3_sfine.out
# ${EXEC}   options/a4_sfine_ksp_lines.opt | tee hst/a4_sfine_ksp_lines.out


# nohup ~/code/ANSLib/hooshi/apps/solver/Solver options/a4_fine_full_qmd.opt >> qmd_output.txt  2>&1 &

# while :; do     clear;     ps faux | grep Solver >> hst/a4_fine_full_qmd.mem;     sleep 500s; done
