import pyscreenshot as ImageGrab
from PIL import Image

i = 0

while i <= 100:
    imagem = ImageGrab.grab()
    imagem.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela.png','png')
    img = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela.png')
    #img.show()
    area0 = (1500,623,1501,624)
    corte0 = img.crop(area0)
    corte0.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img1.png','png')
    img_0 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img1.png')
    gg = img_0.convert('RGB').getcolors()
    print("Color inicial: ", gg)
    if gg == [(1, (206, 180, 125))] or gg == [(1, (205, 179, 124))]:
        print("Cor localizada")
        print(i)
        imagem1 = ImageGrab.grab()
        imagem1.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/fig1.png','png')
        img1 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/fig1.png')
        area1 = (1476, 603, 1504, 625)
        corte1 = img1.crop(area1)
        name = str(i + 1) + 'img.png'
        path_save = '/home/oziel/Documentos/Alunos/Derick/Work_Roleta/data_teste/' + name
        corte1.save(path_save,'png')
        
        j = 0
        while j == 0:
            imagem2 = ImageGrab.grab()
            imagem2.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela1.png','png')
            img2 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela1.png')
            #img.show()
            area2 = (1500,623,1501,624)
            corte2 = img2.crop(area2)
            corte2.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img2.png','png')
            img_1 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img2.png')
            gg0 = img_1.convert('RGB').getcolors()
            print("Color inicial: ", gg0)
            if gg0 != [(1, (206, 180, 125))] or gg0 != [(1, (205, 179, 124))]:    
                print("Imagem salve na data")
                i += 1
                j += 1
        