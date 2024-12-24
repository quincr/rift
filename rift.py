from __future__ import annotations

__author__ = 'quincr'
__version__ = '0.0'

import pygame as pg
import time

if not pg.get_init():
    pg.init()

class Window():
    def __init__(self: Window, resolution: tuple[int, int] = (800, 600), title: str = 'Rift Window', icon: pg.Surface = None, flags: int = 0) -> None:
        self.surface = pg.display.set_mode(resolution, flags)
        pg.display.set_caption(title)

        if icon is None:
            pg.display.set_icon(pg.Surface((0, 0)))
        else:
            pg.display.set_icon(icon)

        self._clock = pg.time.Clock()
        self._kill = False

        self._last_time = time.time()
        self.delta_time = 0.0001

    def Tick(self: Window, target_fps: int = 120, clear_color: pg.Color = pg.Color(0, 0, 0)) -> bool:
        self._clock.tick(target_fps)

        cur_time = time.time()
        self.delta_time = max(cur_time - self._last_time, 0.0001)
        self._last_time = cur_time

        pg.display.flip()
        self.surface.fill(clear_color)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

        if self._kill:
            return False

        return True

    def Kill(self: Window) -> None:
        self._kill = True

class GUI():
    class Font():
        def __init__(self: GUI.Font, path: str) -> None:
            self.path = path
            self._cache = {}

        def Get(self: GUI.Font, size: int) -> pg.font.Font:
            if not size in self._cache:
                self._cache[size] = pg.font.Font(self.path, size)

            return self._cache[size]

class Scene():
    def __init__(self: Scene) -> None:
        self._font = GUI.Font('m3x6.ttf')

    def Render(self: Scene) -> None:
        window_surf = pg.display.get_surface()
        half_res = pg.Vector2(window_surf.get_width() / 2, window_surf.get_height() / 2)

        for x in range(-2, 2):
            for y in range(-2, 2):
                pg.draw.rect(window_surf, (40, 40, 40) if (x + y) % 2 == 0 else (50, 50, 50), (x * 24 + half_res.x, -y * 24 - 24 + half_res.y, 24, 24))
                window_surf.blit(self._font.Get(16).render(f'{x},{y}', False, (80, 80, 80)), (x * 24 + half_res.x, -y * 24 - 24 + half_res.y))

        pg.draw.circle(window_surf, (255, 255, 0), half_res, 2)
