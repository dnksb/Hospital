import pygame
import sys
import math
from random import randint

pygame.init()
clock = pygame.time.Clock()
fps = 60
size = (640, 480)
Person_skin = {1:R'Grafics/DoctorFL.png', 
	2:R'Grafics/DoctorSL.png', 
	3:R'Grafics/DoctorTL.png', 
	4:R'Grafics/DoctorFoL.png'}

lone = pygame.Rect(218, 95, 47, 188)
pacient = pygame.Rect(136, 100, 79, 132)
BackMenu = pygame.Rect(141, 178, 358, 124)
Shadow = pygame.Rect(0, 0, 122, 111)
show_hp = []
pacient_live = True

for x in range(1, 6, 1):
	show_hp.append(pygame.Rect(10 * (x * 2), 20, 10, 20))

screen = pygame.display.set_mode(size)
pygame.display.set_caption("HOSPITAL")

class Enemi(pygame.sprite.Sprite):

	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.live = True
		self.pacient_live = True
		self.HP = 2
		self.Step_num = 0
		self.attack = 0
		self.local = location
		self.rect.left, self.rect.top = location
		self.level = 1

	def damage(self, dam):
		self.HP -= dam
		
		if(self.HP < 0):
			self.live = False

		else:
			pass

	def UPDATE(self):
		
		if(self.live):
			self.Step_num += 1
			self.rect.left -= 1

			while(self.Step_num > 30):
				self.Step_num -= 30

			if(self.Step_num <= 15):
				self.image = pygame.image.load(
					R'Grafics/EnemiStep2.png')

			else:
				self.image = pygame.image.load(
					R'Grafics/EnemiStep1.png')

			if(lone.collidepoint(
					self.rect.left - 10, self.rect.top) or
				lone.collidepoint(
					self.rect.left - 10, self.rect.top + 122)):
		
				if(self.rect.top + 61 < 210 and self.level != 2):
					self.rect.left += 1
					self.rect.top -= 1

					while(self.Step_num > 30):
						self.Step_num -= 30
		
				else:
					self.rect.left += 1
					self.rect.top += 1

			elif(lone.collidepoint(
					self.rect.left - 30, self.rect.top) or
				lone.collidepoint(
					self.rect.left - 30, self.rect.top + 122)):
		
				if(self.rect.top + 61 < 210 and self.level != 2):
					self.rect.top -= 1
		
				else:
					self.rect.top += 1

			elif(lone.collidepoint(
					self.rect.left + 50, self.rect.top) or
				lone.collidepoint(
					self.rect.left + 50, self.rect.top + 122) or
				lone.collidepoint(
					self.rect.left + 30, self.rect.top) or
				lone.collidepoint(
					self.rect.left + 30, self.rect.top + 122) or
				lone.collidepoint(
					self.rect.left + 70, self.rect.top) or
				lone.collidepoint(
					self.rect.left + 70, self.rect.top + 122)):
		
				if(self.rect.top + 61 < 210 and self.level != 2):
					self.rect.top -= 1
					self.rect.left += 1
		
				else:
					self.rect.top += 1
					self.rect.left += 1

			elif(Shadow.collidepoint(
					self.rect.left + 50, self.rect.top + 70) or 
				Shadow.collidepoint(
					self.rect.left + 50, self.rect.top + 80)):
				self.rect.left += 1
				self.attack += 1

				while(self.attack > 60):
					self.attack -= 60

				if(self.attack <= 10):
					self.image = pygame.image.load(
						R'Grafics/EnemiAttack1.png')
		
				elif(self.attack <= 20):
					self.image = pygame.image.load(
						R'Grafics/EnemiAttack2.png')
		
				elif(self.attack <= 30):
					self.image = pygame.image.load(
						R'Grafics/EnemiAttack3.png')

				else:
					self.image = pygame.image.load(
						R'Grafics/EnemiAttack4.png')

			elif((self.rect.left - pacient.left) == 
				abs(pacient.top - self.rect.top)):
				
				if(pacient.top > self.rect.top):
					self.rect.top += 1
				
				else:
					self.rect.top -= 1

			elif((self.rect.left - pacient.left) == 
				abs(pacient.top - self.rect.top) / 2):
				
				if(pacient.top > self.rect.top):
					self.rect.top += 2
				
				else:
					self.rect.top -= 2

			elif((self.rect.left - pacient.left) == -25):
				
				if(pacient.top > self.rect.top):
					self.rect.top += 1
					self.rect.left += 1
				
				else:
					self.rect.top -= 1
					self.rect.left += 1

			else:
				pass
		
		else:
			self.Step_num += 1

			if(self.Step_num <= 10):
				self.image = pygame.image.load(
					R'Grafics/EnemiDie1.png')
		
			elif(self.Step_num <= 20):
				self.image = pygame.image.load(
					R'Grafics/EnemiDie2.png')
		
			elif(self.Step_num <= 30):
				self.image = pygame.image.load(
					R'Grafics/EnemiDie3.png')

			else:
				pass
		
