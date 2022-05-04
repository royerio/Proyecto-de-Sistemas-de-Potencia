reset
set terminal windows
set style data lines
set xtics
set border
set xlabel 't (s)'
set grid
set key opaque
plot \
'Preactivas_Gens.cur' using 1 :  2 title 'sync mach G1                  : reactive power produced (Mvar)',\
'Preactivas_Gens.cur' using 1 :  3 title 'sync mach G2                  : reactive power produced (Mvar)',\
'Preactivas_Gens.cur' using 1 :  4 title 'sync mach G3                  : reactive power produced (Mvar)',\
'Preactivas_Gens.cur' using 1 :  5 title 'sync mach G4                  : reactive power produced (Mvar)'
