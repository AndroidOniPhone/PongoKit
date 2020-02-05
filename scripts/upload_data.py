import sys
data = open(sys.argv[1], "rb").read()
import usb.core
dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
if dev is None:
    raise ValueError('Device not found')
dev.set_configuration()

dev.ctrl_transfer(0x21, 2, 0, 0, 0)
dev.ctrl_transfer(0x21, 1, 0, 0, 0)
dev.write(2,data,100000)
if len(data) % 512 == 0:
	dev.write(2,"")
