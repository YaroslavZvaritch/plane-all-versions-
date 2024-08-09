# import tkinter as tk
# root = tk.Tk()
# root.title("Мое первое приложение на Tkinter")  # Устанавливаем заголовок окна
# root.geometry("400x300")  # Устанавливаем размеры окна (ширина x высота)
# root.resizable(True, True)
# root.minsize(1,1)
# root.maxsize(1920,1080)
# root.iconbitmap(default="controller.ico")
#
# # Создаем кнопку
# A = 0
# button = tk.Button(root, text="Нажатий:" + str(A))
# B = 0
# button2 = tk.Button(root, text="bla-bla-bla" + str(B))
# def onpress(event):
#     global B,A
#     B += 1
#     button["text"] = "Нажатий:" + str(A)
# def onpress2(event2):
#     global A,B
#     A += 1
#     button2["text"] = "bla-bla-bla" + str(B)
# button.bind("<ButtonPress-1>", onpress)
# button2.bind("<ButtonPress-1>", onpress2)
# # Размещаем кнопку в окне
# button.pack()
# button2.pack()
#
# root.mainloop()
import random

import pygame
pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Игра")
# Основной игровой цикл
running = True
F = "france.png"
Fs = pygame.image.load(F)
Fs = pygame.transform.scale(Fs,[200,200])
A = pygame.Rect(0,0,100,100)
X = 0
Y = 0
B = pygame.Rect(500,500, 100, 100)
Xe = 500
Ye = 500
B.x = Xe
B.y = Ye
Fx = 18
Fy = 12
clock = pygame.time.Clock()
def textdisplay(size,tylpanchikiilandishi,color,Tx,Ty):
    font = pygame.font.SysFont("Calibri",size)
    text = font.render(tylpanchikiilandishi,True,color)
    window.blit(text,[Tx,Ty])
