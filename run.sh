
./setup.sh


{
echo '#!/usr/bin/env xdg-open'
echo '[Desktop Entry]'
echo 'Version=1.0'
echo 'Icon[en_IN]=gnome-panel-launcher'
echo 'Name[en_IN]=Aarohi'
echo 'Type=Application'
echo 'Terminal=true'
echo 'Exec=python3 login.cpython-36.pyc'
echo 'Name=Aarohi Impex'
echo 'Icon=gnome-panel-launcher'
echo 'StartupNotify=true'
} > Aarohi.desktop


#`grep '^Exec' Aarohi.desktop | tail -1 | sed 's/^Exec=//' | sed 's/%.//' | sed 's/^"//g' | sed 's/" *$//g'` &
