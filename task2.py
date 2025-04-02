import pygame
import os

pygame.init()

WIDTH, HEIGHT = 300, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

button_size = (50, 50)

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir,"images", "play.png")
play_img = pygame.transform.scale(pygame.image.load(image_path), button_size)
image_path = os.path.join(script_dir,"images", "pause.png")
pause_img = pygame.transform.scale(pygame.image.load(image_path), button_size)
image_path = os.path.join(script_dir,"images", "next.png")
next_img = pygame.transform.scale(pygame.image.load(image_path), button_size)
image_path = os.path.join(script_dir,"images", "prev.png")
prev_img = pygame.transform.scale(pygame.image.load(image_path), button_size)

button_size = (50, 50)
play_rect = pygame.Rect(100, 75, *button_size)
pause_rect = pygame.Rect(160, 75, *button_size)
next_rect = pygame.Rect(220, 75, *button_size)
prev_rect = pygame.Rect(40, 75, *button_size)

music_folder = "tracks"
tracks = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0

if tracks:
    pygame.mixer.music.load(tracks[current_track])

def play_music():
    pygame.mixer.music.play()

def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    pygame.mixer.music.load(tracks[current_track])
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    pygame.mixer.music.load(tracks[current_track])
    play_music()

running = True
while running:
    screen.fill((255, 255, 255))
    
    screen.blit(prev_img, prev_rect.topleft)
    screen.blit(play_img, play_rect.topleft)
    screen.blit(pause_img, pause_rect.topleft)
    screen.blit(next_img, next_rect.topleft)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                play_music()
            elif pause_rect.collidepoint(event.pos):
                pause_music()
            elif next_rect.collidepoint(event.pos):
                next_track()
            elif prev_rect.collidepoint(event.pos):
                prev_track()

pygame.quit()