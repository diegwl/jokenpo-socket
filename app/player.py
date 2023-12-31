import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.x -= self.vel

        if key[pygame.K_RIGHT]:
            self.x += self.vel

        if key[pygame.K_UP]:
            self.y -= self.vel

        if key[pygame.K_DOWN]:
            self.y += self.vel

        self.update()