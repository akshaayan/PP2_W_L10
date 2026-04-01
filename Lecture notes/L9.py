from pygame import *
from pygame.sprite import *
from pygame.font import *

init()
screen = display.set_mode((1200, 700))
display.set_caption("New game window")
my_font = Font(None, 60)

class Square(Sprite):
    def __init__(self):
        self.image = Surface((100, 100))
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
        self.rect = self.image.get_rect().move(30, 650) 
        
    def update_left(self):
        self.rect = self.rect.move(-2, 0)
    def update_right(self):
        self.rect = self.rect.move(2, 0)
    

        
s1 = Square()
r1 = Run()
b1 = Banner()
while True:
    key_down = key.get_pressed()
    e = event.wait()
    if e.type == QUIT:
        quit()
        break 
    elif key_down[K_LEFT]:
        b1.update_left()
    elif key_down[K_RIGHT]:
        b1.update_right()
        
    b1.update_right()
    screen.fill((255, 255, 255))
    s1.image.fill((120, 30, 200))
    screen.blit(s1.image, s1.rect)
    screen.blit(r1.image, r1.rect)
    screen.blit(b1.image, b1.rect)
    display.update()