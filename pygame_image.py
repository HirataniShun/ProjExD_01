import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tmr = 0 

    kou1 = pg.image.load("ex01/fig/3.png")
    kou1 = pg.transform.flip(kou1, True, False)
    kou_list = [kou1]
    for i in range(20):
        kou_list.append(pg.transform.rotozoom(kou1, i/2, 1.0))
    for i in range(20):
        kou_list.append(pg.transform.rotozoom(kou1, 10-(i/2), 1.0))
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kou_list[tmr%40], [300, 200])
        pg.display.update()
        tmr += 1
        if tmr == 3199:
            tmr = 0
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()