Tx = 0
Ty = 0
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,size,up,down,right,left):
        super().__init__()
        self.up = []
        self.down = []
        self.right = []
        self.left = []
        for i in up:
            image = pygame.image.load(i)
            self.up.append(pygame.transform.scale(image,size))
        for i in down:
            image = pygame.image.load(i)
            self.down.append(pygame.transform.scale(image, size))
        for i in left:
            image = pygame.image.load(i)
            self.left.append(pygame.transform.scale(image, size))
        for i in right:
            image = pygame.image.load(i)
            image = pygame.transform.scale(image, size)
            image = pygame.transform.flip(image,True,False)
            self.right.append(image)
        self.image = self.up[0]
        self.images = [self.down[1]]
        self.index = 0
        self.rect = self.images[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orintation = 0
        self.x = x
        self.y = y
        self.size = size
    def update(self):
        if self.orintation == 0:
            self.index = (self.index + 1)% len(self.images)
            self.image = self.images[self.index]
        if self.orintation == 1:
            self.index = (self.index + 1) % len(self.up)
            self.image = self.up[self.index]
        if self.orintation == 2:
            self.index = (self.index + 1) % len(self.left)
            self.image = self.left[self.index]
        if self.orintation == 3:
            self.index = (self.index + 1) % len(self.down)
            self.image = self.down[self.index]
        if self.orintation == 4:
                self.index = (self.index + 1) % len(self.right)
                self.image = self.right[self.index]

    def move(self,keys):
        if keys[pygame.K_w]:
            self.rect.y -= 10
            self.orintation = 1
        if keys[pygame.K_a]:
            self.rect.x -= 10
            self.orintation = 2
        if keys[pygame.K_s]:
            self.rect.y += 10
            self.orintation = 3
        if keys[pygame.K_d]:
            self.rect.x += 10
            self.orintation = 4
        if keys[pygame.K_a] == False and keys[pygame.K_s] == False and keys[pygame.K_d] == False and keys[pygame.K_w] == False:
            self.orintation = 0
    # def display(self):
    #     window.blit(self.image,[self.x,self.y])
anim_up = ["sprites/sprite5.png","sprites/sprite6.png","sprites/sprite7.png"]
anim_down = ["sprites/sprite1.png","sprites/sprite2.png","sprites/sprite3.png"]
anim_right = ["sprites/sprite9.png","sprites/sprite10.png","sprites/sprite11.png"]
anim_left = ["sprites/sprite9.png","sprites/sprite10.png","sprites/sprite11.png"]
player = Player(150,150,[80,80],anim_up,anim_down,anim_right,anim_left)
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,size,color):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
FirstBlock = Block(0,0,[50,50],[10,20,30])
SecondBlock = Block(50,0,[50,50],[10,20,30])
ThirdBlock = Block(100,0,[50,50],[10,20,30])
FourthBlock = Block(150,0,[50,50],[10,20,30])
FifthBlock = Block(200,0,[50,50],[10,20,30])
SixthBlock = Block(250,0,[50,50],[10,20,30])
SeventhBlock = Block(300,0,[50,50],[10,20,30])
EighthBlock = Block(350,0,[50,50],[10,20,30])
NinethBlock = Block(400,0,[50,100],[10,20,30])
TenthBlock = Block(450,0,[50,50],[10,20,30])
EleventhBlock = Block(500,0,[50,50],[10,20,30])
TwelvethBlock = Block(550,0,[50,50],[10,20,30])
ThirdTeenBlock = Block(0,50,[50,50],[10,20,30])
FourthTeenBlock = Block(0,100,[50,50],[10,20,30])
FifthTeenBlock = Block(0,150,[50,50],[10,20,30])
SixthTeenBlock = Block(0,200,[50,50],[10,20,30])
SeventhTeenBlock = Block(0,250,[50,50],[10,20,30])
EighthTeenBlock = Block(0,300,[50,50],[10,20,30])
NinethTeenBlock = Block(0,350,[50,50],[10,20,30])
TwentythBlock = Block(0,400,[50,50],[10,20,30])
TwentyFirstBlock = Block(0,450,[50,50],[10,20,30])
TwentySecondBlock = Block(0,500,[50,50],[10,20,30])
TwentyThirdBlock = Block(0,550,[50,50],[10,20,30])
TwentyFourthBlock = Block(400,100,[50,50],[10,20,30])
TwentyFifthBlock = Block(400,150,[50,50],[10,20,30])
TwentySixthBlock = Block(450,150,[50,50],[10,20,30])
TwentySeventhBlock = Block(500,150,[50,50],[10,20,30])
TwentyEightBlock = Block(500,150,[50,50],[10,20,30])
TwentyNinethBlock = Block(500,300,[50,50],[10,20,30])
ThirtyFirstBlock = Block(450,300,[50,50],[10,20,30])
ThirtythSecondBlock = Block(500,350,[50,50],[10,20,30])
ThirtythThirdBlock = Block(500,400,[50,50],[10,20,30])
ThirtyFourthBlock = Block(500,450,[50,50],[10,20,30])
ThirtyFifthBlock = Block(450, 450, [50, 50], [10, 20, 30])
ThirtySixthBlock = Block(400, 450, [50, 50], [10, 20, 30])
ThirtySeventhBlock = Block(350, 450, [50, 50], [10, 20, 30])
ThirtyEightBlock = Block(350, 500, [50, 50], [10, 20, 30])
ThirtyNinethBlock = Block(350, 550, [50, 50], [10, 20, 30])
FourtyFirstBlock = Block(400,300,[50,50],[10,20,30])
FourtySecondBlock = Block(350,300,[50,50],[10,20,30])
FourtyThirdBlock = Block(300,300,[50,50],[10,20,30])
FourtyFourthBlock = Block(250,300,[50,50],[10,20,30])
FourtyFifthBlock = Block(200,300,[50,50],[10,20,30])
TwentyNinethBlock = Block(500,300,[50,50],[10,20,30])
TwentyNinethBlock = Block(500,300,[50,50],[10,20,30])
TwentyNinethBlock = Block(500,300,[50,50],[10,20,30])
#Coin = Block(300,200,[25,25],[255,255,0])
#Coin2 = Block(500,100,[25,25],[255,255,0])
Teleport = Block(500,100,[50,50],[255,25,50])
InvisibleBlock = Block(400,550,[50,50],[255,25,50])
GruppaTeleportov = pygame.sprite.Group(Teleport)
Scolco_monetok = 0
GruppaBlockov = pygame.sprite.Group()
GruppaBlockov.add(FirstBlock,SecondBlock,ThirdBlock,FourthBlock,FifthBlock,SixthBlock,SeventhBlock,EighthBlock,NinethBlock,TenthBlock,EleventhBlock,TwelvethBlock,ThirdTeenBlock,FourthTeenBlock,FifthTeenBlock,SixthTeenBlock,SeventhTeenBlock,EighthTeenBlock,NinethTeenBlock,TwentythBlock,TwentyFirstBlock,TwentySecondBlock,TwentyThirdBlock,TwentyFourthBlock,TwentyFifthBlock,TwentySixthBlock,TwentySeventhBlock,TwentyEightBlock,TwentyNinethBlock,ThirtyFirstBlock,ThirtythSecondBlock,ThirtythThirdBlock,ThirtyFourthBlock,ThirtyFifthBlock,ThirtySixthBlock,ThirtySeventhBlock,ThirtyEightBlock,ThirtyNinethBlock,FourtyFirstBlock,FourtySecondBlock,FourtyThirdBlock,FourtyFourthBlock,FourtyFifthBlock)
GruppaPlayerov = pygame.sprite.Group(player)
GruppaDlyaVseh = pygame.sprite.Group()
spisokmonetok = []
WE = input("Ведите количество монеток:")
TE = input("Ведите количество телепортов:")
GruppaCoinov = pygame.sprite.Group()
def spawnmonetok(monetokstolco):
    spisokmonetok = []
    while monetokstolco >= 1:
        Coin3 = Block(random.randint(0,525), random.randint(0,525), [25, 25], [255, 255, 0])
        if not pygame.sprite.spritecollide(Coin3,GruppaBlockov,False) and not pygame.sprite.spritecollide(Coin3,GruppaPlayerov,False) and not pygame.sprite.spritecollide(Coin3,GruppaCoinov,False) :
            print("появление монетки")
            spisokmonetok.append(Coin3)
            GruppaDlyaVseh.add(Coin3)
            GruppaCoinov.add(spisokmonetok[-1])
            monetokstolco -= 1
