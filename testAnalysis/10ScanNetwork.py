import socket
import os
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 1743))

s.sendto(b'\xc5\x74\x40\x03\x00\x10\xdb\x6b\x0c\x1a\x00\x00\x02\xc2\x00\x04\x88\xcc\x00\x00',("192.168.88.110",1740))
s.sendto(b'\xc5\x74\x40\x03\x00\x10\xdb\x6b\x0c\x1a\x00\x00\x02\xc2\x00\x04\x88\xcc\x00\x00',("192.168.88.110",1741))
s.sendto(b'\xc5\x74\x40\x03\x00\x10\xdb\x6b\x0c\x1a\x00\x00\x02\xc2\x00\x04\x88\xcc\x00\x00',("192.168.88.110",1742))
s.sendto(b'\xc5\x74\x40\x03\x00\x10\xdb\x6b\x0c\x1a\x00\x00\x02\xc2\x00\x04\x88\xcc\x00\x00',("192.168.88.110",1743))
