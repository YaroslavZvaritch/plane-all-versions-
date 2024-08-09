import random

import pygame
pygame.init()
fon = pygame.image.load("igra/bluefon.png")
fon = pygame.transform.scale(fon,[600,600])
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Игра")
# Основной игровой цикл
running = True
clock = pygame.time.Clock()
def textdisplay(size,tylpanchikiilandishi,color,Tx,Ty):
    font = pygame.font.SysFont("Calibri",size)
    text = font.render(tylpanchikiilandishi,True,color)
    window.blit(text,[Tx,Ty])
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,size,up,down,right,left):
        super().__init__()
        self.up = pygame.image.load(up)
        self.up = pygame.transform.scale(self.up, size)
        self.down = pygame.image.load(down)
        self.down = pygame.transform.scale(self.down, size)
        self.right = pygame.image.load(right)
        self.right = pygame.transform.scale(self.right, size)
        self.left = pygame.image.load(left)
        self.left = pygame.transform.scale(self.left, size)
        self.rect = self.up.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.live = 1
        self.orintation = 1
        self.x = x
        self.y = y
        self.size = size
    def shoot(self):
        laser = Laser(self.rect.centerx,self.rect.top,[5,10],"igra/laserigrokared.png")
        GruppaLaserov.add(laser)
        GruppaDlyaVseh.add(laser)
    def doubleshoot(self):
        laser2 = Laser(self.rect.x,self.rect.top + 15,[5,10],"igra/laserigrokared.png")
        laser3 = Laser(self.rect.x + 50, self.rect.top + 15, [5, 10], "igra/laserigrokared.png")
        GruppaLaserov.add(laser2)
        GruppaLaserov.add(laser3)
        GruppaDlyaVseh.add(laser2)
        GruppaDlyaVseh.add(laser3)
    def update(self):
        if self.orintation == 1:
            self.image = self.up
        if self.orintation == 2:
            self.image = self.left
        if self.orintation == 3:
            self.image = self.down
        if self.orintation == 4:
            self.image = self.right

    def move(self,keys):
        global Points
        if keys[pygame.K_w]:
            self.rect.y -= 0
            self.orintation = 1
        if keys[pygame.K_a]:
            self.rect.x -= 2
            self.orintation = 2
        if keys[pygame.K_s]:
            self.rect.y += 0
            self.orintation = 3
        if keys[pygame.K_d]:
            self.rect.x += 2
            self.orintation = 4
        if keys[pygame.K_SPACE]:
            if cd % 50 == 0:
                self.shoot()
        if keys[pygame.K_e]:
            if cd % 25 == 0:
                if Points >= 0.01:
                    self.doubleshoot()
                    Points -= 0.01


    # def display(self):
    #     window.blit(self.image,[self.x,self.y])
anim_up = "igra/playerShip1_red.png"
anim_down = "igra/playerShip1_red.png"
anim_right = "igra/playerShip1_red.png"
anim_left = "igra/playerShip1_red.png"
player = Player(150,500,[50,50],anim_up,anim_down,anim_right,anim_left)
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

class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, size, fon):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.image.load(fon)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 0.75
        if self.rect.y >= 600:
            self.kill()

Points = 0
TimerQuoti = 60
TimerQuoti2 = 0
SpawnSpeed = 240

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, size, fon):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.image.load(fon)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global Points
        self.rect.y -= 2.5
        if self.rect.y <= -50:
            self.kill()
        if self.rect.y <= -50:
            self.kill()

GruppaPlayerov = pygame.sprite.Group(player)
GruppaEnemies = pygame.sprite.Group()
GruppaDlyaVseh = pygame.sprite.Group()
GruppaDlyaVseh.add(GruppaPlayerov)
GruppaLaserov = pygame.sprite.Group()
GruppaDlyaVseh.add(GruppaEnemies)
def SpawnVragov():
    enemy = Enemies(random.randint(0,551),-100,[50,50],f"igra/enemies/enemyBlack{random.randint(1,5)}.png")
    GruppaEnemies.add(enemy)
    GruppaDlyaVseh.add(enemy)
counter_timer = 0
cd = 1
while running:
    clock.tick(240)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.sprite.groupcollide(GruppaPlayerov, GruppaEnemies, True, True):
        exit()
    hits = pygame.sprite.groupcollide(GruppaLaserov, GruppaEnemies, True, True)
    for i in hits:
        Points += 1
    TimerQuoti2 += 1
    zapominanie_polozheniya = player.rect.copy()
    keys = pygame.key.get_pressed()
    player.move(keys)
    # Здесь вы можете добавить код для обновления игры
    if counter_timer % SpawnSpeed == 0:
        SpawnVragov()
    if SpawnSpeed >= 1 and counter_timer % 240 == 0:
        SpawnSpeed -= 1
    if TimerQuoti2 % 240 == 0:
        TimerQuoti -= 1
    if TimerQuoti == 0:
        Points -= 50

    counter_timer += 1
    cd += 1

    # Отображение изменений на экранеa
    window.blit(fon,[0,0])
    #window.blit(Fs,[Fx,Fy])
    GruppaDlyaVseh.update()
    GruppaDlyaVseh.draw(window)
    #textdisplay(20,"монет:" + str(Scolco_monetok),[255,255,255],520,20)
    textdisplay(20,"очков:" + str(Points),[255,255,255],530,0)
    textdisplay(20,"секунд осталось до сдачи квоты:" + str(TimerQuoti),[255,255,255],300,20)
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
#квота lethal company(идея)
