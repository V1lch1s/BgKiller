from PIL import Image
#from PyQt5.QtWidgets import QInputDialog
import numpy as np
import cv2

print("----Eliminador de Fondo (Transparentador de pngs)----")
print("\nRequisitos de entrada:\n")
print("1-La imagen de entrada debe ser PNG\n")
print("2-El fondo debe ser RGB(0, 255, 0)\n\n")
carpeta = str(input('Carpeta (Nombre): '))
imgName = str(input("Imagen que desea alterar (Imagen.png): "))
img = Image.open(carpeta+'/'+imgName)

#Color a retirar: RGB: ( 34, 177,  76)
img = img.convert('RGBA')
pixdata = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x,y][0] == 0 or pixdata[x,y][0] == 1 or pixdata[x,y][0] == 2 or pixdata[x,y][0] == 3 or pixdata[x,y][0] == 4 or pixdata[x,y][0] == 5 and pixdata[x,y][1] == 255 and pixdata[x,y][2] == 0 or pixdata[x,y][2] == 1 or pixdata[x,y][2] == 2 or pixdata[x,y][2] == 3 or pixdata[x,y][2] == 4 or pixdata[x,y][2] == 5:
           pixdata[x, y] = (255, 255, 255,0)

img.save("{}/{}".format(carpeta,imgName)) #Image.save(fp, format=None, **params)
img.show()


