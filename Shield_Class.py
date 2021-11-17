from Game_Settings import *
game_screen = pygame.Surface(GAME_RESOLUTION.size)

S_I_Shield_1 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_1.png"))
S_I_Shield_2 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_2.png"))
S_I_Shield_3 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_3.png"))
S_I_Shield_4 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_4.png"))
S_I_Shield_5 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_5.png"))
S_I_Shield_6 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_6.png"))
S_I_Shield_7 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_7.png"))
S_I_Shield_8 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_8.png"))
S_I_Shield_9 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_9.png"))
S_I_Shield_10 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_10.png"))
S_I_Shield_11 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_11.png"))
S_I_Shield_12 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_12.png"))
S_I_Shield_13 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_13.png"))
S_I_Shield_14 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_14.png"))
S_I_Shield_15 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_15.png"))
S_I_Shield_16 = pygame.image.load(os.path.join(img_folder, "S_I_Shield_16.png"))


class ShieldPiece(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, 6, 4)
        self.image = image


class Shield(pygame.sprite.Group):
    def __init__(self, x, y):
        pygame.sprite.Group.__init__(self)
        self.add(ShieldPiece(x, y, S_I_Shield_1))
        self.add(ShieldPiece(x + 6, y, S_I_Shield_2))
        self.add(ShieldPiece(x + 12, y, S_I_Shield_3))
        self.add(ShieldPiece(x + 18, y, S_I_Shield_4))

        self.add(ShieldPiece(x, y + 4, S_I_Shield_5))
        self.add(ShieldPiece(x + 6, y + 4, S_I_Shield_6))
        self.add(ShieldPiece(x + 12, y + 4, S_I_Shield_7))
        self.add(ShieldPiece(x + 18, y + 4, S_I_Shield_8))

        self.add(ShieldPiece(x, y + 8, S_I_Shield_9))
        self.add(ShieldPiece(x + 6, y + 8, S_I_Shield_10))
        self.add(ShieldPiece(x + 12, y + 8, S_I_Shield_11))
        self.add(ShieldPiece(x + 18, y + 8, S_I_Shield_12))

        self.add(ShieldPiece(x, y + 12, S_I_Shield_13))
        self.add(ShieldPiece(x + 6, y + 12, S_I_Shield_14))
        self.add(ShieldPiece(x + 12, y + 12, S_I_Shield_15))
        self.add(ShieldPiece(x + 18, y + 12, S_I_Shield_16))

    def update(self):
        self.draw(game_screen)
