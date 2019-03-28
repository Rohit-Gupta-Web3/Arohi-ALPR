
#./setup.sh


{
echo '#!/usr/bin/env xdg-open'
echo '[Desktop Entry]'
echo 'Version=1.0'
echo 'Icon[en_IN]=gnome-panel-launcher'
echo 'Name[en_IN]=Aarohi Impex'
echo 'Type=Application'
echo 'Terminal=true'
echo 'Exec=exec.sh'
echo 'Name=Aarohi Impex'
echo 'Icon=gnome-panel-launcher'
echo 'StartupNotify=true'
} > Aarohi-Impex.desktop

{
echo '#!/usr/bin/env xdg-open'
echo '[Desktop Entry]'
echo 'Version=1.0'
echo 'Icon[en_IN]=gnome-panel-launcher'
echo 'Name[en_IN]=Aarohi Impex Database'
echo 'Type=Application'
echo 'Terminal=true'
echo 'Exec= sqlitebrowser Aarohi.db'
echo 'Name=Aarohi Impex Databanel-ase'
echo 'Icon=gnome-panel-launcher'
echo 'StartupNotify=true'
} > Aarohi-Database.desktop


#`grep '^Exec' Aarohi-database.desktop | tail -1 | sed 's/^Exec=//' | sed 's/%.//' | sed 's/^"//g' | sed 's/" *$//g'` &
