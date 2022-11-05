import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
fps = 60
size = (640, 480)

def ClearSave(m):
    file_name_save = R'Save/SaveLV.txt'
    print(f'{file_name_save} clear')

    with open(file_name_save, 'w') as file:
        file.write(f'{m}')
        file.close()

def SaveData(m):
    file_name_save = R'Save/SaveLV.txt'
    print(file_name_save)

    with open(file_name_save, 'w') as file:
        file.write(f'{m}')
        file.close()

screen = pygame.display.set_mode(size)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background(
    R'Grafics/GroundSave.png', [0, 0])

BackMenu = pygame.Rect(40, 330, 155, 50)
DeleteSave = pygame.Rect(40, 265, 155, 50)
AddSave = pygame.Rect(40, 200, 155, 50)

def GameOptions(level):

    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if BackMenu.collidepoint(mouse_pos):
                    return level

                elif DeleteSave.collidepoint(mouse_pos):
                    level = 1
                    ClearSave(level)

                elif AddSave.collidepoint(mouse_pos):
                    SaveData(level)

                else:
                    pass75

            else:
                pass

        screen.blit(BackGround.image, BackGround.rect)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit
