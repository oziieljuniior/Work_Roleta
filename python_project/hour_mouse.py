import datetime as dt
import pyautogui

i = 0


while i <= 1000:
    hora1 = int(dt.datetime.now().strftime("%M"))
    
    move1 = hora1 % 3
    move2 = hora1 % 5
    move3 = hora1 % 7
    
    print(i)
    print('Hora: ', hora1)
    print("Clique 1: ", move1)
    print("Clique 2: ", move2)
    print("Clique 3: ", move3)
    
    if move1 == 0:
    #1381 297
    #1535, 300
        pyautogui.click((1381,297), interval = 2)
        i += 1
        while move1 == 0:
            hora1 = int(dt.datetime.now().strftime("%M"))
            move1 = hora1 % 3
        
    if move2 == 0:
    #1479 446
    #1538, 502
        pyautogui.click((1479, 446), interval = 2)
        i += 1
        while move2 == 0:
            hora1 = int(dt.datetime.now().strftime("%M"))
            move2 = hora1 % 5
        
    if move3 == 0:
    #1628 444
    #1538, 520
        pyautogui.click((1628, 444), interval = 2)
        i += 1
        while move3 == 0:
            hora1 = int(dt.datetime.now().strftime("%M"))
            move3 = hora1 % 7
        
    
    
    
                
    
    
