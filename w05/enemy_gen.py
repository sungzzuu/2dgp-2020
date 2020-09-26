import random
import gfw
import gfw_world
from pico2d import *
from enemy import Enemy

GEN_X = [ 50, 150, 250, 350, 450 ]
next_wave = 0
wave_index = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time * 10
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave
    levels = []
    for x in GEN_X:
        e = Enemy(x, -1)
        gfw_world.add(gfw.layer.enemy, e)
        levels.append(enemy_level())

    print(wave_index, levels)
    wave_index += 1
    next_wave = random.uniform(5, 6)

LEVEL_ADJUST_PERCENTS = [ 10, 15, 15, 40, 15, 5 ] # -3 ~ 2
def enemy_level():
    level = (wave_index - 10) // 10 - 3;
    percent = random.randrange(100)
    pl = level
    pp = percent
    for p in LEVEL_ADJUST_PERCENTS:
        if percent < p: break
        percent -= p
        level += 1
    # print(pl, '->', level, ', ', pp, '->', percent)
    if level < 0: level = 0
    return level

