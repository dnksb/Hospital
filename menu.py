import pygame 
import sys
from option import GameOptions
from selectlevel import SelectLevel
from datafromsave import level

def SaveData(level1):
    file_name_save = (R'Save\SaveLV.txt')
    print(file_name_save)

    with open(file_name_save, 'w') as file:
        file.write(f'{level1}')
        file.close()

pygame.init()
clock = pygame.time.Clock()
fps = 60
size = (640, 480)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("HOSPITAL")

game_exit = pygame.Rect(575, 15, 50, 50)
show_options = pygame.Rect(40, 265, 155, 50)
start_game = pygame.Rect(40, 200, 155, 50)
game_exit_button = pygame.Rect(40, 330, 155, 50)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
            
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background(
    R'Grafics\Ground.png', [0, 0])

def GameMenu():
    new_level = level

    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  

                if show_options.collidepoint(mouse_pos):
                    new_level = GameOptions(new_level)

                elif game_exit.collidepoint(mouse_pos):
                    SaveData(new_level)
                    return False

                elif game_exit_button.collidepoint(mouse_pos):
                    SaveData(new_level)
                    return False

                elif start_game.collidepoint(mouse_pos):
                    new_level = SelectLevel(level)

                else:
                    pass

            else:
                pass

        screen.blit(BackGround.image, BackGround.rect)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit

GameMenu()
