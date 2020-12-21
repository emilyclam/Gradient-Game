import pygame


class Block:
    def __init__(self, surface, color, x, y, size, num):
        # all these variables will be given once we make all the blocks togther
        # super(Block, self).__init__()
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.num = num
        self.is_locked = False
        self.show_hint = False  # draws an X on the first incorrect square
        self.font = pygame.font.Font("freesansbold.ttf", 15)


    def draw_block(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.size, self.size))

        # draw the X if show_hint is true
        if self.show_hint:
            text = self.font.render("X", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
            self.surface.blit(text, text_rect)

    def toggle_lock(self):
        self.is_locked = not self.is_locked  # toggles the boolean

    def select_block(self, mouseX, mouseY):
        if self.x < mouseX < self.x+self.size and self.y < mouseY < self.y+self.size:
            # add an animation to show the block was clicked
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)  # deosn't work
            return True
        else:
            return False

    def to_string(self):
        return "x: " + str(self.x) + "\ny: " + str(self.y) + "\ncolor: " + str(self.color) + "\nnum: " + str(self.num)
