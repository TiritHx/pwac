# projekt wymyślony pod prysznicem, tak jestem zajebisty
# program będzie iterował po każdym pikselu i dla każdego koloru jaki jest na zdjęciu będzie dawał numer tego piksela
# jeśli jakiś kolor będzie najwięcej razy używany będzie ustawiony na default dla pozostałych pikseli
# to samo będzie sie działo z kanałem alpha dla plików png
# photo with avant-garde compression - pwac, it sounds fancy -> picture with state_of_the_art compression, yes state of the art is one word here dont judge me
from PIL import Image
from func import Image_To_Dict, File_Exist, Write_Image_Info

ifn = "serdek.png" # input file name
ofn = "data.pwsc" # output file name
img = Image.open(ifn)
pix = img.load()
w ,h = img.size
data = Image_To_Dict(w, h, pix)
File_Exist(ofn)
Write_Image_Info(ofn, w, h, data)
