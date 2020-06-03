#!/bin/bash

torun="$1"

onbrowser="$2"
if [ x"$onbrowser" == x ]; then
# onbrowser='firefox'
onbrowser='chrome'
fi

date1=`date +%Y%m%d_%H`
minit=`date +%M`
minit2=$(((10#$minit / 5 ) * 5))
if [ $minit2 -lt 10 ]; then
   minit1=0${minit2}
else
   minit1=${minit2}
fi
masani=${date1}${minit1}00

if [ x"$torun" == xp02 ]||[ x"$torun" == xmengkome ]; then

file1=console_${masani}_p02mainmengkometest.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > "$file1"
echo "$ py.test.exe -v -s tests/p02mengkome/p02mengkomeloginout1_test1.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/p02mengkome/p02mengkomeloginout1_test1.py | tee -a "$file1"

elif [ x"$torun" == xp01test1 ]||[ x"$torun" == xtest1 ]; then

file1=console_${masani}_p02test1mengkome.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > "$file1"
echo "$ py.test.exe -v -s tests/p02mengkome/p02mengkomeloginout1_test1.py::P02MengkomeLoginLogoutTests::test1_login_mengkome_add_cookie_page > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/p02mengkome/p02mengkomeloginout1_test1.py::P02MengkomeLoginLogoutTests::test1_login_mengkome_add_cookie_page | tee -a "$file1"

else

echo
# echo "./pytest_xruntest_p02mengkome1.sh test_suite  [ testsuite / test_suite / suite ] [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p02mengkome1.sh p02         [ p02 / mengkome ]                 [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p02mengkome1.sh p02test1    [ p02test1 / test1 ]               [ ie / chrome / firefox / opera ] "
echo

fi
