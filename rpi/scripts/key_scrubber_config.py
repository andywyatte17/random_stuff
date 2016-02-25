#!/bin/python

'''
Configuration data for key_scrubber.py
'''

from collections import namedtuple

bus = namedtuple("bus", "bus_stop_code")
mpc = namedtuple("mpc", "command")
system = namedtuple("system", "command_name")

NUM_KEY_CODES={41:"1",3:"2",4:"3",5:"4",6:"5",7:"6",8:"7",9:"8",10:"9",11:"0"}
ENTER_KEY=28
KBD_DEV="platform-i8042-serio-0-event-kbd"

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

