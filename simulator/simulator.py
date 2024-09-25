import pygame
import random

class Block:
    def __init__(self, x, y, width, height, colour = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour if colour else self.random_colour()

    def random_colour(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Simulator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.placed_blocks = []

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('2D Bin Packing Simulator')

        self.running = True

    def check_overlap(self, block1, block2):
        horizontal_check = (block1.x < block2.x and block1.x + block1.width > block2.x) or (block1.x < block2.x + block2.width and block1.x + block1.width > block2.x + block2.width)
        vertical_check = (block1.y < block2.y and block1.y + block1.height > block2.y) or (block1.y < block2.y + block2.height and block1.y + block1.height > block2.y + block2.height)

        return horizontal_check and vertical_check
    
    def valid_placement(self, input_block):
        if input_block.x < 0 or input_block.x > self.width or input_block.y < 0 or input_block.y > self.height or (input_block.x + input_block.width > self.width) or (input_block.y + input_block.height > self.height):
            return False
        for block in self.placed_blocks:
            if self.check_overlap(block, input_block):
                return False
        return True

    def place_block(self, block):
        if self.valid_placement(block):
            self.placed_blocks.append(block)
            return True
        else:
            print("Invalid Placement")
            return False
        
    def draw_blocks(self):
        self.screen.fill((255, 255, 255)) 
        for block in self.placed_blocks:
            pygame.draw.rect(self.screen, block.colour, pygame.Rect(block.x, self.height - block.y - block.height, block.width, block.height))
        pygame.display.flip() 

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.draw_blocks()
        pygame.quit()

sim = Simulator(600, 400) 
block1 = Block(0, 0, 100, 100)
block2 = Block(0, 100, 150, 100)
block3 = Block(100, 0, 300, 200)
block4 = Block(400, 0, 200, 100)
block5 = Block(800, 0, 100, 100)
block6 = Block(500, 50, 150, 100)

sim.place_block(block1)
sim.place_block(block2)
sim.place_block(block3)
sim.place_block(block4) 
sim.place_block(block5)
sim.place_block(block6) 

sim.run()  
