set terminal postscript eps color
set out "oflow_narrow.eps"
set xlabel "Average speed"
set ylabel "Number of trackable points"
set grid
set xrange [0.3:0.82]
set xtics 0.1
set yrange [1:8]
plot "oflow_narrow.dat" w lp lw 3 pt 3 ps 2 notitle
