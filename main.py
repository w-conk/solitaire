import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solitare")

running = True

card_values = ["H13", "H12", "H11", "H10", "H09", "H08", "H07", "H06", "H05", "H04", "H03", "H02", "H01"]

# Create individual positions for each card (stacked)
card_positions = []
base_x, base_y = 100, 100
for i in range(len(card_values)):
    # Stack cards with slight offset
    card_positions.append(pygame.Vector2(base_x, base_y + i * 2))

dragging_card = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("green")

     # Draw all cards at their individual positions
    # Draw all cards EXCEPT the dragged one
    for i, card in enumerate(card_values):
        card_image = pygame.image.load(f"greywyvern-cardset/{card}.png")
        screen.blit(card_image, card_positions[i])

    # Check if mouse is being held down
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()

    # Find the topmost card under the mouse (check from top to bottom)
    # Find the topmost card under the mouse (check from top to bottom)
    if dragging_card is None and mouse_pressed:
        for i in range(len(card_values) - 1, -1, -1):  # Check from top card down
            card_image = pygame.image.load(f"greywyvern-cardset/{card_values[i]}.png")
            if (mouse_pos[0] > card_positions[i][0] and mouse_pos[0] < card_positions[i][0] + card_image.get_width() and 
                mouse_pos[1] > card_positions[i][1] and mouse_pos[1] < card_positions[i][1] + card_image.get_height()):
                dragging_card = i  # Store the index of the card being dragged
            
            # Move the dragged card to the end of the list so it draws last
                card_values.append(card_values.pop(i))
                card_positions.append(card_positions.pop(i))
                dragging_card = len(card_values) - 1  # Update to new position
            
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


