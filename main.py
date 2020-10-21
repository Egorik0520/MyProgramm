import pygame
import random

num = random.randint(0, 100)
print(num)
W = 480
H = 360
SILVER =(192,192,192)
BLACK = (0,0,0)
numeral = ''
move = 1
block = 0
start = 1 
OUTSIDE_BG = (0, -100)


pygame.init()
pygame.display.set_caption('угадай число')  #название окна
screen = pygame.display.set_mode((W,H)) #создает окно
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 28, True, False)
font2 = pygame.font.SysFont('Arial', 14, False, True)
font_box = pygame.Surface((W - 20,font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))

bg = pygame.image.load('Image/room.png') #изображение
bg_rect = bg.get_rect(topleft=(0,0))

cat = pygame.image.load('Image/cat.png')  #изображение
cat_rect = cat.get_rect(center=(70, 220))

dog = pygame.image.load('Image/dog.png')#изображение
dog_rect = dog.get_rect(center=(410,220))

owl = pygame.image.load('Image/owl.png')#изображение
owl_rect = owl.get_rect(center=(210,120))

dialog = pygame.image.load('Image/dialog.png')#изображение
dialog_rect = dialog.get_rect() 
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)
dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)

def dialogs(text,pos, owl_text):
    screen.blit(dialog,pos)
    screen.blit(font2.render(text,True,BLACK), (pos[0]+5, pos[1] +5))
    screen.blit(dialog, dialog_owl_pos)
    screen.blit(font2.render(
        owl_text,True,BLACK), (dialog_owl_pos[0]+5, dialog_owl_pos[1] +5))
    pygame.display.update()
    pygame.time.wait(1000)


run = True 
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            elif e.unicode.isdecimal() and block == 0:
                numeral += e.unicode  
            elif e.key == pygame.K_BACKSPACE:
                numeral = numeral[:-1]
            elif e.key == pygame.K_RETURN and numeral:
                if int(numeral) > 100:
                    dialogs('',OUTSIDE_BG, 'ВЫ ОШИБЛИСЬ')
                elif int(numeral) > num:
                    dialogs('',OUTSIDE_BG, 'число меньше')
                elif int(numeral) < num:
                    dialogs('',OUTSIDE_BG, 'ЧИСЛО БОЛЬШЕ')

                if move == 1:
                    if int(numeral) == num:
                        dialogs('Да',dialog_cat_pos, 'кот, ты победил')
                        block = 1
                    else:
                       dialog('пес, твой ход',dialog_dog_pos,'продолжаем')
                    
                if move == 2:
                    if int(numeral) == num:
                        dialogs('Да',dialog_dog_pos, 'пес, ты победил')
                        block = 1
                    else:
                        dialog('кот, твой ход',dialog_cat_pos,'продолжаем')
                numeral = ''
                move += 1
                if move > 2:
                    move = 1 


                
                    

    if block == 0:
        screen.blit(bg, bg_rect)
        screen.blit(cat, cat_rect)
        screen.blit(dog, dog_rect)
        screen.blit(owl, owl_rect)
        screen.blit(dialog, dialog_rect)
        screen.blit(font_box, font_rect)
        font_box.fill(SILVER)
        font_box.blit(font.render(numeral, True, BLACK), (10,0))
        pygame.display.update()

        if start == 1:
            dialogs('', OUTSIDE_BG, 'я загадала число')
            dialogs('', OUTSIDE_BG, 'от 0 до 100')
            dialogs('кот, твой ход',dialog_dog_pos , 'отгадайте его')   
            start = 0 



            
