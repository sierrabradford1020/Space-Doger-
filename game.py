import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
game_on = False
title_on = True

# SET
p1_score = 0
p2_score = 0
p1_lives = 2
p2_lives = 2
gravity = 10
p1_speed = 15
p2_speed = 15
ticker = 0

# CREATING SPRITES
ground = gamebox.from_color(400, 600, "dark blue", 800, 40)
# (ALIEN SPRITE) https://www.google.com/search?q=cute+alien&tbm=isch&ved=2ahUKEwjbya7lhJ_mAhUELlkKHYbABvkQ2-cCegQIABAA&oq=cute+alien&gs_l=img.3..35i39j0j0i67l2j0j0i67l2j0j0i67l2.7545.9212..9631...0.0..0.112.168.1j1......0....1..gws-wiz-img.j4xA1vZ-9zw&ei=8T7pXZuNC4Tc5AKGgZvIDw&bih=765&biw=1022&safe=strict#imgrc=H4kvqYKDkHwj3M
player_1 = gamebox.from_image(200, 525, "cute-alien.png")
player_2 = gamebox.from_image(600, 525, "cute-alien2.png")
# (MONSTER) https://www.google.com/search?biw=1004&bih=798&tbm=isch&sa=1&ei=PK7qXcsE0IHnAr7SvaAO&q=cartoon+monster&oq=cartoon+monster&gs_l=img.3..0l10.37127.39183..39259...0.0..1.330.3230.0j16j1j1......0....1..gws-wiz-img.....0..0i67._U63sUrS5xs&ved=0ahUKEwjLkuyI46HmAhXQwFkKHT5pD-QQ4dUDCAc&uact=5#imgrc=3Obpv2DsurvuDM:
monster1 = gamebox.from_image(590, -300, 'monster.png')
monster2 = gamebox.from_image(40, -320, 'monster.png')
monster3 = gamebox.from_image(425, -90, 'monster.png')
monster4 = gamebox.from_image(100, 0, 'monster.png')
monsters = [monster1, monster2, monster3, monster4]
# (gold coin) https://free-game-assets.itch.io/free-game-coins-sprite
coin1 = gamebox.from_image(500, -215, 'Gold_1.png')
coin2 = gamebox.from_image(100, -50, 'Gold_1.png')
coin3 = gamebox.from_image(800, -300, 'Gold_1.png')
# (HEART) https://www.google.com/search?q=cartoon+heart&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiStveG46HmAhUJJt8KHZA5Dw0Q_AUoAXoECAsQAw&biw=1004&bih=798#imgrc=mwrc-M2roMQrnM:
heart1 = gamebox.from_image(650, 90, 'heart.png')
heart2 = gamebox.from_image(700, 90, 'heart.png')
heart3 = gamebox.from_image(750, 90, 'heart.png')
p1_heart = [heart1, heart2, heart3]
heart4 = gamebox.from_image(50, 90, 'heart.png')
heart5 = gamebox.from_image(100, 90, 'heart.png')
heart6 = gamebox.from_image(150, 90, 'heart.png')
p2_heart = [heart4, heart5, heart6]

# TITLE SPRITES
title_bac = gamebox.from_image(400, 300, 'title_bac.png')
background = gamebox.from_image(400, 300, 'cartoon.png')
background.scale_by(0.7)


def tick(keys):
    """

    :param keys: takes in keys pressed by user
    :return: Return a working game
    """
    global game_on, p1_score, p2_score, p1_lives, p2_lives, title_on, monsters
    score_keeper1 = gamebox.from_text(120, 50, "P1 SCORE: " + str(p1_score), 50, "white")
    score_keeper2 = gamebox.from_text(650, 50, "P2 SCORE: " + str(p2_score), 50, "white")
    if title_on:
        camera.clear('black')
        camera.draw(title_bac)
        camera.draw(gamebox.from_text(400, 100, 'Welcome to Space Dodger!', 50, "white", bold=True))
        camera.draw(gamebox.from_text(400, 150, 'Press the space bar to start', 50, "white", bold=False))
        camera.draw(gamebox.from_text(400, 200, "Get 10 coins before your opponent. Don't let the monsters get you!",
                                      35, "light green", bold=False))
        camera.draw(gamebox.from_text(400, 250, 'Use arrow keys to control player 1.', 35,
                                      "white", bold=False))
        camera.draw(gamebox.from_text(400, 300, 'Use A and D keys to control player 2.', 35,
                                      "white", bold=False))
        camera.draw(gamebox.from_text(275, 575, 'Created by Sierra Bradford (sjb9qvc) and Rebecca Chung (rc8kt)', 25,
                                      "white", bold=False))
    if pygame.K_SPACE in keys:
        game_on = True
        title_on = False

    if game_on:
        camera.clear('black')
        camera.draw(background)

        camera.draw(coin1)
        camera.draw(coin2)
        camera.draw(coin3)

        coin1.speedy = gravity
        coin1.move_speed()
        coin2.speedy = gravity
        coin2.move_speed()
        coin3.speedy = gravity
        coin3.move_speed()

        monster1.speedy = gravity
        monster1.move_speed()
        monster2.speedy = gravity
        monster2.move_speed()
        monster3.speedy = gravity
        monster3.move_speed()
        monster4.speedy = gravity
        monster4.move_speed()

        camera.draw(player_1)
        camera.draw(player_2)

        for life2 in p2_heart:
            camera.draw(life2)
        for life1 in p1_heart:
            camera.draw(life1)

        for monster in monsters:
            camera.draw(monster)
            monster.speedy += gravity
            if monster.y > 700:
                monster.y -= random.randint(600, 1500)
                monster.x = random.randint(10, 790)
