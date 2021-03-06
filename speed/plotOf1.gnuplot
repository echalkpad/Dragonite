set terminal postscript eps color
set out "oflow1.eps"
set xlabel "Average speed"
set ylabel "Number of trackable points"
set grid
set xrange [0.5:1.8]
set xtics 0.1
set yrange [5:21]
plot "oflow1.dat" w lp lw 3 pt 3 ps 2 notitle
