from Game_Settings import *


class Fleet(pygame.sprite.Group):
    def __init__(self, starting_speed, starting_direction, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.fleet_dir = ""
        self.fleet_speed = 0
        self.set_direction(starting_direction)
        self.set_speed(starting_speed)

    def set_direction(self, new_direction):
        self.fleet_dir = new_direction
        for m in self.sprites():
            m.set_direction(new_direction)

    def set_speed(self, new_speed):
        self.fleet_speed = new_speed
        for m in self.sprites():
            m.set_speed(new_speed)

    def get_right_side(self):
        right_side = -10000000000
        for m in self.sprites():
            if m.rect.x + m.rect.width > right_side:
                right_side = m.rect.x + m.rect.width
        return right_side

    def get_left_side(self):
        left_side = 10000000000
        for m in self.sprites():
            if m.rect.x < left_side:
                left_side = m.rect.x
        return left_side
