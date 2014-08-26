#!/bin/bash

sudo mount /dev/sda4 /media/MyDrive
if [ $? -eq 0 ] ; then
nautilus /media/MyDrive/meine\ daten
else
sudo mount /dev/sda4 /media/MyDrive
nautilus /media/MyDrive/meine\ daten
fi
