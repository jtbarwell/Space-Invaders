from Game_Settings import *
from Player_Class import Player
from Fleet_Class import Fleet
from Game_Loop import title_page

player_sprite = pygame.sprite.GroupSingle()
player = Player()
player_sprite.add(player)

mob_fleet = Fleet(fleet_speed, "right")

pygame.init()

title_page(display_screen)

pygame.quit()
