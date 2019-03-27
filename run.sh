
./setup.sh


{
echo '#!/usr/bin/env xdg-open'
echo '[Desktop Entry]'
echo 'Version=1.0'
echo 'Type=Application'
echo 'Terminal=false'
echo 'Exec=python3 login.cpython-36.pyc'
echo 'Name=Aarohi Impex'
echo 'Icon=.'
} > Aarohi.desktop


#`grep '^Exec' Aarohi.desktop | tail -1 | sed 's/^Exec=//' | sed 's/%.//' | sed 's/^"//g' | sed 's/" *$//g'` &
