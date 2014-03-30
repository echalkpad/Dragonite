set terminal postscript eps color
set out "oflow_intersect.eps"
set xlabel "Average speed"
set ylabel "Number of trackable points"
set grid
set xrange [0.5:2.2]
set xtics 0.1
set yrange [0:7]
plot "oflow_intersect.dat" w lp lw 3 pt 3 ps 2 notitle
