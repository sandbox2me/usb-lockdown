#!/usr/bin/python
import sys
import glob
import time
import getpass

if getpass.getuser() != "root":
	print "you need to be root to run this program!\n"
	exit(0)

usb_ports_path = "/sys/bus/usb/devices/usb"

def lock(choice,count,ports):
	for x in range(1,count):
		try:
			if choice == 1:
				print "Usb Port " + str(x) + " Unlocked"
			else:
				print "Usb Port " + str(x) + " Locked"

			with open(ports + str(x) + "/authorized_default","w") as handle:
				handle.write(str(choice))
		except:
			print "something is wrong"

if sys.argv[1] == "u": #unlock usb ports
	state = 1
elif sys.argv[1] == "l": #lock usb ports
	state = 0
else:
	print "You Typed something wrong ... !\n"
	print "Example... python usblock.py l\n"
	print "Usage: python usblock.py [option]\n"
	print "options: l for lock and u for unlock\n"
	exit(0)

num_of_ports = 1
data = glob.glob("/sys/bus/usb/devices/*")
for x in data:
	if "usb" in x.replace('/sys/bus/usb/devices/',''):
		num_of_ports += 1

lock(state,num_of_ports,usb_ports_path)

if state == 1:
	print "Ports are unlocked, you have 10 seconds to attach a new device\n"
	time.sleep(10)
	state = 0
	print "Ports are now being locked down again\n"
	lock(state,num_of_ports,usb_ports_path)
	print "Ports locked Down\n"
