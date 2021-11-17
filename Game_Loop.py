from Game_Settings import *


def title_page(display_screen):
    import time
    xx = 100
    yy = 100
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, "img")
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xx, yy)
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Space Invaders")
    myfont = pygame.font.SysFont('ArcadeClassic', 50)
    Start_Font = pygame.font.SysFont('ArcadeClassic', 15)
    titlefont = pygame.font.SysFont('ArcadeClassic', 10)
    space_invaders_logo = pygame.image.load(os.path.join(img_folder, "Space_Invaders_TitlePage.png")).convert()
    alien1 = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien1.png")).convert()
    alien2 = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien2.png")).convert()
    alien3 = pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien3.png")).convert()

    pygame.mixer.music.stop()

    on = True
    while on:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                on = False
                exit()

            elif event.type == pygame.VIDEORESIZE:
                DISPLAY_RESOLUTION.height = event.h
                DISPLAY_RESOLUTION.width = event.w
                display_screen = pygame.display.set_mode(DISPLAY_RESOLUTION.size, DISPLAY_FLAGS)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loading.play(0)
                    time.sleep(3)
                    game_loop(display_screen)

        textsurface = myfont.render(str(int(score)), False, (255, 255, 255))
        Start = Start_Font.render(str("Click Enter to Start"), False, (255, 255, 255))
        points = titlefont.render(str("=  10 points"), False, (255, 255, 255))

        game_screen.fill(black)
        game_screen.blit(space_invaders_logo, (int(width / 4), 0))
        game_screen.blit(textsurface, (10, 10))
        game_screen.blit(Start, (int(width / 3.5), 75))
        game_screen.blit(alien1, (int(width / 3), 120)) and game_screen.blit(points, (int(width / 2), 120))
        game_screen.blit(alien2, (int(width / 3), 130)) and game_screen.blit(points, (int(width / 2), 130))
        game_screen.blit(alien3, (int(width / 3), 140)) and game_screen.blit(points, (int(width / 2), 140))

        display_screen.blit(pygame.transform.scale(game_screen, DISPLAY_RESOLUTION.size), (0, 0))
        pygame.display.flip()


