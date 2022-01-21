import fcntl
import struct
import termios


def calc_tam():
            th, tw, hp, =struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH',0,0,0,0)))

print(calc_tam())