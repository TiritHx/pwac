# projekt wymyślony pod prysznicem, tak jestem zajebisty
# program będzie iterował po każdym pikselu i dla każdego koloru jaki jest na zdjęciu będzie dawał numer tego piksela
# jeśli jakiś kolor będzie najwięcej razy używany będzie ustawiony na default dla pozostałych pikseli
# to samo będzie sie działo z kanałem alpha dla plików png
# photo with avant-garde compression - pwac, it sounds fancy -> picture with state_of_the_art compression, yes state of the art is one word here dont judge me
from PIL import Image
from func import Image_To_Dict, File_Exist, Write_Image_Info

loop = True

while(loop):
    inp = input("Image to PWSC - 1\nPWSC to Image - 2\nQuit - 3\n")
    try:
        inp = int(inp)
    except:
        inp = 0
    match inp:
        case 1:
            ifn = input("Enter name of input file with extension like this: example.png\n")
            ofn = input("Enter name of the output file\n") + ".pwsc"
            try: 
                img = Image.open(ifn)
                pix = img.load()
                w ,h = img.size
                data = Image_To_Dict(w, h, pix)
                File_Exist(ofn)
                Write_Image_Info(ofn, w, h, data)
            except:
                print("File not found\n")
        case 2:
            print("Not yet amigo\n") # I will do that eventually
        case 3:
            loop = False
        case _:
            print("Unknown command\n")



