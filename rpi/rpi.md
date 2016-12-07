* Downloaded Raspian Jessie Lite (circa Feb 2016)

### Burn

* ```lsblk```
* ```sudo apt-get install pv```
* ```sudo dd bs=4M if=/dev/zero | pv -r | dd bs=4M of=/dev/mmcblk0```
* ```sudo dd bs=4M if=/path/to/image | pv -r | dd bs=4M of=/dev/mmcblk0```

### First Boot

* Default user pi, password raspberry
* login

### Setup wifi

Edit - sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

network={
  ssid="..."
  proto=RSN
  key_mgmt=WPA_PKA
  pairwise=CCMP TKIP
  group=CCMP TKIP
  psk="..."
}

### Restart network

    sudo ifup wlan0
    ping www.google.co.uk
    ifconfig wlan0 | grep inet

### Update packages

    sudo apt-get update

### SSH

    sudo apt-get install ssh
    sudo /etc/init.d/ssh start
    sudo update-rc.d ssh defaults
    sudo reboot now

### Packages

    sudo apt-get install lynx
    
    cd /tmp
    wget https://bootstrap.pypa.io/get-pip.py
    sudo -H python /tmp/get-pip.py
    
    sudo -H python -m pip install BeautifulSoup

    sudo apt-get install festival festvox-rablpc16k

### Read keycodes

```
#!/bin/python
import struct
import sys

EV_KEY=1
EV_SYN=0
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

f = open("/dev/input/event0", "rb")

while True:
  key = f.read(EVENT_SIZE)
  sec, usec, type, code, value = struct.unpack(FORMAT, key)
  if type==EV_KEY and value==1:
    print("DN: type,code,value = %u %u %u" % (type, code, value))
  if type==EV_KEY and value==0:
    print("UP: type,code,value = %u %u %u" % (type, code, value))

f.close()
```
