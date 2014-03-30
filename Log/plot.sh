#!/bin/bash
./LogReader $1 traces_$1 match$1.log
gnuplot -e "matfile='$1_match.dat';upper=$1;outfile='$1.eps'" plotMat.gnuplot
