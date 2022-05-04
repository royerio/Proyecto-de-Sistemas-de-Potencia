reset
set terminal windows
set style data lines
set xtics
set border
set xlabel 't (s)'
set grid
set key opaque
plot \
'VelocidadRotorG1Inestable.cur' using 1 :  2 title 'sync mach G1                  : rotor speed (pu)'
