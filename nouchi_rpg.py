# coding: utf-8
import pygame as pg
import sys

pg.init()
WIDTH = 640
HEIGHT = 480
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ウィンドウの作成")

font = pg.font.SysFont("applegothic", 80)
text1 = font.render("にゃんころもち", True, (0, 0, 0))

while True:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.blit(text1, (20, 50))
    pg.display.update()