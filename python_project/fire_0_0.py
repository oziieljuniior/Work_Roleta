import pyscreenshot as ImageGrab
from PIL import Image
import datetime as dt
import time
i = 0
t_0 = int(input("Quantidade de coleta: "))

while i <= t_0:
    imagem = ImageGrab.grab()
    imagem.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela.png','png')
    img = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela.png')
    #img.show()
    #(1027, 510, 1028,511)
    #(1026, 523, 1027, 524)
    area0 = (1027, 510, 1028,511)
    corte0 = img.crop(area0)
    corte0.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img1.png','png')
    img_0 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img1.png')
    gg = img_0.convert('RGB').getcolors()
    print("Color inicial: ", gg)
    
    if gg == [(1, (203, 177, 123))] or gg == [(1, (202, 176, 122))] or gg == [(1, (204, 178, 124))]:
        print("Cor localizada")
        print(i)
        imagem1 = ImageGrab.grab()
        imagem1.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/fig1.png','png')
        img1 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/fig1.png')
        #985, 460, 1032, 503
        #995 494 1030 523
        area1 = (996, 484, 1026 , 514)
        corte1 = img1.crop(area1)
        name = str(i + 1) + 'img.png'
        path_save = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/data_teste/Numeros/' + name
        corte1.save(path_save,'png')
        
        j = 0
        k = 0
        while j == 0:
            imagem2 = ImageGrab.grab()
            imagem2.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela1.png','png')
            img2 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela1.png')
            #img.show()
            
            area2 = (1027, 510, 1028,511)
            #1284 288 1578 564
            #1263, 272, 1535, 535
            area3 = (1267 , 294, 1546,  551)
            
            corte2 = img2.crop(area2)
            corte2.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img2.png','png')
            img_1 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img2.png')
            gg0 = img_1.convert('RGB').getcolors()
            print("Color inicial: ", gg0)
            time.sleep(6)
            
            
            if gg0 != [(1, (203, 177, 123))] or gg0 != [(1, (202, 176, 122))] or gg0 != [(1, (204, 178, 124))]:    
                print("Imagem salve na data")
                i += 1
                j += 1
                
                hour = int(dt.datetime.now().strftime("%M"))
                
                if hour % 6 == 0 and k == 0:
                    
                    corte3 = img2.crop(area3)
                    name2 = str(i + 1) + '_Historico_Numeros.png'
                    path_save2 = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/data_teste/Numeros_Gerais/' + name2 
                    corte3.save(path_save2, 'png')
                    k = k + 1
        
