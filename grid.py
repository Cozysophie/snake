from turtle import _Screen
import pygame

lightBlue = (106, 174, 203 )
pygame.font.init()
#text_font = pygame.font.Fontont("downloads.LVDCGO_",30)
                
class Grid():
    def __init__(self,block_size,offset,num_cols,num_rows):
        self.block_size = block_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.offset = offset
        self.grid = [[0 for J in range(self.num_cols)] for I in range(self.num_rows)]
        #self.draw_text =

    def print_grid(self): 
        for row in range(self.num_rows):
            for col in range(self.num_cols): 
                print(self.grid[row][col], end = " ")
            print()

    def draw(self,screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_rect = pygame.Rect(row*self.block_size+self.offset, col*self.block_size+self.offset, self.block_size-1, self.block_size-1) 
                pygame.draw.rect(screen,(lightBlue), cell_rect)

                
    #def draw_text(self,text, font, text_color,):
        # my_font = pygame.font.SysFont('Comic Sans MS', 30)
        # text_surface = my_font.render('Yum yum!', False, (0, 0, 0))
        # screen.blit(text_surface, (0,0))
        # print("Yum yum!")
        