class Bullet(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.hot = False
		self.local = location
		self.rect.left, self.rect.top = location

	def LOCATION(self, location):
		self.rect.left, self.rect.top = location
		self.rect.left += 115
		self.rect.top += 67

	def UPDATE(self):

		if(self.hot):
			self.rect.left += 15

			if(self.rect.left > 640 or 
				lone.collidepoint(
					self.rect.left + 8, self.rect.top + 3)):
				self.rect.left, self.rect.top = self.local
				self.hot = False

			else:
				pass

		else:
			pass

class DrobBullet(pygame.sprite.Sprite):
	def __init__(self, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(
			R'Grafics/DrobBullet1.png')
		self.cadr_image = {
			1:R'Grafics/DrobBullet1.png',
			2:R'Grafics/DrobBullet2.png',
			3:R'Grafics/DrobBullet3.png',
			4:R'Grafics/DrobBullet4.png',
			5:R'Grafics/DrobBullet5.png',
			6:R'Grafics/DrobBullet6.png'}
		self.rect = self.image.get_rect()
		self.hot = False
		self.local = location
		self.rect.left, self.rect.top = location
		self.num_Step = 0
		self.start_left = 0

	def LOCATION(self, location_left, location_top):
		self.rect.left, self.rect.top = location_left, location_top
		self.start_left += 115
		self.rect.left += 115
		self.rect.top += 39
		self.num_Step = 0

	def UPDATE(self):

		if(self.hot):
			self.rect.left += 15
			self.num_Step += 1

			if(self.num_Step <= 2):
				self.image = pygame.image.load(self.cadr_image[1])

			elif(self.num_Step <= 4):
				self.image = pygame.image.load(self.cadr_image[2])

			elif(self.num_Step <= 6):
				self.image = pygame.image.load(self.cadr_image[3])

			elif(self.num_Step <= 8):
				self.image = pygame.image.load(self.cadr_image[4])

			elif(self.num_Step <= 10):
				self.image = pygame.image.load(self.cadr_image[5])

			elif(self.num_Step <= 12):
				self.image = pygame.image.load(self.cadr_image[6])

			else:
				pass

			if(self.num_Step > 12 or 
				lone.collidepoint(
					self.rect.left + 8, self.rect.top + 3)):
				self.rect.left, self.rect.top = self.local
				self.hot = False

			else:
				pass

		else:
			pass

class Texture(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.Step = False
		self.Step_num = int(0)
		self.rect.left, self.rect.top = location

	def UPDATE(self, location):
		self.rect.left, self.rect.top = location

		if(self.Step):
			self.Step_num += 1

			while(self.Step_num > 30):
				self.Step_num -= 30

			if(self.Step_num <= 15):
				self.image = pygame.image.load(
					R'Grafics/Step2.png')

			else:
				self.image = pygame.image.load(
					R'Grafics/Step3.png')

		else:
			pass

class Person(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.moving_left = bool(False)
		self.moving_right = bool(False)
		self.moving_up = bool(False)
		self.moving_down = bool(False)
		self.live = bool(True)
		self.HP = 5
		self.rect.left, self.rect.top = location

	def damage(self):
		self.HP -= 1

	def UPDATE(self): 
		
		if(self.live):
			
			if(self.moving_right):

				if(self.rect.left + 4 <= 533 and 
					lone.collidepoint(
						self.rect.left + 70, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left + 90, self.rect.top + 100) == False and
					lone.collidepoint(
						self.rect.left + 133, self.rect.top + 70) == False and
					pacient.collidepoint(
						self.rect.left + 70, self.rect.top + 25) == False and
					pacient.collidepoint(
						self.rect.left + 90, self.rect.top + 100) == False and
					pacient.collidepoint(
						self.rect.left + 133, self.rect.top + 70) == False):
					self.rect.left += 4

				else:
					pass

			else:
				pass

			if(self.moving_left):
				
				if(self.rect.left - 4 >= -13 and
					lone.collidepoint(
						self.rect.left, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left, self.rect.top + 100) == False and
					pacient.collidepoint(
						self.rect.left, self.rect.top + 25) == False and
					pacient.collidepoint(
						self.rect.left, self.rect.top + 100) == False):
					self.rect.left -= 4

				else:
					pass

			else:
				pass
		
			if(self.moving_up):
				
				if(self.rect.top - 4 >= -20 and
					lone.collidepoint(
						self.rect.left + 129, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left + 100, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left + 70, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left + 75, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left + 10, self.rect.top + 25) == False and
					lone.collidepoint(
						self.rect.left + 40, self.rect.top + 25) == False and
					pacient.collidepoint(
						self.rect.left + 129, self.rect.top + 50) == False and
					pacient.collidepoint(
						self.rect.left + 100, self.rect.top + 50) == False and
					pacient.collidepoint(
						self.rect.left + 70, self.rect.top + 50) == False and
					pacient.collidepoint(
						self.rect.left + 75, self.rect.top + 50) == False and
					pacient.collidepoint(
						self.rect.left + 10, self.rect.top + 50) == False and
					pacient.collidepoint(
						self.rect.left + 40, self.rect.top + 50) == False):
					self.rect.top -= 4

				else:
					pass

			else:
				pass
		
			if(self.moving_down):
			
				if(self.rect.top + 4 <= 377 and 
					lone.collidepoint(
						self.rect.left + 5, self.rect.top + 114) == False and
					lone.collidepoint(
						self.rect.left + 41, self.rect.top + 122) == False and
					lone.collidepoint(
						self.rect.left + 80, self.rect.top + 122) == False and
					lone.collidepoint(
						self.rect.left + 90, self.rect.top + 122) == False and
					lone.collidepoint(
						self.rect.left + 100, self.rect.top + 78) == False and
					lone.collidepoint(
						self.rect.left + 129, self.rect.top + 78) == False and
					pacient.collidepoint(
						self.rect.left + 5, self.rect.top + 114) == False and
					pacient.collidepoint(
						self.rect.left + 41, self.rect.top + 122) == False and
					pacient.collidepoint(
						self.rect.left + 80, self.rect.top + 122) == False and
					pacient.collidepoint(
						self.rect.left + 90, self.rect.top + 122) == False and
					pacient.collidepoint(
						self.rect.left + 100, self.rect.top + 78) == False and
					pacient.collidepoint(
						self.rect.left + 129, self.rect.top + 78) == False):
					self.rect.top += 4

				else:
					pass

			else:
				pass

			if(self.HP <= 0):
				self.live = False

			elif(pacient_live == False):
				self.live = False

			else:
				pass

		else:
			END = Texture(
				R'Grafics/YES.png', [self.rect.left - 70, self.rect.top - 60])
			screen.blit(END.image, END.rect)
			self.image = pygame.image.load(R'Grafics/DoctorDead.png')

def FirstLevel():

	pacient_live = True

	Step = int(0)
	num = int(0)
	live_enems = int(8)

	lone.left, lone.top = 218, 95
	pacient.left, pacient.top = 136, 100
	LOSE = Texture(
		R'Grafics/LoseMenu.png', [0, 0])
	WIN = Texture(
		R'Grafics/WinMenu.png', [0, 0])
	Style = Texture(
		R'Grafics/Style.png', [0, 0])	
	END = Texture(
		R'Grafics/END.png', [0, 0])
	BackGround = Texture(
		R'Grafics/flatFL.jpg', [0, 0])
	character = Person(
		Person_skin[1], [30, 185])
	leg = Texture(
		R'Grafics/Step1.png', 
		[character.rect.left, character.rect.top])

	Bullets = []
	Enemis = []

	for i in range(0, 8, 1):
		Enemis.append(Enemi(
			R'Grafics/EnemiStep1.png', 
			[800 + (i * randint(40, 150)), randint(10, 370)]))

	for i in range(0, 4, 1):
		Bullets.append(Bullet(
			R'Grafics/Bullet.png', 
			[character.rect.left, character.rect.top]))

	while True:

		ind = False

		for event in pygame.event.get():

			if (event.type == pygame.QUIT):
				return False

			elif (event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos

				if (character.live == False):

					if (BackMenu.collidepoint(mouse_pos)):
						return False

					else:
						pass

				elif (live_enems <= 0):

					if (BackMenu.collidepoint(mouse_pos)):
						return True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYDOWN):

				if(character.live and pacient_live):

					if (event.key == pygame.K_LEFT):
						leg.Step = True
						character.moving_left = True

					elif (event.key == pygame.K_RIGHT):
						leg.Step = True
						character.moving_right = True

					else:
						pass

					if (event.key == pygame.K_UP):
						leg.Step = True
						character.moving_up = True

					elif (event.key == pygame.K_DOWN):
						leg.Step = True
						character.moving_down = True

					else:
						pass

					if (event.key == pygame.K_c):
					
						for bullet in Bullets:
							bullet.LOCATION(
								[character.rect.left, character.rect.top])
							bullet.hot = True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYUP):

				if (event.key == pygame.K_LEFT):
					character.moving_left = False

				elif (event.key == pygame.K_RIGHT):
					character.moving_right = False

				else:
					pass

				if (event.key == pygame.K_UP):
					character.moving_up = False

				elif (event.key == pygame.K_DOWN):
					character.moving_down = False
				leg.Step = False
				leg.image = pygame.image.load(
					R'Grafics/Step1.png')

			else:
				pass

		screen.blit(BackGround.image, BackGround.rect)
		
		for bullet in Bullets:

			if(bullet.hot):
				screen.blit(bullet.image, bullet.rect)

			else:
				pass
		
		for enem in Enemis:
			screen.blit(enem.image, enem.rect)
		
		screen.blit(character.image, character.rect)

		screen.blit(leg.image, leg.rect)

		if(character.live == False and pacient_live == False):
			END.rect.left, END.rect.top = character.rect.left - 70, character.rect.top - 60 
			screen.blit(END.image, END.rect)

		else:
			pass

		screen.blit(Style.image, Style.rect)

		for i in range(0, character.HP, 1):
			pygame.draw.rect(screen, [255, 0, 0], show_hp[i])

		if(character.live and pacient_live):

			live_enems = 8

			for enem in Enemis:
				enem.level = 1
				enem.UPDATE()
				
				if(pacient.collidepoint(
					enem.rect.left + 50, enem.rect.top + 10) or
					pacient.collidepoint(
						enem.rect.left + 50, enem.rect.top + 122)):
		
					character.damage()
					
					if(pacient.top > enem.rect.top):
						enem.rect.left += 1
						enem.rect.top -=1

					else:
						enem.rect.left += 1
						enem.rect.top += 1

				elif((Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 70) or 
					Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 80)) and
					enem.live):
						
					if(enem.attack == 25):
						character.damage()

					else:
						pass

				elif(enem.rect.left < 0):
					return False

				elif(enem.live == False):
					live_enems -= 1

				else:
					pass

				for bullet in Bullets:
		
					if(enem.live and
						enem.rect.collidepoint(
							bullet.rect.left + 8, bullet.rect.top + 3) and
						bullet.hot == True):
						enem.damage(2)
						bullet.hot = False

					else:
						pass

			character.UPDATE()
			leg.UPDATE([character.rect.left, character.rect.top])
		
			Shadow.left, Shadow.top = character.rect.left, character.rect.top

			for bullet in Bullets:
				bullet.UPDATE()

			num += 1
		
			if(num % 60 == 0 or (num - 1) % 60 == 0):
				character.image = pygame.image.load(R'Grafics/DoctorFLMG.png')
		
			else:
				character.image = pygame.image.load(R'Grafics/DoctorFL.png')

			if(live_enems <= 0):
				screen.blit(WIN.image, WIN.rect)

			else:
				pass

		else:
			character.image = pygame.image.load(R'Grafics/DoctorDead.png')
			screen.blit(LOSE.image, LOSE.rect)

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	sys.exit

def SecondLevel():
	live_enems = 8

	Step = int(0)
	num = int(0)

	lone.left, lone.top = 223, 7
	pacient.left, pacient.top = 136, 12 
	LOSE = Texture(
		R'Grafics/LoseMenu.png', [0, 0])
	WIN = Texture(
		R'Grafics/WinMenu.png', [0, 0])
	YES = Texture(
		R'Grafics/YES.png', [0, 0])
	END = Texture(
		R'Grafics/END.png', [0, 0])
	Style = Texture(
		R'Grafics/Style.png', [0, 0])	
	BackGround = Texture(
		R'Grafics/flatSL.jpg', [0, 0])
	character = Person(
		Person_skin[2], [30, 185])
	leg = Texture(
		R'Grafics/Step1.png', 
		[character.rect.left, character.rect.top])

	Bullets = []
	Enemis = []

	for i in range(0, 8, 1):
		Enemis.append(Enemi(
			R'Grafics/EnemiStep1.png', 
			[800 + (i * randint(40, 150)), randint(10, 370)]))

	for i in range(0, 4, 1):
		Bullets.append(Bullet(
			R'Grafics/Bullet.png', 
			[character.rect.left, character.rect.top]))

	while True:

		ind = False

		for event in pygame.event.get():

			if (event.type == pygame.QUIT):
				return False

			elif (event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos

				if(character.live == False):

					if (BackMenu.collidepoint(mouse_pos)):
						return False

					else:
						pass

				elif (live_enems <= 0):

					if (BackMenu.collidepoint(mouse_pos)):
						return True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYDOWN):

				if(character.live):

					if (event.key == pygame.K_LEFT):
						leg.Step = True
						character.moving_left = True

					elif (event.key == pygame.K_RIGHT):
						leg.Step = True
						character.moving_right = True

					if (event.key == pygame.K_UP):
						leg.Step = True
						character.moving_up = True

					elif (event.key == pygame.K_DOWN):
						leg.Step = True
						character.moving_down = True

					if (event.key == pygame.K_c):
					
						for bullet in Bullets:
							bullet.LOCATION(
								[character.rect.left, 
								character.rect.top])
							bullet.hot = True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYUP):

				if (event.key == pygame.K_LEFT):
					character.moving_left = False

				elif (event.key == pygame.K_RIGHT):
					character.moving_right = False

				else:
					pass

				if (event.key == pygame.K_UP):
					character.moving_up = False

				elif (event.key == pygame.K_DOWN):
					character.moving_down = False
				leg.Step = False
				leg.image = pygame.image.load(
					R'Grafics/Step1.png')

			else:
				pass

		screen.blit(BackGround.image, BackGround.rect)
		
		if(num < 2400 and num > 2000):
			YES.rect.left, YES.rect.top = character.rect.left - 70, character.rect.top - 60
			screen.blit(YES.image, YES.rect)

		else:
			pass

		for bullet in Bullets:

			if(bullet.hot):
				screen.blit(bullet.image, bullet.rect)
		
		for enem in Enemis:
			screen.blit(enem.image, enem.rect)

		screen.blit(character.image, character.rect)
		screen.blit(leg.image, leg.rect)

		if(character.live == False):
			END.rect.left, END.rect.top = character.rect.left - 70, character.rect.top - 60 
			screen.blit(END.image, END.rect)

		else:
			pass
		
		screen.blit(Style.image, Style.rect)

		for i in range(0, character.HP, 1):
			pygame.draw.rect(screen, [255, 0, 0], show_hp[i])
		
		if(character.live):
			live_enems = 8

			character.UPDATE()
			leg.UPDATE([character.rect.left, character.rect.top])
			Shadow.left, Shadow.top = character.rect.left, character.rect.top

			for enem in Enemis:
				enem.level = 2
				enem.UPDATE()
				
				if(pacient.collidepoint(
					enem.rect.left + 50, enem.rect.top + 10) or
					pacient.collidepoint(
						enem.rect.left + 50, enem.rect.top + 122)):
		
					character.damage()
					
					if(pacient.top > enem.rect.top):
						enem.rect.left += 1
						enem.rect.top -=1

					else:
						enem.rect.left += 1
						enem.rect.top += 1

				elif((Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 70) or 
					Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 80)) and
					enem.live):
					if(enem.attack == 25):
						character.damage()

					else:
						pass

				elif(enem.live == False):
					live_enems -= 1

				else:
					pass

				for bullet in Bullets:
		
					if(enem.live and
						enem.rect.collidepoint(
							bullet.rect.left + 8, bullet.rect.top + 3) and
						bullet.hot == True):
						enem.damage(1)
						bullet.hot = False

					else:
						pass

				if(enem.rect.left < 0):
					return False

				else:
					pass

			for bullet in Bullets:
				bullet.UPDATE()

			num += 1
		
			if(num % 60 == 0 or (num - 1) % 60 == 0):
				character.image = pygame.image.load(R'Grafics/DoctorSLMG.png')
		
			else:
				character.image = pygame.image.load(R'Grafics/DoctorSL.png')

			if(live_enems <= 0):
				screen.blit(WIN.image, WIN.rect)

			else:
				pass

		else:
			character.image = pygame.image.load(R'Grafics/DoctorDead.png')
			screen.blit(LOSE.image, LOSE.rect)

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	sys.exit

