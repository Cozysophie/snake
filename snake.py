import pygame

class Snake():
    def __init__(self,block_size):
        self.snake_body = [[90,90]]
        self.block_size = block_size
        self.direction = " "
        self.ate = False
        self.last_meal = 0

    def draw(self,screen):
        for square in self.snake_body:
            cell_rect= pygame.Rect(square[0],square[1],self.block_size, self.block_size)
            pygame.draw.rect(screen,((0,0,0)), cell_rect)

    def move_forward(self):
        if self.direction == "right":
            head = self.snake_body[0]
            self.snake_body.pop()
            self.snake_body.insert(0,[head[0]+self.block_size, head[1]])
        if self.direction == "left":
            head = self.snake_body[0]
            self.snake_body.pop()
            self.snake_body.insert(0,[head[0]-self.block_size, head[1]])
           
        if self.direction == "up":
            head = self.snake_body[0]
            self.snake_body.pop()
            self.snake_body.insert(0,[head[0], head[1]-self.block_size])
        if self.direction == "down":
            head = self.snake_body[0]
            self.snake_body.pop()
            self.snake_body.insert(0,[head[0], head[1]+self.block_size])

    def eat(self):
        tail = self.snake_body[-1]
        self.snake_body.append(tail)
        self.last_meal = pygame.time.get_ticks()
        
        self.ate = True
        
        
    