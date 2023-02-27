import os
import time
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image
from playsound import playsound

#from openpyxl import Workbook

path_original = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/data_teste/Numeros'
path_salvo = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/data_teste/Numero_Tratado'

i = 1
add_numeros = []

m = 0
n = 0
o = 0

t_0 = int(input("Quantidade de coletas: "))
sound = int(input("Repetições de coluna: "))
while i <= t_0:
    caminho = os.listdir(path_original)
    t = len(caminho)
    #print(i , t)
    
    if t == i:
        time.sleep(2)
        name = path_original + '/' + str(i) + 'img.png'
        
        img1 = Image.open(name)
        area = (10,5,40,35)
        corte = img1.crop(area)
        name1 = path_salvo + '/' + str(i) + 'img.png'
        corte.save(name1,'png')
        
        imagem = cv.imread(name1)
        gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
        #thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
        
        dsize = (640,480)
        resized = cv.resize(gray, dsize, fx=16.0, fy=16.0, interpolation=cv.INTER_LINEAR)
        
        kernel = np.ones((1,1), np.float64)/2
        dst = cv.filter2D(resized,-1,kernel)  
        
        kernel1 = np.ones((3,3), np.uint8)/5
        erode = cv.erode(dst, kernel1, iterations = 2)
        kernel2 = np.ones((3,3), np.uint8)/5
        morp = cv.morphologyEx(erode, cv.MORPH_OPEN, kernel2)
        #match_template = cv.matchTemplate(morp,dst,cv.TM_CCOEFF_NORMED)
        
        blur = cv.GaussianBlur(morp, (3,3), 1)
        thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
        
        
        #plt.imshow(thresh),plt.show()
        
        custom_config10 = r'-l eng --oem 3 --psm 13 -c tessdit_char_whitelist=0123456789'
        
        text10 = pytesseract.image_to_string(thresh, config = custom_config10)
        
        
        print(i,":" , text10)
        
        a = text10.split('\n\x0c')
        if a[0] == '271':
            b = a.replace('271','27')
            a = b
        elif a[0] == 'Ws':
            b = a.replace('Ws','17')
            a = b
        bad = [',','.']
        for j in bad:
            b = a[0].replace(j,'')
            a = b
        print(a)
        add_numeros.append(int(a))
        
        if int(a) % 3 == 0 and int(a) != 0:
            m += 1
            n = 0
            o = 0
        elif int(a) % 3 == 1:
            m = 0
            n += 1
            o = 0
        elif int(a) % 3 == 2:
            m = 0
            n = 0
            o += 1
        else:
            m = 0
            n = 0
            o = 0
        
        if m == sound or n == sound or o == sound:
            print('encontrei um numero')
            playsound('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/python_project/att.mp3')
        
        
        i += 1

print(add_numeros)
