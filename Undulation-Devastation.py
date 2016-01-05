import pyglet

import primitives

window = pyglet.window.Window()
counter = 0


class Producer(object):
    def __init__(self, x, y, width, health, color=(0, 0, 0, 1)):
        self.shape = primitives.Circle(x, y, z=0, width=2, color=color, stroke=width / 2, rotation=0.0,
                                       style=pyglet.gl.GLU_FILL)
        self.health = health


# class Collision? with collided members

def update_frame(dt):
    global counter
    counter += 1


@window.event
def on_draw():
    print(counter)
    pyglet.gl.glClearColor(0, 0, 0, 0)
    window.clear()


pyglet.clock.schedule_interval(update_frame, 1 / 10.0)

pyglet.app.run()