spisokteleportov = []
def spawnTeleportov(Teleportovstolco):
    spisokteleportov = []
    while Teleportovstolco >= 1:
        Teleport3 = Block(random.randint(0,525), random.randint(0,525), [50, 50], [255, 25, 50])
        if not pygame.sprite.spritecollide(Teleport3,GruppaBlockov,False) and not pygame.sprite.spritecollide(Teleport3,GruppaPlayerov,False) and not pygame.sprite.spritecollide(Teleport3,GruppaCoinov,False) and not pygame.sprite.spritecollide(Teleport3,GruppaTeleportov,False):
            print("появление телепорта")
            spisokteleportov.append(Teleport3)
            GruppaDlyaVseh.add(Teleport3)
            GruppaTeleportov.add(spisokteleportov[-1])
            Teleportovstolco -= 1
GruppaDlyaVseh.add(GruppaPlayerov,GruppaBlockov,GruppaTeleportov)
spawnmonetok(int(WE))
spawnTeleportov((int(TE)))
while running:
    window.fill((213,132,123))
    clock.tick(5)
    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
        #     A.y -= 20
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        #     A.y += 20
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
        #     A.x -= 20
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        #     A.x += 20
        if event.type == pygame.QUIT:
            running = False
    zapominanie_polozheniya = player.rect.copy()
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.update()
    # Здесь вы можете добавить код для обновления игры
    if pygame.sprite.spritecollide(player,GruppaBlockov,False):
        print("соприкосновение")
        player.rect = zapominanie_polozheniya
    if pygame.sprite.spritecollide(player,GruppaCoinov,True):
        print("получение монетки")
        Scolco_monetok += 1
    if pygame.sprite.spritecollide(player,GruppaTeleportov,True):
        print("телепорт")
        while True:
            player.rect.x = random.randint(0,500)
            player.rect.y = random.randint(0,500)
            if not pygame.sprite.spritecollide(player,GruppaBlockov,False) and not pygame.sprite.spritecollide(player,GruppaCoinov,False) and not pygame.sprite.spritecollide(player,GruppaTeleportov,False):
                break
    if pygame.sprite.spritecollide(player,[InvisibleBlock],False):
        print("game over")
        print("очков:" + str(Scolco_monetok))
        player.rect = zapominanie_polozheniya
    # Отображение изменений на экране
    pygame.draw.rect(window, (0, 128, 255),A)
    pygame.draw.rect(window, (0, 128, 255),B)
    #window.blit(Fs,[Fx,Fy])
    GruppaDlyaVseh.draw(window)
    textdisplay(20,"монет:" + str(Scolco_monetok),[255,255,255],520,20)
    pygame.display.flip()

# Выход из Pygame
pygame.quit()

