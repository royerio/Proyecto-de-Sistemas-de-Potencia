reset
set terminal windows
set style data lines
set xtics
set border
set xlabel 't (s)'
set grid
set key opaque
plot \
'Pactivas_gens.cur' using 1 :  2 title 'sync mach G1                  : active power produced (MW)',\
'Pactivas_gens.cur' using 1 :  3 title 'sync mach G2                  : active power produced (MW)',\
'Pactivas_gens.cur' using 1 :  4 title 'sync mach G3                  : active power produced (MW)',\
'Pactivas_gens.cur' using 1 :  5 title 'sync mach G4                  : active power produced (MW)'