def ThirdLevel():
	live_enems = 8

	Step = int(0)
	num = int(0)
	LOSE = Texture(
		R'Grafics/LoseMenu.png', [0, 0])
	lone.left, lone.top = 402, 134
	pacient.left, pacient.top = 317, 162 
	Style = Texture(
		R'Grafics/Style.png', [0, 0])
	WIN = Texture(
		R'Grafics/WinMenu.png', [0, 0])
	END = Texture(
		R'Grafics/END.png', [0, 0])
	BackGround = Texture(
		R'Grafics/flatTL.jpg', [0, 0])
	character = Person(
		Person_skin[3], [30, 185])
	leg = Texture(
		R'Grafics/Step1.png', 
		[character.rect.left, character.rect.top])
	Bullet = DrobBullet([0, 0])

	Enemis = []

	for i in range(0, 8, 1):
		Enemis.append(Enemi(
			R'Grafics/EnemiStep1.png', 
			[800 + (i * randint(40, 150)), 
				randint(10, 370)]))

	while True:

		ind = False

		for event in pygame.event.get():

			if (event.type == pygame.QUIT):
				return False

			elif (event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos

				if(character.live == False):

					if (BackMenu.collidepoint(mouse_pos)):
						return True

					else:
						pass

				elif (live_enems <= 0):

					if (BackMenu.collidepoint(mouse_pos)):
						return True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYDOWN):

				if(character.live):

					if (event.key == pygame.K_LEFT):
						leg.Step = True
						character.moving_left = True

					elif (event.key == pygame.K_RIGHT):
						leg.Step = True
						character.moving_right = True

					else:
						pass

					if (event.key == pygame.K_UP):
						leg.Step = True
						character.moving_up = True

					elif (event.key == pygame.K_DOWN):
						leg.Step = True
						character.moving_down = True

					else:
						pass

					if (event.key == pygame.K_c):
					
						Bullet.LOCATION(character.rect.left, 
							character.rect.top)
						Bullet.hot = True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYUP):

				if (event.key == pygame.K_LEFT):
					character.moving_left = False

				elif (event.key == pygame.K_RIGHT):
					character.moving_right = False

				else:
					pass

				if (event.key == pygame.K_UP):
					character.moving_up = False

				elif (event.key == pygame.K_DOWN):
					character.moving_down = False
				leg.Step = False
				leg.image = pygame.image.load(
					R'Grafics/Step1.png')

			else:
				pass

		screen.blit(BackGround.image, BackGround.rect)
		screen.blit(leg.image, leg.rect)
		
		if(Bullet.hot):
			screen.blit(Bullet.image, Bullet.rect)

		else:
			pass
		
		for enem in Enemis:
			screen.blit(enem.image, enem.rect)
		
		screen.blit(character.image, character.rect)
		
		if(character.live == False):
			END.rect.left, END.rect.top = character.rect.left - 70, character.rect.top - 60 
			screen.blit(END.image, END.rect)

		else:
			pass

		screen.blit(Style.image, Style.rect)

		for i in range(0, character.HP, 1):
			pygame.draw.rect(screen, [255, 0, 0], show_hp[i])

		if(character.live):
			live_enems = 8

			character.UPDATE()
			leg.UPDATE([character.rect.left - 10, character.rect.top])
		
			Shadow.left, Shadow.top = character.rect.left, character.rect.top

			Bullet.UPDATE()

			for enem in Enemis:
				enem.level = 3
				enem.UPDATE()

				if(pacient.collidepoint(
					enem.rect.left + 50, enem.rect.top + 10) or
					pacient.collidepoint(
						enem.rect.left + 50, enem.rect.top + 122)):
		
					character.damage()
					
					if(pacient.top > enem.rect.top):
						enem.rect.left += 1
						enem.rect.top -=1

					else:
						enem.rect.left += 1
						enem.rect.top += 1

				elif((Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 70) or 
					Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 80)) and
					enem.live):
					if(enem.attack == 25):
						character.damage()

					else:
						pass

				elif(enem.live and
					Bullet.hot == True):
				
					if(enem.rect.collidepoint(
							Bullet.rect.left + 8, Bullet.rect.top) or
						enem.rect.collidepoint(
							Bullet.rect.left + 8, Bullet.rect.top + 30) or
						enem.rect.collidepoint(
							Bullet.rect.left + 8, Bullet.rect.top + 60)):
						enem.damage(4)
						Bullet.hot = False

					else:
						pass

				elif(enem.rect.left < 0):
					return False

				elif(enem.live == False):
					live_enems -= 1

				else:
					pass

			num += 1
		
			if(num % 60 == 0 or (num - 1) % 60 == 0):
				character.image = pygame.image.load(R'Grafics/DoctorTLMG.png')
		
			else:
				character.image = pygame.image.load(R'Grafics/DoctorTL.png')

			if(live_enems <= 0):
				screen.blit(WIN.image, WIN.rect)

			else:
				pass

		else:
			character.image = pygame.image.load(R'Grafics/DoctorDead.png')
			screen.blit(LOSE.image,LOSE.rect)

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	sys.exit

def FouthLevel():
	live_enems = 8

	Step = int(0)
	num = int(0)
	LOSE = Texture(
		R'Grafics/LoseMenu.png', [0, 0])
	lone.left, lone.top = -50, 500
	pacient.left, pacient.top = 136, 100
	Style = Texture(
		R'Grafics/Style.png', [0, 0])
	WIN = Texture(
		R'Grafics/WinMenu.png', [0, 0])
	END = Texture(
		R'Grafics/END.png', [0, 0])	
	BackGround = Texture(
		R'Grafics/flatFoL.jpg', [0, 0])
	character = Person(
		Person_skin[1], [30, 185])
	leg = Texture(
		R'Grafics/Step1.png', 
		[character.rect.left, character.rect.top])
	Bulllet = Bullet(
			R'Grafics/Bullet.png', [0, 0])
	
	Enemis = []

	for i in range(0, 8, 1):
		Enemis.append(Enemi(
			R'Grafics/EnemiStep1.png', 
			[800 + (i * randint(40, 150)), randint(10, 370)]))

	while True:

		ind = False

		for event in pygame.event.get():

			if (event.type == pygame.QUIT):
				return False

			elif (event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos

				if(character.live == False):

					if (BackMenu.collidepoint(mouse_pos)):
						return True

					else:
						pass

				elif (live_enems <= 0):

					if (BackMenu.collidepoint(mouse_pos)):
						return True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYDOWN):

				if(character.live):

					if (event.key == pygame.K_LEFT):
						leg.Step = True
						character.moving_left = True

					elif (event.key == pygame.K_RIGHT):
						leg.Step = True
						character.moving_right = True

					else:
						pass

					if (event.key == pygame.K_UP):
						leg.Step = True
						character.moving_up = True

					elif (event.key == pygame.K_DOWN):
						leg.Step = True
						character.moving_down = True

					else:
						pass

					if (event.key == pygame.K_c):
					
						Bulllet.LOCATION(
							[character.rect.left, character.rect.top])
						Bulllet.hot = True

					else:
						pass

				else:
					pass

			elif (event.type == pygame.KEYUP):

				if (event.key == pygame.K_LEFT):
					character.moving_left = False

				elif (event.key == pygame.K_RIGHT):
					character.moving_right = False

				else:
					pass

				if (event.key == pygame.K_UP):
					character.moving_up = False

				elif (event.key == pygame.K_DOWN):
					character.moving_down = False
				leg.Step = False
				leg.image = pygame.image.load(
					R'Grafics/Step1.png')

			else:
				pass

		screen.blit(BackGround.image, BackGround.rect)
		screen.blit(leg.image, leg.rect)

		if(Bulllet.hot):
			screen.blit(Bulllet.image, Bulllet.rect)
		
		else:
			pass
		
		for enem in Enemis:
			screen.blit(enem.image, enem.rect)
		
		screen.blit(character.image, character.rect)

		if(character.live == False):
			END.rect.left, END.rect.top = character.rect.left - 70, character.rect.top - 60 
			screen.blit(END.image, END.rect)

		screen.blit(Style.image, Style.rect)

		for i in range(0, character.HP, 1):
			pygame.draw.rect(screen, [255, 0, 0], show_hp[i])

		if(character.live):
			live_enems = 8

			character.UPDATE()
			leg.UPDATE([character.rect.left - 10, character.rect.top])
			Shadow.left, Shadow.top = character.rect.left, character.rect.top
			Bulllet.UPDATE()

			for enem in Enemis:
				enem.level = 4
				enem.UPDATE()
				
				if(pacient.collidepoint(
					enem.rect.left + 50, enem.rect.top + 10) or
					pacient.collidepoint(
						enem.rect.left + 50, enem.rect.top + 122)):
		
					character.damage()
					
					if(pacient.top > enem.rect.top):
						enem.rect.left += 1
						enem.rect.top -=1

					else:
						enem.rect.left += 1
						enem.rect.top += 1

				elif(enem.live and
					enem.rect.collidepoint(
						Bulllet.rect.left + 8, Bulllet.rect.top + 3) and
					Bulllet.hot == True):
					enem.damage(1)
					Bulllet.hot = False

				elif(enem.rect.left < 0):
					return False

				elif((Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 70) or 
					Shadow.collidepoint(
						enem.rect.left + 20, enem.rect.top + 80)) and
					enem.live):
					
					if(enem.attack == 25):
						character.damage()

					else:
						pass

				elif(enem.live == False):
					live_enems -= 1

				else:
					pass

			num += 1
		
			if(num % 60 == 0 or (num - 1) % 60 == 0):
				character.image = pygame.image.load(R'Grafics/DoctorFoLMG.png')
		
			else:
				character.image = pygame.image.load(R'Grafics/DoctorFoL.png')

			if(live_enems <= 0):
				screen.blit(WIN.image, WIN.rect)

			else:
				pass

		else:
			character.image = pygame.image.load(R'Grafics/DoctorDead.png')
			screen.blit(LOSE.image, LOSE.rect)

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	sys.exit