#If players touch monster heart disapear
            if monster.touches(player_1):
                monster.y -= random.randint(600, 1500)
                monster.x = random.randint(10, 790)
                p2_heart.pop()
            if monster.touches(player_2):
                monster.y -= random.randint(600, 1500)
                monster.x = random.randint(10, 790)
                p1_heart.pop()


# WIN/ LOSE if you run out of life

        if not p1_heart:
            game_on = False
            camera.draw(gamebox.from_text(400, 100, 'Player 1 Wins!', 80, "white", bold=False))
            camera.draw(gamebox.from_text(400, 250, 'Exit Window to Play Again', 50, "red", bold=False))
        if not p2_heart:
            game_on = False
            camera.draw(gamebox.from_text(400, 100, 'Player 2 Wins!', 80, "white", bold=False))
            camera.draw(gamebox.from_text(400, 250, 'Exit Window to Play Again', 50, "red", bold=False))

        camera.draw(ground)
        camera.draw(score_keeper1)
        camera.draw(score_keeper2)

# Player 1 movement
    if pygame.K_RIGHT in keys:
        player_1.x += 20
    if player_1.x > 800:
        player_1.x = 800
    if pygame.K_LEFT in keys:
        player_1.x -= 20
    if player_1.x < 0:
        player_1.x = 0
# Player 2 movement
    if pygame.K_a in keys:
        player_2.x -= 20
    if player_2.x < 0:
        player_2.x = 0
    if pygame.K_d in keys:
        player_2.x += 20
    if player_2.x > 800:
        player_2.x = 800

# If player 1 touches coins
    if player_1.touches(coin1):
        p1_score += 1
        coin1.y -= 1000
        coin1.x = random.randint(10, 790)
        coin1.speedy += gravity
    if player_1.touches(coin2):
        p1_score += 1
        coin2.y -= 800
        coin2.x = random.randint(10, 790)
        coin2.speedy += gravity
    if player_1.touches(coin3):
        p1_score += 1
        coin3.y -= 600
        coin3.x = random.randint(10, 790)
        coin3.speedy += gravity

    # If player 2 touches coins
    if player_2.touches(coin1):
        p2_score += 1
        coin1.y -= 1000
        coin1.x = random.randint(10, 790)
        coin1.speedy += gravity - 2
    if player_2.touches(coin2):
        p2_score += 1
        coin2.y -= 800
        coin2.x = random.randint(10, 790)
        coin2.speedy += gravity - 2
    if player_2.touches(coin3):
        p2_score += 1
        coin3.y -= 600
        coin3.x = random.randint(10, 790)
        coin3.speedy += gravity - 2

# If nothing touches coins
    if coin1.y > 700:
        coin1.y -= random.randint(600, 1000)
        coin1.x = random.randint(10, 790)
        coin1.speedy += gravity - 2
    if coin2.y > 700:
        coin2.y -= random.randint(600, 1000)
        coin2.x = random.randint(10, 790)
        coin2.speedy += gravity - 2
    if coin3.y > 700:
        coin3.y -= random.randint(600, 1000)
        coin3.x = random.randint(10, 790)
        coin3.speedy += gravity - 2

#WIN If score = 10
    if p2_score >= 10:
        game_on = False
        camera.draw(gamebox.from_text(400, 100, 'Player 2 Wins! Score 10!', 80, "white", bold=False))
        camera.draw(gamebox.from_text(400, 250, 'Exit Window to Play Again', 50, "red", bold=False))

    if p1_score >= 10:
        game_on = False
        camera.draw(gamebox.from_text(400, 100, 'Player 1 Wins! Score 10!', 80, "white", bold=False))
        camera.draw(gamebox.from_text(400, 250, 'Exit Window to Play Again', 50, "red", bold=False))

    camera.display()


gamebox.timer_loop(30, tick)
