set terminal postscript eps color
set out outfile
unset key
unset colorbox
set xlabel "Trace #"
set ylabel "# of newly added trace"
set xtics 1 rotate by -90
set xrange [-0.5:upper-0.5]
set yrange [-0.5:upper-0.5]
plot matfile matrix with image
