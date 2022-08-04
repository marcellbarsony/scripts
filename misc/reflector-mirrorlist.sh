#!/bin/bash

echo "Backing up mirrorlist..."
sudo cp -f /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
exitcode1=$?

echo "Reflector: generating mirrorlist..."
sudo reflector --latest 20 --protocol https --connection-timeout 5 --sort rate --save /etc/pacman.d/mirrorlist
exitcode2=$?

if [ ${exitcode1} != "0" ] || [ ${exitcode2} != "0" ]; then
    echo "Cannot update Pacman mirrorlist.\n
    Backup: ${exitcode1}\n
    Reflector: ${exitcode2}"
fi
