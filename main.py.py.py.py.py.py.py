import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Игра")
# Основной игровой цикл
running = True
F = "france.png"
Fs = pygame.image.load(F)
Fs = pygame.transform.scale(Fs, [200, 200])
A = pygame.Rect(0, 0, 100, 100)
X = 0
Y = 0
B = pygame.Rect(500, 500, 100, 100)
Xe = 500
Ye = 500

B.x = Xe
B.y = Ye
Fx = 18
Fy = 12
clock = pygame.time.Clock()


def textdisplay(size, tylpanchikiilandishi, color, Tx, Ty):
    font = pygame.font.SysFont("Calibri", size)
    text = font.render(tylpanchikiilandishi, True, color)
    window.blit(text, [Tx, Ty])


Tx = 0
Ty = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size, up, down, right, left):
        super().__init__()
        self.up = []
        self.down = []
        self.right = []
        self.left = []
        for i in up:
            image = pygame.image.load(i)
            self.up.append(pygame.transform.scale(image, size))
        for i in down:
            image = pygame.image.load(i)
            self.down.append(pygame.transform.scale(image, size))
        for i in left:
            image = pygame.image.load(i)
            self.left.append(pygame.transform.scale(image, size))
        for i in right:
            image = pygame.image.load(i)
            image = pygame.transform.scale(image, size)
            image = pygame.transform.flip(image, True, False)
            self.right.append(image)
        self.image = self.up[0]
        self.images = [self.down[1]]
        self.index = 0
        self.rect = self.images[0].get_rect()
        self.orintation = 0
        self.x = x
        self.y = y
        self.size = size

    def update(self):
        if self.orintation == 0:
            self.index = (self.index + 1) % len(self.images)
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

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= 10
            self.orintation = 1
        if keys[pygame.K_a]:
            self.x -= 10
            self.orintation = 2
        if keys[pygame.K_s]:
            self.y += 10
            self.orintation = 3
        if keys[pygame.K_d]:
            self.x += 10
            self.orintation = 4
        if keys[pygame.K_a] == False and keys[pygame.K_s] == False and keys[pygame.K_d] == False and keys[
            pygame.K_w] == False:
            self.orintation = 0

    def display(self):
        window.blit(self.image, [self.x, self.y])


anim_up = ["sprites/sprite5.png", "sprites/sprite6.png", "sprites/sprite7.png"]
anim_down = ["sprites/sprite1.png", "sprites/sprite2.png", "sprites/sprite3.png"]
anim_right = ["sprites/sprite9.png", "sprites/sprite10.png", "sprites/sprite11.png"]
anim_left = ["sprites/sprite9.png", "sprites/sprite10.png", "sprites/sprite11.png"]
player = Player(150, 150, [80, 80], anim_up, anim_down, anim_right, anim_left)


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=[x, y])


