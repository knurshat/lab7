import pygame
import time
import os
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir,"images", "right_hand.png")
minute_hand = pygame.image.load(image_path)
image_path = os.path.join(script_dir,"images", "left_hand.png")
second_hand = pygame.image.load(image_path)
image_path = os.path.join(script_dir,"images", "mickeyclock.jpg")
clock_face = pygame.image.load(image_path)
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
CENTER = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = -minutes * 6
    second_angle = -seconds * 6

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    minute_rect = rotated_minute.get_rect(center=CENTER)
    second_rect = rotated_second.get_rect(center=CENTER)

    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000 // 30)

pygame.quit()
