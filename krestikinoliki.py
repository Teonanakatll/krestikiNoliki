from tkinter import *
from random import randint
from time import sleep
from winsound import Beep

# Анимация победы
def winAnim(x1, y1, x2, y2, x3, y3):
    global playGame, dataImage, copyData
    playGame = False

    n = 0

    for i in range(k):
        for j in range(k):
            copyData[i][j] = dataImage[i][j]

    while (n < 11):
        if (n % 2 == 0):            
            dataImage[x1][y1] = 6
            dataImage[x2][y2] = 6
            dataImage[x3][y3] = 6
            n += 1
            updatePictures()
        else:
            for i in range(k):
                for j in range(k):
                    dataImage[i][j] = copyData[i][j]
            n += 1
            updatePictures()
        sleep(0.4)

    startButton["state"] = NORMAL
      
    

    
        

# Проверка выигрыша
def checkWin():
    
    if (sum(dataImage[0]) == 0 or sum(dataImage[0]) == 3):
        print(333)
        winAnim(0, 0, 0, 1, 0, 2)
    elif (sum(dataImage[1]) == 0 or sum(dataImage[1]) == 3):
        winAnim(1, 0, 1, 1, 1, 2)
    elif (sum(dataImage[2]) == 0 or sum(dataImage[2]) == 3):
        winAnim(2, 0, 2, 1, 2, 2)
    elif (dataImage[0][0] + dataImage[1][0] + dataImage[2][0] == 0 or
          dataImage[0][0] + dataImage[1][0] + dataImage[2][0] == 3):
        winAnim(0, 0, 1, 0, 2, 0)
    elif (dataImage[0][1] + dataImage[1][1] + dataImage[2][1] == 0 or
          dataImage[0][1] + dataImage[1][1] + dataImage[2][1] == 3):
        winAnim(0, 1, 1, 1, 2, 1)
    elif (dataImage[0][2] + dataImage[1][2] + dataImage[2][2] == 0 or
          dataImage[0][2] + dataImage[1][2] + dataImage[2][2] == 3):
        winAnim(0, 2, 1, 2, 2, 2)
    elif (dataImage[0][0] + dataImage[1][1] + dataImage[2][2] == 0 or
          dataImage[0][0] + dataImage[1][1] + dataImage[2][2] == 3):
        winAnim(0, 0, 1, 1, 2, 2)
    elif (dataImage[0][2] + dataImage[1][1] + dataImage[2][0] == 0 or
          dataImage[0][2] + dataImage[1][1] + dataImage[2][0] == 3):
        winAnim(0, 2, 1, 1, 2, 0)
        
                    
                                                           
          
# Обновление картинок
def updatePictures():
    for i in range(k):
        for j in range(k):
            labelImage[i][j]["image"] = image[dataImage[i][j]]

    root.update()

# Ход
def step(x, y):
    global dataImage, stepColor
    if (playGame):
        if (stepColor):
            dataImage[x][y] = 0
            print(stepColor)
            stepColor = False
            Beep(2000, 200)
        else:
            dataImage[x][y] = 1
            print(stepColor) 
            stepColor = True
            Beep(1000, 200)
    else:
        return 0
    
    updatePictures()
    checkWin()

# Начало игры    
def startGame():
    global stepColor, playGame
    playGame = True
    startButton["state"] = DISABLED

    m = randint(5, 15)
    n = randint(0, 1)

    for i in range(m):
        if (n == 0):
            micro01["image"] = image[4]
            micro02["image"] = image[3]
            n = 1
            Beep(3000, 20)
        else:
            micro01["image"] = image[2]
            micro02["image"] = image[4]
            n = 0
            Beep(4000, 20)
        sleep(0.4)
        
        root.update()
    if (n == 0):
        # Синий
        stepColor = True
    else:
        # Зелёный
        stepColor = False




# Цвет фона
white = "#ffffff"

# Количество клеток по х и у
k = 3


# Ширина и высота лейблов
l = 176

root = Tk()
root.resizable(False, False)
root.title("Крестики-Нолики")
root["bg"] = white

WIDTH = 552
HEIGHT = 584

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
root.iconbitmap("ico.ico")

# Игровое поле
desk_image = PhotoImage(file="desk.png")
desk = Label(root, image=desk_image)
desk.place(x=5, y=5)

# Кнопка Старт
startButton = Button(root, text="Старт", width=10)
startButton.place(x=18, y=552)
startButton["command"] = startGame

# Картинки
smile_image = PhotoImage(file="sm.png")
green_image = PhotoImage(file="gr.png")
blue_image = PhotoImage(file="bl.png")
microGreen = PhotoImage(file="grm.png")
microBlue = PhotoImage(file="blm.png")
microWhite = PhotoImage(file="white.png")
brill_image = PhotoImage(file="br.png")

# Список с картинками
image = []
image.append(green_image)
image.append(blue_image)
image.append(microGreen)
image.append(microBlue)
image.append(microWhite)
image.append(smile_image)
image.append(brill_image)

# Микро лейблы
micro01 = Label(root, image=image[2])
micro01.place(x=130, y=550)
micro02 = Label(root, image=image[3])
micro02.place(x=160, y=552)


# Список Label
labelImage = []

# Математическая модель игрового поля
dataImage = []
copyData = []

for i in range(k):
    labelImage.append([])
    dataImage.append([])
    copyData.append([])
    for j in range(k):
        copyData[i].append(5)
        dataImage[i].append(5)
        labelImage[i].append(Label(root))
        labelImage[i][j].place(x=18 + j * l, y=18 + i * l)
        labelImage[i][j]["image"] = image[dataImage[i][j]]
        labelImage[i][j].bind("<Button-1>", lambda e, x=i, y=j: step(x, y))
        
# Цвет хода
stepColor = BooleanVar()

playGame = False    

root.mainloop()

