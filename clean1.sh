#!/bin/bash

scrn1=`ls -p | grep -i '/' | grep -i screenshots2 | tail -1 | sed -e 's/\///g'`
if [ x"$scrn1" == x ]; then
   mkdir screenshots2
fi

cscrn1=`ls screenshots/*.png | wc -l`
if [ $cscrn1 -gt 0 ]; then
   mv screenshots/*.png screenshots2
fi

cgeck1=`ls geckodriver.log | wc -l`
if [ $cgeck1 -gt 0 ]; then
   rm geckodriver.log
fi

log1=`ls -p | grep -i '/' | grep -i logs2 | tail -1 | sed -e 's/\///g'`
if [ x"$log1" == x ]; then
   mkdir logs2
fi

cauto1=`ls automation_*.log | wc -l`
if [ $cauto1 -gt 0 ]; then
   mv automation_*.log logs2
fi

ccons1=`ls console_*.txt | wc -l`
if [ $ccons1 -gt 0 ]; then
   mv console_*.txt logs2
fi
