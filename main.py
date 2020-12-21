# experimenting with pygame
"""
game: there are squares of colors in a row and you have to put them in the correct order. Use OOP and pygame.

steps:
X figure out how to make a square with pygame
X make a class that can make blocks (basic)
    X there will be a property for color and num (important for correct order)
X make a for loop that draws all the squares next to each other
X make the colors of the squares be a random gradient!
X mix up the colors (random)
    - later: animate the process?!?! idk could look cool...
X be able to click/select a square (click on square and return which one/id
X switch locations of squares (first click: selector, second click: switch)
    - if second click != square or if it's the same square, unselect it.
    - put animation when selecting and switching!! (size pulses, border)
X check if the order is correct
    X when i switched x vals, i also switched it's index in blockHolder... if num
    matches all the indexes, then it's correct
    X make one end of it locked so that user knows what order to do it
    X *all four corners* because i realize you could still do it flipped the wrong way :(

later:
- change difficulty level (buttons?)
    - only perfect moves (no way too hard)
    - gradients are further or closer apart! (hard to do)
    X 2d!!!!!
    - change which blocks are locked! (eg four random ones? preferably on the outside... use abs to check dist. from
    border)
- control board size (buttons)
- selection signal + switch animation
X make pre given squares actually locked? like you can't move them? + symbol!
X help button >:( --> gives away one incorrect square
X should i make a button class? what are the common attributes? (size? x, y, color??, text, and what function that they
 set off)

- sound effects!!! could be so satisfying!!!
- make a score system? based on mode, time, # moves, # hints

CURRENTLY WORKING ON 11/16
- making the buttons functional:
    X hint reveals the next incorrect square
    X hide the mode buttons
    X "new game" button toggles mode button (drop down menu)
    - mode buttons eventually causes new game... idk how i'm gonna do that yet tho
        - make sure to reset blocks and confetti~
- organize the code so it makes more sense...
- after this project i want to do a follow along vid (flappy bird) + watch other videos from clear code on yt
- make hint + win screen more visual - it'd be cool if i could do a cool confetti effect...

- confetti feature... (class)
    X colors are random colors from block's colors
    X same size? or make different sizes and smaller ones fall slower
    X small skinny rectangles
    X falls from the top
    - ok it'd be cool if i had the words 'YOU WON' that fall with the confetti (at dif speeds) and have them rotate?
    - the words have a range of x values they can be, but they have to be int he correct order

to fix:
- if random colors are greater than half way, increment them backwards...
- also fix color_factor so that i don't end up with duplicate colors
- make all three rgb values dependent on location? (instead of just two)
X different system for choosing random colors...
    - choose num_colors blocks (after they're initialized) and use random.choose()...
    X four corners + some random?
- minor thing: for the confetti, rearrange the order from size:small->big so that big ones are drawn last and
overlap the small ones...
- start working on the new game buttons... but how...
- also, when you click one of those, it should toggle the buttons to close... but worry about that later...
- the overall organization / structure of this code is really bad but i don't know how to fix it...
"""


import pygame
import Block
import Button
import Confetti
import random


def hint():
    pos = check_order()
    # note: current location=placeHolder[index] & correct location=self.num & pos = current location
    # set show_hint of that block to True
    for index, block in enumerate(block_holder):
        if pos == index:
            block.show_hint = True
            break  # hopefully for saving runtime


def new_game():
    print("toggle mode buttons")
    # toggle show on mode buttons
    for btn in buttons[2:5]:
        btn.toggle_button()


def set_easy():
    return set_mode("easy")


def set_medium():
    return set_mode("medium")


def set_hard():
    return set_mode("hard")


def set_mode(mode_in):
    # change mode, then start a new game...
    print(mode_in)
    if mode_in == "easy":
        size_in = 80
        num_rows_in, num_cols_in = 5, 5
    elif mode_in == "medium":
        size_in = 50
        num_rows_in, num_cols_in = 8, 8
    else:
        size_in = 40
        num_rows_in, num_cols_in = 10, 10
    return size_in, num_rows_in, num_cols_in


# switches the order of the blocks in blockHolder!
def switch_order(b1, b2):  # b1 = blocksSelected[0], etc
    b1.x, b2.x = b2.x, b1.x
    b1.y, b2.y = b2.y, b1.y
    i1 = block_holder.index(b1)
    i2 = block_holder.index(b2)
    block_holder[i1] = b2
    block_holder[i2] = b1


# note that block.num = it's correct index
def check_order():
    for i, block in enumerate(block_holder):
        if block.num != i:
            return i  # position of the first incorrect block
    return "win"


# the square at the given index will be correct
def make_correct(block_index):
    for i, block in enumerate(block_holder):
        if block.num == block_index:
            switch_order(block, block_holder[block_index])
    block_holder[block_index].toggle_lock()

    # corners = confetti colors
    confetti_colors.append(block_holder[block_index].color)


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gradiant Game!")
clock = pygame.time.Clock()


"""CONSTANT BETWEEN GAMES"""
# blocks
X_START = 50
Y_START = 50

# button colors
hint_color = (214, 28, 56)
hint_hover = (173, 2, 26)
restart_color = (94, 118, 224)
restart_hover = (43, 60, 138)
mode_color = (11, 19, 59)
mode_hover = (43, 60, 138)

# text
font = pygame.font.Font("freesansbold.ttf", 15)

# confetti
num_colors = 5
num_confetti = 150  # adjust

