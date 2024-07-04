import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("flappy bird")

BACKGROUND = pygame.image.load('C:\\Users\\salmo\\python work\\flappybird\\assets\\assets\\sprites\\background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Bird(pygame.sprite.Sprite,):
    
    def __init__(self):
        super().__init__()
        
        
        self.images = [pygame.image.load('C:\\Users\\salmo\\python work\\flappybird\\assets\\assets\\sprites\\bluebird-upflap.png'),
                       pygame.image.load('C:\\Users\\salmo\\python work\\flappybird\\assets\\assets\\sprites\\bluebird-midflap.png'), 
                       pygame.image.load('C:\\Users\\salmo\\python work\\flappybird\\assets\\assets\\sprites\\bluebird-downflap.png')]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 6
        self.rect.y = SCREEN_HEIGHT // 2

    def update(self):
        self.image_index = (self.image_index + 1) % 3
        self.image = self.images[self.image_index]
        self.rect.y += 10
    def up(self):
        self.rect.y -=30
    

bird = Bird()
bird_group = pygame.sprite.Group()
bird_group.add(bird)

running = True
clock = pygame.time.Clock()

while running:
    if clock.tick(10):
        screen.blit(BACKGROUND, (0,0))
        bird_group.draw(screen)
        bird_group.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()


pygame.quit()