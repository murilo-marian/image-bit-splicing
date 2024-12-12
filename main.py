import numpy as np
from PIL import Image

def get_bit(number, n):
    return (number >> n) & 1

def transformarImagem(img, bit, mode):
    newImage = []
    for linha in img:
        if mode == "1":
            novaLinha = [get_bit(number, bit) * 255 for number in linha]
        elif mode == "L":
            novaLinha = [get_bit(number, bit) * (2 ** bit) for number in linha]
        else:
            novaLinha = [sum(get_bit(number, bit - i) * (2 ** (bit - i)) for i in range(3)) for number in linha]
        newImage.append(novaLinha)
    return newImage

def salvarImagem(array, nomeArquivo):
    arraynp = np.array(array, dtype=np.uint8)
    img = Image.fromarray(arraynp, mode="L")
    img.save(nomeArquivo)
    
img = Image.open("Fig0314(a)(100-dollars).tif")
imgArray = np.array(img)

for i in range(8):
    newImage = transformarImagem(imgArray, i, mode="1")
    salvarImagem(newImage, "spliceBinary" + str(i+1) + ".tif")


for i in range(8):
    newImage = transformarImagem(imgArray, i, mode="L")
    salvarImagem(newImage, "splice" + str(i+1) + ".tif")

newImage = transformarImagem(imgArray, i, mode="3")
salvarImagem(newImage, "splicethree" + str(i+1) + ".tif")


print("done")