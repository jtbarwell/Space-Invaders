from Game_Settings import *

xx = 100
yy = 100
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xx, yy)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")
myfont = pygame.font.SysFont('ArcadeClassic', 50)
Start_Font = pygame.font.SysFont('ArcadeClassic', 15)
titlefont = pygame.font.SysFont('ArcadeClassic', 10)
Space_Invaders_Logo = pygame.image.load(os.path.join(img_folder, "Space_Invaders_TitlePage.png")).convert()
alien1 = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien1.png")).convert()
alien2 = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien2.png")).convert()
alien3 = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien3.png")).convert()


on = True
while on:
    keystate = pygame.key.get_pressed()
    events = pygame.event.get()
    for event in events:
        # Check for closing window
        if event.type == pygame.QUIT:
            on = False

        elif event.type == pygame.VIDEORESIZE:
            DISPLAY_RESOLUTION.height = event.h
            DISPLAY_RESOLUTION.width = event.w
            display_screen = pygame.display.set_mode(DISPLAY_RESOLUTION.size, DISPLAY_FLAGS)

    TextSurface = myfont.render(str(int(score)), False, (255, 255, 255))
    Start = Start_Font.render(str("Click Enter to Start"), False, (255, 255, 255))
    points = titlefont.render(str("=  10 points"), False, (255, 255, 255))

    game_screen.fill(black)
    game_screen.blit(Space_Invaders_Logo, (int(width / 4), 0))
    game_screen.blit(TextSurface, (10, 10))
    game_screen.blit(Start, (int(width / 3.5), 75))
    game_screen.blit(alien1, (int(width / 3), 120)) and game_screen.blit(points, (int(width / 2), 120))
    game_screen.blit(alien2, (int(width / 3), 130)) and game_screen.blit(points, (int(width / 2), 130))
    game_screen.blit(alien3, (int(width / 3), 140)) and game_screen.blit(points, (int(width / 2), 140))

    display_screen.blit(pygame.transform.scale(game_screen, DISPLAY_RESOLUTION.size), (0, 0))
    pygame.display.flip()