# defining the buttons
hint_btn = Button.Button(screen, hint_color, hint_hover, 525, 75, "H I N T", hint)
restart_btn = Button.Button(screen, restart_color, restart_hover, 525, 200, "N E W  G A M E", new_game)
easy_btn = Button.Button(screen, mode_color, mode_hover, 525, 250, "E A S Y", set_easy)
medium_btn = Button.Button(screen, mode_color, mode_hover, 525, 300, "M E D I U M", set_medium)
hard_btn = Button.Button(screen, mode_color, mode_hover, 525, 350, "H A R D", set_hard)
buttons = [hint_btn, restart_btn, easy_btn, medium_btn, hard_btn]
for btn in buttons[2:5]:
    btn.make_toggle()

""" VARIABLES """

# game
game_state = "playing"
mode = "easy"
end_text = "YOU WON!"

# blocks
color_main = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
color1, color2 = random.sample((0, 1, 2), 2)  # color1 and color2 cannot be the same...
block_holder = []  # holds all blocks
blocks_selected = []  # for switching order
size, num_rows, num_cols = set_mode(mode)
color_factor = 255//num_rows
num_blocks = num_rows * num_cols

# confetti
confetti_colors = []
color_chance = num_blocks//num_colors
confetti = []
letters = []


"""BLOCK STUFF"""
# store block objects in []
for y in range(num_cols):
    for x in range(num_rows):
        # difficulty: 1 = easiest, 0 = middle, 2 = hardest
        color_main[color1] = y * color_factor
        color_main[color2] = x * color_factor
        color = [color_main[0], color_main[1], color_main[2]]
        block_x = X_START + size*x
        block_y = Y_START + size*y
        num = y*num_rows + x
        block_holder.append(Block.Block(screen, color, block_x, block_y, size, num))

# shuffle shuffle the indexes in block_holder
random.shuffle(block_holder)

# change the x values to match its (shuffled) index... only needs to be done once after the og shuffle
for i, block in enumerate(block_holder):
    y = i//num_rows
    block.x = X_START + size*i - size*num_rows*y
    block.y = Y_START + size*y

# put certain blocks in the correct place + locks them
TOP_LEFT_CORNER = 0
TOP_RIGHT_CORNER = num_cols - 1
BOTTOM_LEFT_CORNER = num_cols*(num_rows-1)
BOTTOM_RIGHT_CORNER = num_blocks-1
corner_nums = [TOP_LEFT_CORNER, TOP_RIGHT_CORNER, BOTTOM_LEFT_CORNER, BOTTOM_RIGHT_CORNER]
for corner in corner_nums:
    make_correct(corner)


"""CONFETTI + WORDS"""
# hold all confetti in confetti[]
for i in range(num_confetti):
    size = random.randint(30, 80)/10  # so there's decimals
    x = random.randint(0, SCREEN_WIDTH)
    y = -(random.randint(0, 250) + (size*50)) + 100
    size_factor = random.randint(5, 40) / 10
    size = (size, size*2.5)
    color = random.choice(confetti_colors)
    confetti.append(Confetti.Confetti(screen, x, y, size, color))

# hold all letters in letters[]
for index, letter in enumerate(end_text):
    column = SCREEN_WIDTH / len(end_text)
    x = index*column + random.randint(0, int(column - 20))
    speed = random.randint(10, 30) / 10
    letters.append(Confetti.FallingLetters(screen, letter, x, -180, speed))


# while loop
running = True
while running:
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)  # at rest arrow goes back to normal which is annoying

    # change cursor shape when hovering over buttons
    for btn in buttons:
        if btn.select_button(mouseX, mouseY):
            # hover!
            btn.set_color = btn.hover_color
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
            # ^ cursor has some issues but whatever
        else:
            btn.set_color = btn.color

    # react to user events
    for event in pygame.event.get():
        # close window on click
        if event.type == pygame.QUIT:
            running = False
        # check if mouse is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # if a hint is showing, clicking it will disable it
            for block in block_holder:
                block.show_hint = False
                # probably not very efficient but...

            # checks buttons to see which was clicked... how do i loop through all of them?
            for btn in buttons:
                if btn.select_button(mouseX, mouseY):
                    btn.function()  # calls the corresponding function

            # checks every Block to see which one was clicked... Blocks cannot be moved after winning
            if game_state == "playing":
                for block in block_holder:
                    if block.select_block(mouseX, mouseY):
                        blocks_selected.append(block)

                if len(blocks_selected) > 1:  # switches order
                    b1 = blocks_selected[0]
                    b2 = blocks_selected[1]
                    """if b1 == b2:  # will uncomment after i make a locked symbol
                        b1.toggle_lock()"""
                    if (not b1.is_locked) and (not b2.is_locked):
                        switch_order(b1, b2)
                    blocks_selected = []
                    if check_order() == "win":
                        print("YOU WIN!")
                        game_state = "won"

                    break  # IMPORTANT
    # somehow messing with the order and adding the [break] fixed my problem...

    # background color
    screen.fill((180, 200, 255))

    # draws the blocks
    for block in block_holder:
        block.draw_block()

    # draws the buttons
    hint_btn.draw_button()
    restart_btn.draw_button()
    easy_btn.draw_button()
    medium_btn.draw_button()
    hard_btn.draw_button()

    # draw confetti + text if game_state == "won"
    if game_state == "won":
        for piece in confetti:
            piece.draw()
            if piece.y >= SCREEN_HEIGHT+50:
                confetti.remove(piece)
        for letter in letters:
            letter.draw()
            if letter.y >= SCREEN_HEIGHT:
                letters.remove(letter)

    pygame.display.update()
    clock.tick(50)
pygame.quit()
