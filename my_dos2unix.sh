#!/bin/bash

inputfile="$1"
outputfile="$2"

if [ x"$inputfile" != x -a x"$outputfile" != x ]; then
tr -d '\r' < "$inputfile" > "$outputfile"
else
echo
echo "./my_dos2unix.sh <inputfile> <outputfile>"
echo
exit
fi
