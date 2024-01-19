import sys
import pygame
from game import Game

screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
blue = (171, 211, 247)
lightBlue = (106, 174, 203 )

Square = pygame.Rect(0, 0, 50, 50) 

my_font = pygame.font.SysFont('Comic Sans MS', 30)
yummy_in_my_tummy = my_font.render('Yum yum!', False, (0, 0, 0))

game = Game()

clock = pygame.time.Clock() 
move_forward = pygame.USEREVENT
pygame.time.set_timer(move_forward,200)

current_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and game.snake.direction != "up":
                game.snake.direction = "down"
            if event.key == pygame.K_UP and game.snake.direction != "down":
                game.snake.direction = "up"
            if event.key == pygame.K_LEFT and game.snake.direction != "right":
                game.snake.direction = "left"
            if event.key == pygame.K_RIGHT and game.snake.direction != "left":
                game.snake.direction = "right"
        if event.type == move_forward and game.playing == True: 
            game.snake.move_forward() 
            game.check_location(screen)
            current_time = pygame.time.get_ticks()

    screen.fill((blue))

    if current_time - game.snake.last_meal > 100 and game.snake.ate == True:
        game.snake.ate = False
        print(f'current time;{current_time}')
        print(f'last meal;{game.snake.last_meal}')
        print(f'time elapsed;{current_time - game.snake.last_meal}')
        print(f'snake ate;{game.snake.ate}')
    
    if game.snake.ate == True:
        screen.blit(yummy_in_my_tummy,(0,0))


    game.draw(screen)
    pygame.display.update() 
    clock.tick(60)