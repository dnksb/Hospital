import pygame
import sys
import Levels as Ls

pygame.init()
clock = pygame.time.Clock()
fps = 60
size = (640, 480)

screen = pygame.display.set_mode(size)

complete_first_level = bool()
complete_second_level = bool()
complete_third_level = bool()
complete_fouth_level = bool()

class Texture(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Texture(
    R'Grafics/SelectLevelGround.png', [0, 0])
AK47 = Texture(
    R'Grafics/AK47.png', [60, 150])
M4A4 = Texture(
    R'Grafics/M4A4.png', [270, 120])
SATS = Texture(
    R'Grafics/SATS.png', [270, 260])
pistol = Texture(
    R'Grafics/pistol.png', [270, 380])
Croses = (
    Texture(R'Grafics/NoLevel.png', [245, 60]),
    Texture(R'Grafics/NoLevel.png', [245, 191]),
    Texture(R'Grafics/NoLevel.png', [245, 321]))

back_menu = pygame.Rect(43, 390, 155, 50)
level_first = pygame.Rect(43, 58, 160, 320)
level_second = pygame.Rect(248, 66, 350, 120)
level_third = pygame.Rect(248, 198, 350, 120)
level_fouth = pygame.Rect(248, 328, 350, 120)

def SelectLevel(level):

    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  

                if back_menu.collidepoint(mouse_pos):
                    return level    

                elif(level == 1):
                    
                    if level_first.collidepoint(mouse_pos):
                        complete_first_level = Ls.FirstLevel()
                        print('level 1')
                        
                        if(complete_first_level):
                            level = 2

                        else:
                            pass

                    else:
                        pass

                elif(level == 2):
                    
                    if level_first.collidepoint(mouse_pos):
                        Ls.FirstLevel()
                        print('level 1')

                    elif level_second.collidepoint(mouse_pos):
                        complete_second_level = Ls.SecondLevel()
                        print('level 2')
                    
                        if(complete_second_level):
                            level = 3

                        else:
                            pass

                    else:
                        pass
               
                elif(level == 3):
               
                    if level_first.collidepoint(mouse_pos):
                        Ls.FirstLevel()
                        print('level 1')
               
                    elif level_second.collidepoint(mouse_pos):
                        Ls.SecondLevel()
                        print('level 2')

                    elif level_third.collidepoint(mouse_pos):
                        complete_third_level = Ls.ThirdLevel()
                        print('level 3')

                        if(complete_third_level):
                            level = 4

                        else:
                            pass

                    else:
                        pass

                elif(level >= 4):

                    if level_first.collidepoint(mouse_pos):
                        Ls.FirstLevel()
                        print('level 1')

                    elif level_second.collidepoint(mouse_pos):
                        Ls.SecondLevel()
                        print('level 2')

                    elif level_third.collidepoint(mouse_pos):
                        Ls.ThirdLevel()
                        print('level 3')

                    elif level_fouth.collidepoint(mouse_pos):
                        complete_fouth_level = Ls.FouthLevel()
                        print('level 4')

                        if(complete_fouth_level):
                            level = 5

                        else:
                            pass

                    else:
                        pass

                else:
                    pass

            else:
                pass

        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(AK47.image, AK47.rect)
        screen.blit(M4A4.image, M4A4.rect)
        screen.blit(SATS.image, SATS.rect)
        screen.blit(pistol.image, pistol.rect)
        
        if(level == 1):
            screen.blit(Croses[0].image, Croses[0].rect)
            screen.blit(Croses[1].image, Croses[1].rect)
            screen.blit(Croses[2].image, Croses[2].rect)
        
        elif(level == 2):
            screen.blit(Croses[1].image, Croses[1].rect)
            screen.blit(Croses[2].image, Croses[2].rect)
        
        elif(level == 3):
            screen.blit(Croses[2].image, Croses[2].rect)

        else:
            pass
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit
