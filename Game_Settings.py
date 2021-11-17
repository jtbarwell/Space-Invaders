import os
import pygame
from pygame.rect import Rect
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE

width = 224
height = 256
fps = 120
score = 0
fleet_speed = 5
fleet_numbers = 11
Screen_size_multiplier = 3

GAME_RESOLUTION = Rect(0, 0, width, height)
DISPLAY_FLAGS = HWSURFACE | DOUBLEBUF | RESIZABLE
DISPLAY_RESOLUTION = Rect(0, 0, GAME_RESOLUTION.width * Screen_size_multiplier, GAME_RESOLUTION.height * Screen_size_multiplier)


# Define a few Useful Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

xx = 100
yy = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xx, yy)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
display_screen = pygame.display.set_mode(DISPLAY_RESOLUTION.size, DISPLAY_FLAGS)
game_screen = pygame.Surface(GAME_RESOLUTION.size)
background = pygame.Surface(GAME_RESOLUTION.size)
background.fill(black)
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('ArcadeClassic', 15)
titlefont = pygame.font.SysFont('ArcadeClassic', 10)
Game_Over_Font = pygame.font.SysFont('ArcadeClassic', 15)
MotherShip_loops = 0

next_dir = "left"
ships = pygame.sprite.GroupSingle()
player_bullets = pygame.sprite.Group()
mob_bullets = pygame.sprite.Group()
num = 0

# -----SOUNDS----- #
atmosphere_sound = pygame.mixer.music.load("Space_Atmosphere.mp3")
background_music = pygame.mixer.music.load("spaceinvaders1.mpeg")
title_screen_music = pygame.mixer.music.load("Title_Screen.mp3")
game_loading = pygame.mixer.Sound("loading.wav")
death_sound = pygame.mixer.Sound("invaderkilled.wav")
laser_sound = pygame.mixer.Sound("shoot.wav")
ship_crash = pygame.mixer.Sound("explosion.wav")

death_sound.set_volume(0.1)
laser_sound.set_volume(0.1)
ship_crash.set_volume(0.75)