_1Block = Block(0, 0, [50, 50], [10, 20, 30])
_2Block = Block(50, 0, [50, 50], [10, 20, 30])
_3Block = Block(100, 0, [50, 50], [10, 20, 30])
_4Block = Block(150, 0, [50, 50], [10, 20, 30])
_5Block = Block(200, 0, [50, 50], [10, 20, 30])
_6Block = Block(250, 0, [50, 50], [10, 20, 30])
_7Block = Block(300, 0, [50, 50], [10, 20, 30])
_8Block = Block(350, 0, [50, 50], [10, 20, 30])
_9Block = Block(450, 0, [50, 50], [10, 20, 30])
_10Block = Block(500, 0, [50, 50], [10, 20, 30])
_11Block = Block(550, 0, [50, 50], [10, 20, 30])
_12Block = Block(550, 50, [50, 50], [10, 20, 30])
_13Block = Block(550, 100, [50, 50], [10, 20, 30])
_14Block = Block(550, 150, [50, 50], [10, 20, 30])
_15Block = Block(550, 200, [50, 50], [10, 20, 30])
_16Block = Block(550, 250, [50, 50], [10, 20, 30])
_17Block = Block(550, 300, [50, 50], [10, 20, 30])
_18Block = Block(550, 350, [50, 50], [10, 20, 30])
_19Block = Block(550, 400, [50, 50], [10, 20, 30])
_20Block = Block(550, 450, [50, 50], [10, 20, 30])
_21Block = Block(550, 500, [50, 50], [10, 20, 30])
_22Block = Block(550, 550, [50, 50], [10, 20, 30])
_23Block = Block(500, 550, [50, 50], [10, 20, 30])
_24Block = Block(450, 550, [50, 50], [10, 20, 30])
_25Block = Block(400, 550, [50, 50], [10, 20, 30])
_26Block = Block(350, 550, [50, 50], [10, 20, 30])
_27Block = Block(300, 550, [50, 50], [10, 20, 30])
_28Block = Block(250, 550, [50, 50], [10, 20, 30])
_29Block = Block(200, 550, [50, 50], [10, 20, 30])
_30Block = Block(150, 550, [50, 50], [10, 20, 30])
_31Block = Block(100, 550, [50, 50], [10, 20, 30])
_32Block = Block(50, 550, [50, 50], [10, 20, 30])
_33Block = Block(0, 550, [50, 50], [10, 20, 30])
_34Block = Block(0, 500, [50, 50], [10, 20, 30])
_35Block = Block(0, 450, [50, 50], [10, 20, 30])
_36Block = Block(0, 400, [50, 50], [10, 20, 30])
_37Block = Block(0, 350, [50, 50], [10, 20, 30])
_38Block = Block(0, 300, [50, 50], [10, 20, 30])
_39Block = Block(0, 250, [50, 50], [10, 20, 30])
_40Block = Block(0, 200, [50, 50], [10, 20, 30])
_41Block = Block(0, 150, [50, 50], [10, 20, 30])
_42Block = Block(0, 100, [50, 50], [10, 20, 30])
_43Block = Block(0, 50, [50, 50], [10, 20, 30])
_44Block = Block(50, 150, [50, 50], [10, 20, 30])
_45Block = Block(100, 150, [50, 50], [10, 20, 30])
_46Block = Block(150, 150, [50, 50], [10, 20, 30])
_47Block = Block(200, 150, [50, 50], [10, 20, 30])
_48Block = Block(350, 150, [50, 50], [10, 20, 30])
_49Block = Block(400, 150, [50, 50], [10, 20, 30])
_50Block = Block(450, 150, [50, 50], [10, 20, 30])
GruppaBlockov = pygame.sprite.Group()
GruppaBlockov.add(_1Block,_2Block,_3Block,_4Block,_5Block,_6Block,_7Block,_8Block,_9Block,_10Block,_11Block,_12Block,_13Block,_14Block,_15Block,_16Block,_17Block,_18Block,_19Block,_20Block,_21Block,_22Block,_23Block,_24Block,_25Block,_26Block,_27Block,_28Block,_29Block,_30Block,_31Block,_32Block,_33Block,_34Block,_35Block,_36Block,_37Block,_38Block,_39Block,_40Block,_41Block,_42Block,_43Block,_44Block,_45Block,_46Block,_47Block,_48Block,_49Block,_50Block)
GruppaPlayerov = pygame.sprite.Group(player)
Blocking = Block(252, 134, [134, 132], [142, 213, 13])
GruppaBlockov.add(Blocking)
while running:
    window.fill((213, 132, 123))
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
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.update()
    # Здесь вы можете добавить код для обновления игры
    if pygame.sprite.spritecollide(player, [Blocking], False):
        print("соприкосновение")

    # Отображение изменений на экране
    pygame.draw.rect(window, (0, 128, 255), A)
    pygame.draw.rect(window, (0, 128, 255), B)
    # window.blit(Fs,[Fx,Fy])
    # textdisplay(20,"tylpanchikiilandishi",[142,125,164],Tx,Ty)
    player.display()
    GruppaBlockov.draw(window)
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
