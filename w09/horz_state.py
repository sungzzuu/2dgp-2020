import gfw
from pico2d import *
from gobj import *
from player import Player
from background import HorzScrollBackground
from platform import Platform

canvas_width = 1120
canvas_height = 630

def enter():
    gfw.world.init(['bg', 'enemy', 'platform', 'item', 'player'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

def update():
    gfw.world.update()

    move_platform()

def move_platform():
    x = 0
    dx = -200 * gfw.delta_time
    for layer in range(gfw.layer.enemy, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)
            x = obj.right()

    cw = get_canvas_width()
    while x < cw:
        t = random.choice([Platform.T_10x2, Platform.T_2x2])
        pf = Platform(t, x, 0)
        gfw.world.add(gfw.layer.platform, pf)
        print('adding platform:', gfw.world.count_at(gfw.layer.platform))
        x += pf.width

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()
