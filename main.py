# projekt wymyślony pod prysznicem, tak jestem zajebisty
# program będzie iterował po każdym pikselu i dla każdego koloru jaki jest na zdjęciu będzie dawał numer tego piksela
# jeśli jakiś kolor będzie najwięcej razy używany będzie ustawiony na default dla pozostałych pikseli
# to samo będzie sie działo z kanałem alpha dla plików png
# photo with avant-garde compression - pwac, it sounds fancy
from PIL import Image
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
# file = open('data.txt', 'w')
# file.write(str(data).replace(" ", "").replace("'", "")) # potrzeba procedularnego generowania pliku, początek pliku to główne rzeczy typu wysokośc 512x512, główny kolor do zamiany, ustalenie znaków które mało ważą itp
# file.close() 
print("\ndone\n")