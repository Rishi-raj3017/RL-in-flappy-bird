import pygame
import random

class Ground:
    ground_level = 500

    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width, 5)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)



class Pipes:
     width = 15
     opening = 100

     def __init__(self, win_width):
         self.x = win_width
         self.top_pipe_height = random.randint(50, Ground.ground_level - self.opening - 50)
         self.bottom_pipe_y = self.top_pipe_height + self.opening
         self.bottom_pipe_height = Ground.ground_level - self.bottom_pipe_y
         
         self.top_pipe_rect = pygame.Rect(self.x, 0, self.width, self.top_pipe_height)
         self.bottom_pipe_rect = pygame.Rect(self.x, self.bottom_pipe_y, self.width, self.bottom_pipe_height)
         
         self.passed = False
         self.off_screen = False


     def draw(self, window):
         pygame.draw.rect(window, (255, 255, 255), self.top_pipe_rect)
         pygame.draw.rect(window, (255, 255, 255), self.bottom_pipe_rect)
         

     def update(self):
         self.x -= 1
         # Update rectangle positions to match the new x coordinate
         self.top_pipe_rect.x = self.x
         self.bottom_pipe_rect.x = self.x
         
         if self.x + Pipes.width <= 50:
             self.passed = True

         if self.x <= -self.width:
             self.off_screen = True
         

         