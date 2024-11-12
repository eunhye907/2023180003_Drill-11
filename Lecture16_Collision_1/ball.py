from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, fire_ball= False):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.fire_ball = fire_ball
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x -10, self.y -10, self.x +10, self.y +10


    def handle_collision(self, group, other):
        from zombie import Zombie
        if group == 'boy:ball':
            game_world.remove_object(self)
        if group == 'zombie:ball'and isinstance(other, Zombie):
            game_world.remove_object(self)
        # fill here
