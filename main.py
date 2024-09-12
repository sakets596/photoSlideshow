import pygame
from sys import exit
from helper import screen_size, photo_list

pygame.init()

screen_width, screen_height = screen_size()
screen = pygame.display.set_mode(screen_size(), pygame.RESIZABLE)
clock = pygame.time.Clock()
game_active = True
index = 0
SLIDE_SPEED = 2000
pics = photo_list('static/imgs')


def active_photo(ind):
    try:
        active_pic = pics[index]
        pic_surface = pygame.image.load(active_pic)
        pic_width = pic_surface.get_width()
        pic_height = pic_surface.get_height()
        if pic_width > screen_width or pic_height > screen_height:
            pic_surface = pygame.transform.scale(pic_surface, (768,1024))
        pic_rect = pic_surface.get_rect(center=(screen_width/2, screen_height/2))
        return (pic_surface, pic_rect)
    except Exception as e:
        print(f"Error occured: {e}")


active_pic = pics[index]
pic_surface = pygame.image.load(active_pic)
pic_rect = pic_surface.get_rect(center=(screen_width/2, screen_height/2))

backward_button = pygame.Surface((50,50))
backward_button.fill('yellow')
backward_button_rect = backward_button.get_rect(midleft=(pic_rect.left, pic_rect.left))

forward_button = pygame.Surface((50,50))
forward_button.fill('green')
forward_button_rect = forward_button.get_rect(midright=(pic_rect.right, pic_rect.left))

# Initialize a variable to track mouse movement time
mouse_last_moved = pygame.time.get_ticks()
button_visible = False  # Start with the button hidden
BUTTON_HIDE_DELAY = 2000  # Hide button after 2 seconds

slide_timer = pygame.USEREVENT + 1
pygame.time.set_timer(slide_timer, SLIDE_SPEED)

while True:
    current_time = pygame.time.get_ticks()
    mouse_moved = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_last_moved = pygame.time.get_ticks()
            mouse_moved = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                try:
                    pygame.time.set_timer(slide_timer, SLIDE_SPEED) #resetting the event time to 2 sec again. so that slids don't rush.
                    if forward_button_rect.collidepoint(event.pos):
                        index = index + 1
                        if index >= len(pics) - 1:
                            index = len(pics) - 1
                        surface, rect = active_photo(index)
                        forward_button_rect = forward_button.get_rect(midright=(rect.right, rect.left))
                        backward_button_rect = backward_button.get_rect(midleft=(rect.left, rect.left))
                    if backward_button_rect.collidepoint(event.pos):
                        index = index - 1
                        if index <= 0:
                            index = 0
                        surface, rect = active_photo(index)
                        forward_button_rect = forward_button.get_rect(midright=(rect.right, rect.left))
                        backward_button_rect = backward_button.get_rect(midleft=(rect.left, rect.left))
                except Exception as e:
                    print(f"Error occured: {e}")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.time.set_timer(slide_timer, SLIDE_SPEED) #resetting the event time to 2 sec again. so that slids don't rush.
                index = index + 1
                if index >= len(pics) - 1:
                    index = len(pics) - 1
                surface, rect = active_photo(index)
                forward_button_rect = forward_button.get_rect(midright=(rect.right, rect.left))
                backward_button_rect = backward_button.get_rect(midleft=(rect.left, rect.left))
            if event.key == pygame.K_LEFT:
                pygame.time.set_timer(slide_timer, SLIDE_SPEED) #resetting the event time to 2 sec again. so that slids don't rush.
                index = index - 1
                if index <= 0:
                    index = 0
                surface, rect = active_photo(index)
                forward_button_rect = forward_button.get_rect(midright=(rect.right, rect.left))
                backward_button_rect = backward_button.get_rect(midleft=(rect.left, rect.left))
        elif event.type == slide_timer:
            index = index + 1
            if index >= len(pics) - 1:
                index = len(pics) - 1
            surface, rect = active_photo(index)
            forward_button_rect = forward_button.get_rect(midright=(rect.right, rect.left))
            backward_button_rect = backward_button.get_rect(midleft=(rect.left, rect.left))

    # Check if the mouse has not moved for more than 2 seconds
    if current_time - mouse_last_moved < BUTTON_HIDE_DELAY:
        button_visible = True
    else:
        button_visible = False

    screen.fill((0,0,0))
    try:
        surface, rect = active_photo(index)
        screen.blit(surface, rect)
    except Exception as e:
        print(f"Error occured: {e}")
    if button_visible:
        screen.blit(forward_button, forward_button_rect)
        screen.blit(backward_button, backward_button_rect)

    clock.tick(120)
    pygame.display.update()
