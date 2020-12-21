import pygame


class Button:

    # class attributes;; deal with this later

    buttons = ["hey"]

    # instance attributes (unique per obj)
    def __init__(self, surface, color, hover_color, x, y, text, function):
        self.surface = surface
        self.color = color
        self.hover_color = hover_color
        self.x = x
        self.y = y
        self.text = text
        self.function = function
        self.font = pygame.font.Font("freesansbold.ttf", 15)
        self.width = 200
        self.height = 50
        self.set_color = self.color
        self.is_toggle = False
        self.show = True

        #self.buttons.append(self)

    def draw_button(self):
        if self.show:
            pygame.draw.rect(self.surface, self.set_color, (self.x, self.y, 200, 50))
            text = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
            self.surface.blit(text, text_rect)


    # confirm that mouse is inside button
    def select_button(self, mouseX, mouseY):
        if self.x < mouseX < self.x+self.width and self.y < mouseY < self.y + self.height:
            return True
        return False

    # make the button a toggle button...
    def make_toggle(self):
        self.is_toggle = True
        self.show = False

    def toggle_button(self):
        self.show = not self.show
