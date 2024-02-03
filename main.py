# projekt wymyślony pod prysznicem, tak jestem zajebisty
# program będzie iterował po każdym pikselu i dla każdego koloru jaki jest na zdjęciu będzie dawał numer tego piksela
# jeśli jakiś kolor będzie najwięcej razy używany będzie ustawiony na default dla pozostałych pikseli
# to samo będzie sie działo z kanałem alpha dla plików png
# photo with avant-garde compression - pwac, it sounds fancy -> picture with state_of_the_art compression, yes state of the art is one word here dont judge me
import os
from PIL import Image
from func import Byte_Conv
img = Image.open('serdek.png')
pix = img.load()
w ,h = img.size
data = {}
pos = 0
for i in range(w):
    for y in range(h):
        if '#%02x%02x%02x' % pix[i, y] not in data:
            data['#%02x%02x%02x' % pix[i, y]] = []
        data['#%02x%02x%02x' % pix[i, y]].append(pos)
        pos += 1
print("\nPixel data added to dictionary")

ofn = "data.pwsc" # output file name
if not os.path.isfile(ofn): # create output file if it doesnt exist
    file = open(ofn, "x")
    file.close()
    print("Output file '" + ofn + "' created")

file = open(ofn, "wb")
if w == h:
    file.write(str(w).encode('utf-8'))
else:
    file.write(Byte_Conv((str(w) + "x" + str(h)).encode('utf-8')))
max_val = max(data, key=data.get)
file.write(('\n' + max_val).encode('utf-8'))
file.close()
print("Image stored succesfully\n")

with open(ofn, 'rb') as file:
    binary_data = file.read()
    print(binary_data.decode('utf-8'))


# TODO 
# 1 dodaj os sprawdzanie czy plik data.pwac istnieje
# 2 potrzeba procedularnego generowania pliku, początek pliku to główne rzeczy typu wysokośc 512x512, główny kolor do zamiany, ustalenie znaków które mało ważą itp
# 3 nie wiem kurwa napij sie czegoś bo tu jebniesz


# updaż!!!! zadeklaruj kolory jako np. a,b,c ale te najbardziej common i potem będzie np a+9, b-14 jak na dużej palecdie kolorów