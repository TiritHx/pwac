def Byte_Conv(x): # only for ints ;C
    check1 = True
    byte_size = 1
    while check1:
        try:
            x = x.to_bytes(byte_size, byteorder='big')
            check1 = False
        except OverflowError:
            byte_size += 1
    return x