import pygame
import math

# Py_game start additionall work cube
def hsv_rgb(gr, light):
    hi = abs(gr / 60) // 6
    p = light * (1 - 100)
    q = light * (1 - (gr / 60) - abs(gr / 60) * 100)
    t = light * (1 - (1 - ((gr / 60) - abs(gr / 60))) * 100)
    x = 255 / 100
    print(hi, p, q, t)
    if hi == 0:
        rgb = (light * x, p * x, t * x)
    elif hi == 1:
        rgb = (q, light, p)
    elif hi == 2:
        rgb = (p, light, t)
    elif hi == 3:
        rgb = (p, q, light)
    elif hi == 4:
        rgb = (t, p, light)
    elif hi == 5:
        rgb = (light, p, q)
    return rgb


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # название
    pygame.display.set_caption('крест')
    # размеры окна:
    size = width, height = 300, 300
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    w = int(input())
    hue = int(input())
    if w % 4 == 0 and w < 101 and 0 < hue <= 360:
        # pygame.draw.rect(screen, (255, 255, 0), (150, 50, 100, 100))
        start_pos = int(150 - (w / 2))
        finish_pos = int(150 + (w / 2))
        pos_2 = start_pos - int(w / 2)
        print(hsv_rgb(hue, 0.75))
        # pygame.draw.rect(screen, hsv_rgb(hue, 0.75), (start_pos, start_pos, w, w))
        # pygame.draw.polygon(screen, hsv_rgb(hue, 1), [[150, pos_2],
        #                                               [start_pos, start_pos], [start_pos + w, start_pos],
        #                                               [w + (w / 2) + start_pos, pos_2]])
        # pygame.draw.polygon(screen, hsv_rgb(hue, 0.5), [[start_pos + w, start_pos], [150 + w, pos_2], [150 + w, 150],
        #                                                 [150 + (w / 2), 150 + (w / 2)]])
        # # формирование кадра:
        # # команды рисования на холсте
        # # смена (отрисовка) кадра:
        pygame.display.flip()
        # # ожидание закрытия окна:
        while pygame.event.wait().type != pygame.QUIT:
            pass
        # завершение работы:
    else:
        print('Неправильный формат ввода')
        pygame.quit()
    pygame.quit()
