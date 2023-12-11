import pygame
from network import Network

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0


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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redraw_window(win, player: Player, player2: Player):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    start_pos = read_pos(n.get_pos())
    p = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(win, p, p2)

if __name__ == "__main__":
    main()