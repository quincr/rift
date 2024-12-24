import rift
import pygame as pg

window = rift.Window((640, 360), 'RIFT Test project', flags=pg.SCALED)
font = rift.GUI.Font('m5x7.ttf')

scene = rift.Scene()

while window.Tick():
    scene.Render()

    window.surface.blit(font.Get(16).render('[ Testing project ]', False, (255, 255, 255)), (4, 0))
    window.surface.blit(font.Get(16).render(f'> FPS: {int(1 / window.delta_time * 100) / 100}', False, (255, 255, 255)), (4, 30))
