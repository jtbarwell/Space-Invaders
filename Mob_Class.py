from Game_Settings import *


class Mob(pygame.sprite.Sprite):
    def __init__(self, start_posx, start_posy, start_direction, start_speed, start_animation_speed, start_frames):
        pygame.sprite.Sprite.__init__(self)
        self.posx = start_posx
        self.posy = start_posy
        self.animation_speed = start_animation_speed
        self.frames = start_frames
        self.frame_index = 0
        self.rect = start_frames[0].get_rect()
        self.image = start_frames[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = ""
        self.speed = 0
        self.__speedx = 0
        self.__speedy = 0
        self.set_direction(start_direction)
        self.set_speed(start_speed)

    def update(self):
        self.posx += self.__speedx / float(fps)
        self.posy += self.__speedy / float(fps)
        self.frame_index += self.animation_speed / float(fps)
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.rect.x = int(self.posx)
        self.rect.y = int(self.posy)
        self.image = self.frames[int(self.frame_index)]
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def set_direction(self, new_direction):
        self.direction = new_direction
        self.__set_direction_and_speed()

    def set_speed(self, new_speed):
        self.speed = new_speed
        self.__set_direction_and_speed()

    def __set_direction_and_speed(self):
        if self.direction == "left":
            self.__speedx = -self.speed
            self.__speedy = 0
        elif self.direction == "right":
            self.__speedx = self.speed
            self.__speedy = 0
        elif self.direction == "down":
            self.__speedx = 0
            self.__speedy = self.speed
