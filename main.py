import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solitare")

running = True

card_values = ["H13", "H12", "H11", "H10", "H09", "H08", "H07", "H06", "H05", "H04", "H03", "H02", "H01","D13", "D12", "D11", "D10", "D09", "D08", "D07", "D06", "D05", "D04", "D03", "D02", "D01","C13", "C12", "C11", "C10", "C09", "C08", "C07", "C06", "C05", "C04", "C03", "C02", "C01","S13", "S12", "S11", "S10", "S09", "S08", "S07", "S06", "S05", "S04", "S03", "S02", "S01"]

card_is_face_up = []
for i in range(len(card_values)):
    card_is_face_up.append(False)  # Start all cards face down

random.shuffle(card_values)

stacks = [[] for _ in range(7)]  # 7 empty stacks
deck_remaining = []  

# Deal cards to stacks (like solitaire)
card_index = 0
for stack_num in range(7):
    for card_in_stack in range(stack_num + 1):  # Stack 0 gets 1 card, stack 1 gets 2, etc.
        if card_index < len(card_values):
            stacks[stack_num].append(card_index)
            card_index += 1

# Remaining cards go to deck
deck_remaining = list(range(card_index, len(card_values)))# Cards not dealt yet

# Create positions for 7 stacks
card_positions = []
stack_x_positions = [100, 200, 300, 400, 500, 600, 700]  # X positions for each stack

for stack_num in range(7):
    for card_in_stack in range(len(stacks[stack_num])):
        card_index = stacks[stack_num][card_in_stack]
        x = stack_x_positions[stack_num]
        y = 100 + (card_in_stack * 20)  # 20 pixel offset between cards in stack
        card_positions.append(pygame.Vector2(x, y))

# Add positions for deck cards (off-screen or in a pile)
for card_index in deck_remaining:
    card_positions.append(pygame.Vector2(1000, 50)) 
    
for stack_num in range(7):
    if len(stacks[stack_num]) > 0:
        top_card_index = stacks[stack_num][-1]  # Last card in stack
        card_is_face_up[top_card_index] = True # Deck position

dragging_card = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("green")

    
    # Sort cards by their screen position (from back to front)
    sorted_card_indices = sorted(range(len(card_values)), key=lambda i: (card_positions[i].y, card_positions[i].x))

# Draw all cards in screen order (from back to front)
    for i in sorted_card_indices:
        if i != dragging_card:
            if card_is_face_up[i]:
                card_image = pygame.image.load(f"greywyvern-cardset/{card_values[i]}.png")
            else:
                card_image = pygame.image.load(f"greywyvern-cardset/back1.png")
            screen.blit(card_image, card_positions[i])
    
    # Draw the dragged card last so it appears on top
    if dragging_card is not None:
        if card_is_face_up[dragging_card]:
            card_image = pygame.image.load(f"greywyvern-cardset/{card_values[dragging_card]}.png")
        else:
            card_image = pygame.image.load(f"greywyvern-cardset/back1.png")
        screen.blit(card_image, card_positions[dragging_card])
            # Check if mouse is being held down
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()

    if dragging_card is None and mouse_pressed:
    # Check collision from top to bottom on screen (not list order)
        for i in range(len(card_values) - 1, -1, -1):  # Check from top card down
            card_image = pygame.image.load(f"greywyvern-cardset/{card_values[i]}.png")
            if (mouse_pos[0] > card_positions[i][0] and mouse_pos[0] < card_positions[i][0] + card_image.get_width() and 
                mouse_pos[1] > card_positions[i][1] and mouse_pos[1] < card_positions[i][1] + card_image.get_height()):
                dragging_card = i  # Store the index of the card being dragged
                break

    # Update position of the dragged card only
    if dragging_card is not None and mouse_pressed:
        card_image = pygame.image.load(f"greywyvern-cardset/{card_values[dragging_card]}.png")
        card_positions[dragging_card] = pygame.Vector2(mouse_pos[0] - (card_image.get_width()/2), mouse_pos[1] - (card_image.get_height()/2))

    
    #stop dragging when mouse is released
    if not mouse_pressed:
        dragging_card = None

    pygame.display.flip()

pygame.quit()


