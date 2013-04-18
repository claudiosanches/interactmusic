#!/usr/bin/env python
# http://www.pyglet.org/doc/api/index.html
import pyglet

music = pyglet.media.load('guitarra.ogg')
music.play()
pyglet.app.run()
