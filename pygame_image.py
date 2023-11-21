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
    kou2 = pg.transform.rotozoom(kou1, 10, 1.0)
    kou_list = [kou1, kou2]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2 , [1600-x, 0])
        screen.blit(kou_list[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()