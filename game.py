import random
from tkinter import font
from tkinter.tix import DisplayStyle
import pygame

from grid import Grid
from snake import Snake



class Game():
    def __init__(self):
        self.offset = 90
        self.block_size = 30
        self.grid = Grid(self.block_size,self.offset,24,24)
        self.snake = Snake(self.block_size)
        self.food = self.drop_food()
        self.playing = True

    def drop_food(self):
        x = random.choice(range(self.grid.num_cols))*self.grid.block_size+self.offset
        y = random.choice(range(self.grid.num_rows))*self.grid.block_size+self.offset
        return [x,y] 
    
    def check_location(self,screen):
        if self.snake.snake_body[0] == self.food:
            self.food = self.drop_food()
            self.snake.eat()
        head = self.snake.snake_body[0] 
        if head[0] < 0+ self.offset or head[1] < 0+self.offset or head[0] > self.grid.num_cols*self.grid.block_size +self.offset - 1 or head[1] > self.grid.num_rows*self.grid.block_size + self.offset - 1:
            self.game_over()
            print('game over')
        for i in range(1,len(self.snake.snake_body)):
            if head == self.snake.snake_body[i] and len(self.snake.snake_body)>2:
                self.game_over()
                print('game over')

    def draw(self,screen):
        self.grid.draw(screen)
        self.snake.draw(screen)
        food_rect= pygame.Rect(self.food[0],self.food[1],self.grid.block_size, self.grid.block_size)
        pygame.draw.rect(screen,((0,0,0)),food_rect)  
        
    def game_over(self):
        self.playing = False
        score = len(self.snake.snake_body)
        #self.game_over_text = font.render("GAME OVER", True, 200,200,200) 
        #score_text = font.render(f"Yeah You Ate {score} Squares", True, 200,200,200)
        #DisplayStyle.fill((0,0,0))
        print(score)


       