from pygame import *
from pygame.sprite import *
from pygame.font import *

init()
screen = display.set_mode((1200, 700))
display.set_caption("New game window")
my_font = Font(None, 60)
FPSClock = time.Clock()
FPS = 20

class Square(Sprite):
    def __init__(self):
        self.image = Surface((100, 100))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(10, 10)
        # Rect(10, 10, 100, 100)
        
class Run(Sprite):
    def __init__(self):
        self.image = image.load(r"Lecture notes\Run-10.png").convert_alpha()
        self.rect = Rect(150, 100, 50, 100) 
        # self.image.get_rect().move(150, 100) 
        
class Banner(Sprite):
    def __init__(self):
        self.image = my_font.render("New Game Banner", True, (100, 160, 200), (30, 30, 30))
        self.rect = self.image.get_rect()
        
    def update_left(self):
        self.rect = self.rect.move(-2, 0)
    def update_right(self):
        self.rect = self.rect.move(2, 0)
    

        
s1 = Square()
s2 = Square()
s2.rect.x = 150 
r1 = Run()
b1 = Banner()

direction = True
while True:
    key_down = key.get_pressed()
    # e = event.get()
    for e in event.get():
        if e.type == QUIT:
            quit()
            break 
        elif key_down[K_LEFT]:
            b1.update_left()
        elif key_down[K_RIGHT]:
            b1.update_right()
        
    if b1.rect.right <= 1200 and direction:
        b1.update_right()
    elif b1.rect.right > 1200:
        direction = False
        b1.update_left()
    elif b1.rect.left >= 0 and not direction:
        b1.update_left()
    else:
        direction = True
        b1.update_right()
        
        
    screen.fill((255, 255, 255))
    s1.image.fill((120, 30, 200))
    s2.image.fill((128, 0, 128, 30))
    screen.blit(s2.image, s2.rect)
    screen.blit(s1.image, s1.rect)
    screen.blit(r1.image, r1.rect)
    screen.blit(b1.image, b1.rect)
    
    # line = draw.circle(screen, (0, 0, 255), (850, 350), 30, 0)
    draw.circle(screen, (0, 0, 255), (850, 350), 30, 2)
    draw.line(screen, (0, 255, 0), (850, 15), (900, 80), 0)
    # draw.polygon(screen, (100, 150, 200), ((300, 120), (560, 600), (120, 700), (900, 400), (210, 650), (600, 700)))
    
    display.update()
    FPSClock.tick(60)