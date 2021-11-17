from Game_Settings import *


class Lives(pygame.sprite.Group):
    player_life_image = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Ship.png"))

    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, *sprites)

    def get_num_lives(self):
        return len(self)

    def add_life(self):
        life = pygame.sprite.Sprite()
        life.image = Lives.player_life_image
        nl = self.get_num_lives()
        x = nl * (12 + 4) + 2
        life.rect = Rect(x, height - 15, 12, 8)  # figure out the 'x' coordinate here

        self.add(life)

    def remove_life(self):
        nl = self.get_num_lives()
        if nl > 0:
            # remove the last item from the group
            self.sprites()[nl - 1].kill()