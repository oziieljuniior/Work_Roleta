# -*- coding: utf-8 -*-
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image


path_original = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/Data2/Numeros'
path_imagens_tratada = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/Data2/Numero_Tratado'
imagens_salvas = os.listdir(path_imagens_tratada)
imagens = os.listdir(path_original)
t = len(imagens)
#print(t)
i = 1

ad = []
while i <= t:
    #print(i)
    name = path_original + '/' + str(i) + 'img.png'
    name1 = path_imagens_tratada + '/' + str(i) + 'img.png'
    
    img1 = Image.open(name)
    area = (10,5,40,35)
    corte = img1.crop(area)
    corte.save(name1)
    
    imagem = cv.imread(name1)
    
    plt.imshow(img1),plt.show()
    plt.imshow(imagem),plt.show()
    
    
    #print(name)
    
    
    
# =============================================================================
#     imagem = cv.imread(name)
#     gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
#     #thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
#     
#     dsize = (640,480)
#     resized = cv.resize(gray, dsize, fx=16.0, fy=16.0, interpolation=cv.INTER_LINEAR)
#     
#     kernel = np.ones((1,1), np.float64)/2
#     dst = cv.filter2D(resized,-1,kernel)  
#     
#     kernel1 = np.ones((3,3), np.uint8)/5
#     erode = cv.erode(dst, kernel1, iterations = 2)
#     kernel2 = np.ones((3,3), np.uint8)/5
#     morp = cv.morphologyEx(erode, cv.MORPH_OPEN, kernel2)
#     #match_template = cv.matchTemplate(morp,dst,cv.TM_CCOEFF_NORMED)
#     
#     blur = cv.GaussianBlur(morp, (3,3), 1)
#     thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
#     
#     
#     plt.imshow(thresh),plt.show()
#     #-c tessedit_char_whitelist=0123456789
#     #--oem 3 --psm 6
#     #8
#     #13
#     custom_config10 = r'-l eng --oem 3 --psm 13 -c tessdit_char_whitelist=0123456789'
#     
#     text10 = pytesseract.image_to_string(thresh, config = custom_config10)
#     
#     
#     print(i,":" , text10)
#     
#     ad.append(text10)
#     
# =============================================================================
    i += 1
    
print(ad)