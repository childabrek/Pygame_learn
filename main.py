import pygame.examples
import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


size = width, heights = 400, 400
surface = pygame.display.set_mode(size)
sprite = pygame.sprite.Sprite()
running = True
all_sprites = pygame.sprite.Group()
pygame.mouse.set_visible(False)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            surface.fill((0, 0, 0))
            si = pygame.mouse.get_pos()
            sprite.image = load_image('arrow.png')
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = si[0], si[1]
            all_sprites.add(sprite)
            all_sprites.draw(surface)
    pygame.display.flip()
