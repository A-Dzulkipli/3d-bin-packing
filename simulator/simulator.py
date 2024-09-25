class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Simulator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.placed_blocks = []

    def check_overlap(self, block1, block2):
        horizontal_check = (block1.x < block2.x and block1.x + block1.width > block2.x) or (block1.x < block2.x + block2.width and block1.x + block1.width > block2.x + block2.width)
        vertical_check = (block1.y < block2.y and block1.y + block1.height > block2.y) or (block1.y < block2.y + block2.height and block1.y + block1.height > block2.y + block2.height)

        return horizontal_check and vertical_check
    
    def valid_placement(self, input_block):
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

sim = Simulator(1,1)

block1 = Block(0,0,1,1)
block2 = Block(1,1,1,1)
block3 = Block(0.5, 0.5, 1, 1)

print(sim.check_overlap(block1, block2))
print(sim.check_overlap(block1, block3))
print(sim.check_overlap(block2, block3))
