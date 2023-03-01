import pyscreenshot as ImageGrab
from PIL import Image

i = 0

while i <= 100:
    imagem = ImageGrab.grab()
    imagem.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela.png','png')
    img = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/tela.png')
    #img.show()
    #999 494
    #1023 495
    #1026 523
    #1027 510
    area0 = (1027, 510, 1028,511)
    corte0 = img.crop(area0)
    corte0.save('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img1.png','png')
    img_0 = Image.open('/home/oziel/Documentos/Alunos/Derick/Work_Roleta/search/img1.png')
    gg = img_0.convert('RGB').getcolors()
    print("Color inicial: ", gg)
    #[(1, (203, 177, 122))]
    #[(1, (206, 180, 125))] or gg == [(1, (205, 179, 124))]
    #[(1, (202, 176, 122))] or [(1, (204, 178, 124))] or [(1, (203, 177, 123))]
    #[(1, (204, 178, 123))] [(1, (206, 180, 125))]
    #[(1, (203, 177, 122))] [(1, (203, 177, 123))]
    if gg == [(1, (203, 177, 123))] or gg == [(1, (202, 176, 122))] or gg == [(1, (204, 178, 124))]:
        print("Cor localizada")
        print(i)
        i += 1
    