def game_loop(display_screen):
    import time
    import random
    from Player_Class import Player
    from Fleet_Class import Fleet
    from Fleet_Class import fleet_speed
    from Projectile_Class import Projectile
    from Mob_Class import Mob
    from Life_Class import Lives
    from Shield_Class import Shield
    player_sprite = pygame.sprite.GroupSingle()
    player = Player()
    player_sprite.add(player)

    mob_fleet = Fleet(fleet_speed, "right")

    pygame.mixer.music.play(-1)

    def make_mob1(x, y, direction):
        frames = [pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien1.png")).convert(),
                  pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien1_P2.png")).convert()]
        m = Mob(x, y, direction, fleet_speed, float(2), frames)
        return m

    def make_mob2(x, y, direction):
        frames = [pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien2.png")).convert(),
                  pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien2_P2.png")).convert()]
        m = Mob(x, y, direction, fleet_speed, float(2), frames)
        return m

    def make_mob3(x, y, direction):
        frames = [pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien3.png")).convert(),
                  pygame.image.load(os.path.join(img_folder, "Space_Invaders_Alien3_P2.png")).convert()]
        m = Mob(x, y, direction, fleet_speed, float(2), frames)
        return m

    def make_fleet():
        ####    Alien Grid    ### #
        main_xcor = 3.25
        space_between_mobs = 15
        xcor = main_xcor
        for i in range(fleet_numbers):
            row1 = make_mob1(xcor, 65, "right")
            xcor += space_between_mobs
            mob_fleet.add(row1)

        xcor = main_xcor
        for i in range(fleet_numbers):
            row2 = make_mob2(xcor, 75, "right")
            xcor += space_between_mobs
            mob_fleet.add(row2)

        xcor = main_xcor
        for i in range(fleet_numbers):
            row3 = make_mob2(xcor, 85, "right")
            xcor += space_between_mobs
            mob_fleet.add(row3)

        xcor = main_xcor
        for i in range(fleet_numbers):
            row4 = make_mob3(xcor, 95, "right")
            xcor += space_between_mobs
            mob_fleet.add(row4)

        xcor = main_xcor
        for i in range(fleet_numbers):
            row5 = make_mob3(xcor, 105, "right")
            xcor += space_between_mobs
            mob_fleet.add(row5)
        mob_fleet.set_direction("right")
        mob_fleet.set_speed(fleet_speed)

    score = 0
    num = 0
    make_Shield = Shield(25, 200)
    make_Shield.add(Shield(75, 200))
    make_Shield.add(Shield(125, 200))
    make_Shield.add(Shield(175, 200))

    counter_loops = 0
    counter = 0
    mob_bullets_counter = 0

    lives = Lives()
    lives.add_life()
    lives.add_life()
    lives.add_life()


    make_fleet()
    running = True
    self_destruct = False
    while running:
        clock.tick(fps)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                DISPLAY_RESOLUTION.height = event.h
                DISPLAY_RESOLUTION.width = event.w
                display_screen = pygame.display.set_mode(DISPLAY_RESOLUTION.size, DISPLAY_FLAGS)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(player_bullets) == 0:
                        laser_sound.play(0)
                        bullet = Projectile(player.rect.centerx, player.rect.y, -1)
                        player_bullets.add(bullet)
                elif event.key == pygame.K_k:
                    self_destruct = True

        if mob_fleet.fleet_dir == "right" and mob_fleet.get_right_side() > width:
            counter = 0
            mob_fleet.set_direction("down")
            counter_loops = float(10 * fps / fleet_speed)
            next_dir = "left"
        elif mob_fleet.fleet_dir == "left" and mob_fleet.get_left_side() < 0:
            counter = 0
            mob_fleet.set_direction("down")
            counter_loops = float(10 * fps / fleet_speed)
            next_dir = "right"
        elif mob_fleet.fleet_dir == "down":
            counter += 1
            if counter >= counter_loops:
                mob_fleet.set_direction(next_dir)

        # --------Mob Bullets------- #
        mob_bullets_counter += 1
        if mob_bullets_counter == 300:
            n = random.randrange(0, (len(mob_fleet)))
            m = mob_fleet.sprites()[n - 1]
            mob_bullets_counter = 0
            m_bullet = Projectile(m.rect.centerx, (m.rect.y + 64), 1)
            mob_bullets.add(m_bullet)
        # -------Mob Bullets-------- #

        if ships.sprite is not None:
            if ships.sprite.rect.x > (width + 200):
                ships.sprite.kill()

        if len(mob_fleet.sprites()) == 0:
            player.rect.centerx = int(width / 2)
            fleet_speed = 5
            time.sleep(2)
            make_fleet()
            lives.add_life()

        ships.clear(game_screen, background)
        player_sprite.clear(game_screen, background)
        player_bullets.clear(game_screen, background)
        mob_bullets.clear(game_screen, background)

        lives.update()
        make_Shield.update()
        mob_fleet.update()
        ships.update()
        player.update()
        player_bullets.update()
        mob_bullets.update()

        num += 1

        # Check to see if bullet hit mob
        hits = pygame.sprite.groupcollide(mob_fleet, player_bullets, True, True)
        for hit in hits:
            death_sound.play(0)
            if len(mob_fleet) != 0:
                score += 10
                fleet_speed = int(75 / len(mob_fleet) + 5)
                mob_fleet.set_speed(fleet_speed)

        hits = pygame.sprite.groupcollide(make_Shield, player_bullets, True, True)
        for hit in hits:
            break

        hits = pygame.sprite.groupcollide(make_Shield, mob_bullets, True, True)
        for hit in hits:
            break

        hits = pygame.sprite.groupcollide(make_Shield, mob_fleet, True, True)
        for hit in hits:
            title_page(display_screen)

        hits = pygame.sprite.spritecollide(player, mob_bullets, True)
        if hits or self_destruct:
            self_destruct = False
            player.rect.centerx = int(width / 2)
            ship_crash.play(0)
            time.sleep(1)
            lives.remove_life()

        hits = pygame.sprite.groupcollide(ships, player_bullets, True, True)
        for hit in hits:
            score += 50

        if lives.get_num_lives() == 0:
            title_page(display_screen)

        # Draw / Render
        game_screen.fill(black)
        line_1 = pygame.draw.line(game_screen, green, (0, height - 20), (width, height - 20))
        line_2 = pygame.draw.line(game_screen, green, (0, 20), (width, 20))
        textsurface = myfont.render(str(int(score)), False, (255, 255, 255))
        game_screen.blit(textsurface, (10, 10))

        lives.draw(game_screen)
        make_Shield.draw(game_screen)
        mob_fleet.draw(game_screen)
        player_sprite.draw(game_screen)
        player_bullets.draw(game_screen)
        mob_bullets.draw(game_screen)
        ships.draw(game_screen)

        display_screen.blit(pygame.transform.scale(game_screen, DISPLAY_RESOLUTION.size), (0, 0))
        # ALWAYS DO LAST!!!
        pygame.display.flip()
