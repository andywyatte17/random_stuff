#!/bin/python

'''
Configuration data for key_scrubber.py
'''

from collections import namedtuple

bus = namedtuple("bus", "bus_stop_code")
mpc = namedtuple("mpc", "command")
system = namedtuple("system", "command_name")

#ENTER_KEY=28
#NUM_KEY_CODES={41:"1",3:"2",4:"3",5:"4",6:"5",7:"6",8:"7",9:"8",10:"9",11:"0"}
#KBD_DEV="by-path/platform-i8042-serio-0-event-kbd"

ENTER_KEY=96
NUM_KEY_CODES={79:"1",80:"2",81:"3",75:"4",76:"5",77:"6",71:"7",72:"8",73:"9",82:"0"}
KBD_DEV="by-id/usb-13ba_0001-event-kbd"

FUNCTIONS={"111":bus(54761),
           "120":mpc(["stop"]),
           "121":mpc(["clear", "add http://209.126.66.166:9012/aac-64", "play"]),
           "191":mpc(["volume 10"]),
           "192":mpc(["volume 25"]),
           "193":mpc(["volume 50"]),
           "194":mpc(["volume 75"]),
           "195":mpc(["volume 100"]),
           "90":system("stop"),
           "98":system("reboot"),
           "99":system("shutdown")
}

