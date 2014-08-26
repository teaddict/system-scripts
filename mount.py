import os,sys
import subprocess

if os.path.ismount("/media/MyDrive"):
	subprocess.Popen(["nautilus", "/media/MyDrive"])
else:
	path = "/media/MyDrive"
	if not os.path.exists(path):
		os.mkdir(path);
	else:
		subprocess.Popen(["mount","-t","fuseblk","/dev/sda4","/media/MyDrive"])
		subprocess.Popen(["nautilus", "/media/MyDrive"])
	
