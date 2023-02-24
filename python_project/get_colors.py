import pyscreenshot as ImageGrab
from PIL import Image

i = 0

while i <= 100:
    imagem = ImageGrab.grab()
    imagem.save('/home/oziel/Documentos/Alunos/Derick/Roleta_Fire/search/tela.png','png')
    img = Image.open('/home/oziel/Documentos/Alunos/Derick/Roleta_Fire/search/tela.png')
    #img.show()
    area0 = (1500,623,1501,624)
    corte0 = img.crop(area0)
    corte0.save('/home/oziel/Documentos/Alunos/Derick/Roleta_Fire/search/img1.png','png')
    img_0 = Image.open('/home/oziel/Documentos/Alunos/Derick/Roleta_Fire/search/img1.png')
    gg = img_0.convert('RGB').getcolors()
    print("Color inicial: ", gg)
    if gg == [(1, (206, 180, 125))] or gg == [(1, (205, 179, 124))]:
        print("Cor localizada")
        print(i)
        i += 1
    