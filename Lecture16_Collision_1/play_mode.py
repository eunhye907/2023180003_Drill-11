import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global zombie
    global balls

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    zombie = Zombie()
    game_world.add_object(zombie, 1)

    balls = [Ball(random.randint(100, 1600-100), 60, 0)for _ in range(30)]
    for ball in balls:
        game_world.add_object(ball,1)

    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
        game_world.add_collision_pair('zombie:ball', zombie, None)
    # fill here
    game_world.add_collision_pair('boy:zombie', boy, zombie)


def finish():
    game_world.clear()



def update():
    game_world.update()
    game_world.handle_collisions()
    for ball in balls:
        if game_world.collide(boy, ball):
            print('COLLISION boy:ball')
            boy.ball_count += 1
            game_world.remove_object(ball)
            balls.remove(ball)

        if game_world.collide(zombie,ball):
            print('COLLISION zombie:ball')
            zombie.ball_count += 1
            game_world.reduce_objects(zombie)

        if game_world.collide(zombie, boy):
            print('COLLISION boy:zombie')
            game_framework.quit()




def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

