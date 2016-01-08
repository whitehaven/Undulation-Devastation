from __future__ import division
from random import uniform

from pyglet import clock, window
from pyglet.gl import *

import primitives


class Entity(object):
    def __init__(self, id, size, x, y, rot):
        self.id = id
        self.circle = primitives.Circle(x=0, y=0, z=0, width=100, color=(1, 0, 0, 1), stroke=50)

    def draw(self):
        self.circle.render()


class World(object):
    def __init__(self):
        self.ents = {}
        self.nextEntId = 0
        clock.schedule_interval(self.spawnEntity, 0.25)

    def spawnEntity(self, dt):
        size = uniform(1.0, 100.0)
        x = uniform(-100.0, 100.0)
        y = uniform(-100.0, 100.0)
        rot = uniform(0.0, 360.0)
        ent = Entity(self.nextEntId, size, x, y, rot)
        self.ents[ent.id] = ent
        self.nextEntId += 1
        return ent

    def tick(self):
        pass

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        for ent in self.ents.values():
            ent.draw()


class Camera(object):
    def __init__(self, win, x=0.0, y=0.0, rot=0.0, zoom=1.0):
        self.win = win
        self.x = x
        self.y = y
        self.rot = rot
        self.zoom = zoom

    def worldProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        widthRatio = self.win.width / self.win.height
        gluOrtho2D(
            -self.zoom * widthRatio,
            self.zoom * widthRatio,
            -self.zoom,
            self.zoom)

    def hudProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.win.width, 0, self.win.height)


class Hud(object):
    def __init__(self, win):
        self.fps = clock.ClockDisplay()

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.fps.draw()


class App(object):
    def __init__(self):
        self.world = World()
        self.win = window.Window(fullscreen=False, vsync=True)
        self.camera = Camera(self.win, zoom=100.0)
        self.hud = Hud(self.win)
        clock.set_fps_limit(60)

    def mainLoop(self):
        while not self.win.has_exit:
            self.win.dispatch_events()

            self.world.tick()

            self.camera.worldProjection()
            self.world.draw()

            self.camera.hudProjection()
            self.hud.draw()

            clock.tick()
            self.win.flip()


app = App()
app.mainLoop()
