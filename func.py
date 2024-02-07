import os

def Byte_Conversion(x): # only for ints ;C
    check1 = True
    byte_size = 1
    while check1:
        try:
            x = x.to_bytes(byte_size, byteorder='big')
            check1 = False
        except OverflowError:
            byte_size += 1
    return x

def Progress_Bar(progress, total):
    percent = 100 * (progress / total)
    bar = chr(9608) * percent + chr(9617) * (100 - percent)
    print(f"|{bar} {percent:.2f}%|", end="\r")

def Image_To_Dict(w, h, pix): # converts image to dictionary of colored pixels
    data = {}
    pos = 0
    for i in range(w):
        for y in range(h):
            if '#%02x%02x%02x' % pix[i, y] not in data:
                data['#%02x%02x%02x' % pix[i, y]] = []
            data['#%02x%02x%02x' % pix[i, y]].append(pos)
            pos += 1
    print("\nPixel data added to dictionary")
    return data

def File_Exist(file_name):
    if not os.path.isfile(file_name): # create output file if it doesnt exist que????????????????
        file = open(file_name, "x")
        file.close()
        print("Output file '" + file_name + "' created")
        return False
    print("Output file detected")
    return True # returns true or false, it depends if file existed or not, maybe usefull later, just maybe, idk but I will leave it here 

def Encode_Chars(string):
    return string.encode('utf-8')

def Write_Image_Info(file_name, w, h, data):
    file = open(file_name, "wb")
    file.write(Encode_Chars(str(w) + 'x' + str(h) + '\n'))
    file.write(Encode_Chars(str(data).replace(" ", "")))
    file.close()
    print("Info added succesfully")