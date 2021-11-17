from Game_Settings import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, starting_x, starting_y, starting_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1.5, 3))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = starting_x
        self.rect.y = starting_y
        self.speedx = 0
        self.speedy = starting_speed

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y < 20:
            self.kill()
        if self.rect.y > height - 20 - self.rect.height:
            self.kill()
