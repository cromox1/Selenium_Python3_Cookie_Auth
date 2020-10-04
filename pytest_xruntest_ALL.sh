#!/bin/bash

torun="$1"
onbrowser="$2"
if [ x"$onbrowser" == x ]; then
# onbrowser='firefox'
onbrowser='chrome'
# onbrowser='brave'
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

if [ x"$torun" == xp01 ]||[ x"$torun" == xmengkome ]; then

file1=console_${masani}_p01mainmengkometest.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > 'logs'/"$file1"
echo -n "$ py.test.exe -v -s tests/p01mengkome/p01mengkomeloginout1_test1.py --browser " >> 'logs/'"$file1"
echo -n "$onbrowser" >> 'logs/'"$file1"
echo -n " > consoleoutput1.txt 2>&1" >> 'logs/'"$file1"
echo >> 'logs'/"$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> 'logs'/"$file1"
echo "$ cat consoleoutput1.txt" >> 'logs'/"$file1"
echo >> 'logs'/"$file1"

py.test.exe -v -s tests/p01mengkome/p01mengkomeloginout1_test1.py --browser "$onbrowser" | tee -a 'logs'/"$file1"

elif [ x"$torun" == xp01test1 ]||[ x"$torun" == xtest1 ]; then

file1=console_${masani}_p01test1mengkome.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > 'logs'/"$file1"
echo -n "$ py.test.exe -v -s tests/p01mengkome/p01mengkomeloginout1_test1.py::P02MengkomeLoginLogoutTests::test1_login_mengkome_add_cookie_page --browser " >> 'logs'/"$file1"
echo -n "$onbrowser" >> 'logs/'"$file1"
echo -n " > consoleoutput1.txt 2>&1" >> 'logs/'"$file1"
echo >> 'logs'/"$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> 'logs'/"$file1"
echo "$ cat consoleoutput1.txt" >> 'logs'/"$file1"
echo >> 'logs'/"$file1"

py.test.exe -v -s tests/p01mengkome/p01mengkomeloginout1_test1.py::P02MengkomeLoginLogoutTests::test1_login_mengkome_add_cookie_page --browser "$onbrowser" | tee -a 'logs'/"$file1"

elif [ x"$torun" == xp02 ]||[ x"$torun" == xpixitmedia ]; then

file1=console_${masani}_p02mainpixitmediatest.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > 'logs'/"$file1"
echo -n "$ py.test.exe -v -s tests/p02pixitmedia/p02pixitmediahoover1_test1.py --browser " >> 'logs/'"$file1"
echo -n "$onbrowser" >> 'logs/'"$file1"
echo -n " > consoleoutput1.txt 2>&1" >> 'logs/'"$file1"
echo >> 'logs'/"$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> 'logs'/"$file1"
echo "$ cat consoleoutput1.txt" >> 'logs'/"$file1"
echo >> 'logs'/"$file1"

py.test.exe -v -s tests/p02pixitmedia/p02pixitmediahoover1_test1.py --browser "$onbrowser" | tee -a 'logs'/"$file1"

elif [ x"$torun" == xp02test1 ]||[ x"$torun" == xtest2 ]; then

file1=console_${masani}_p01test1mengkome.txt
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" > 'logs'/"$file1"
echo -n "$ py.test.exe -v -s tests/p02pixitmedia/p02pixitmediahoover1_test1.py::P02MengkomeLoginLogoutTests::test1_login_mengkome_add_cookie_page --browser " >> 'logs'/"$file1"
echo -n "$onbrowser" >> 'logs/'"$file1"
echo -n " > consoleoutput1.txt 2>&1" >> 'logs/'"$file1"
echo >> 'logs'/"$file1"
echo "penggunabiasa@PC-rosli MINGW64 ~/python3_projects/Selenium/MengKome" >> 'logs'/"$file1"
echo "$ cat consoleoutput1.txt" >> 'logs'/"$file1"
echo >> 'logs'/"$file1"

py.test.exe -v -s tests/p02pixitmedia/p02pixitmediahoover1_test1.py::P02MengkomeLoginLogoutTests::test1_login_mengkome_add_cookie_page --browser "$onbrowser" | tee -a 'logs'/"$file1"

else

echo
# echo "./pytest_xruntest_p01mengkome1.sh test_suite  [ testsuite / test_suite / suite ] [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p01mengkome1.sh p01         [ p01 / mengkome ]                 [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p01mengkome1.sh p01test1    [ p01test1 / test1 ]               [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p01mengkome1.sh p02         [ p02 / pixitmedia ]               [ ie / chrome / firefox / opera ] "
echo "./pytest_xruntest_p01mengkome1.sh p02test1    [ p02test1 / test2 ]               [ ie / chrome / firefox / opera ] "

echo

fi
