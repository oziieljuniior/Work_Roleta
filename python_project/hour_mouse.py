import datetime as dt
import pyautogui

i = 0


while i <= 100:
    hora1 = int(dt.datetime.now().strftime("%M"))
    
    move1 = hora1 % 3
    move2 = hora1 % 5
    move3 = hora1 % 7
    
    print(i)
    print('Hora: ', hora1)
    print("Clique 1: ", move1)
    print("Clique 2: ", move2)
    if move1 == 0:
        pyautogui.click((1535, 300), interval = 2)
        i += 1
        while move1 == 0:
            hora1 = int(dt.datetime.now().strftime("%M"))
            move1 = hora1 % 3
    i += 1
    
    if move2 == 0:
        pyautogui.click((1538, 502), interval = 2)
        i += 1
        while move2 == 0:
            hora1 = int(dt.datetime.now().strftime("%M"))
            move2 = hora1 % 5
        
    if move3 == 0:
        pyautogui.click((1538, 520), interval = 2)
        i += 1
        while move3 == 0:
            hora1 = int(dt.datetime.now().strftime("%M"))
            move2 = hora1 % 7
        
    
    
    
                
    
    