import pygame
import sys
import os
import datetime
from button import *
from image import *

os.chdir(r"C:\Users\Алексей\Desktop\KBTU\2 semester\PP2\Python_Lab07")

music_folder = "music"
playlist = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 51)
green = (0, 255, 0)
red = (255, 0, 0)

def play_music(track_index):
    pygame.mixer.music.load(playlist[track_index])
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def run():
    pygame.init()
    
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Music Player and Clock")

    pygame.mixer.init()
    global current_track
    play_music(current_track)

    music_paused = False
    isRunning = True

    pause_button = Button(x=screen_width // 2 - 45, y=screen_width - 70, width=90, height=50, text="STOP")
    previous_button = Button(x=screen_width // 2 - 105, y=screen_width - 70, width=50, height=50, text="<")
    next_button = Button(x=screen_width // 2 + 55, y=screen_width - 70, width=50, height=50, text=">")
    
    background_pic = Pic(screen, 'mickeyclock_background.png', 420, 315)
    minute_pic = Pic(screen, 'mickeyclock_minute.png', 420, 315)
    second_pic = Pic(screen, 'mickeyclock_second.png', 420, 315)
    center_pic = Pic(screen, 'mickeyclock_center.png', 420, 315)

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYUP:
                print(f'Pressed the {pygame.key.name(event.key)} key')

                if event.key == pygame.K_UP:
                    pygame.mixer.music.unpause()
                    pause_button.text = "STOP"
                    pause_button.color = red
                    music_paused = False
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.pause()
                    pause_button.text = "PLAY"
                    pause_button.color = green
                    music_paused = True

                elif event.key == pygame.K_LEFT:
                    current_track = (current_track - 1) % len(playlist)
                    play_music(current_track)

                elif event.key == pygame.K_RIGHT:
                    current_track = (current_track + 1) % len(playlist)
                    play_music(current_track)

            if pause_button.is_clicked(event):
                if music_paused:
                    pygame.mixer.music.unpause()
                    pause_button.text = "STOP"
                    pause_button.color = red
                else:
                    pygame.mixer.music.pause()
                    pause_button.text = "PLAY"
                    pause_button.color = green
                music_paused = not music_paused

            if previous_button.is_clicked(event):
                current_track = (current_track - 1) % len(playlist)
                play_music(current_track)

            if next_button.is_clicked(event):
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)

        time_now = datetime.datetime.now()

        minutes = time_now.minute
        seconds = time_now.second

        minute_angle = (minutes / 60) * 360
        second_angle = (seconds / 60) * 360

        minute_pic.rotate(minute_angle)
        second_pic.rotate(second_angle)

        screen.fill(black)
        pygame.draw.rect(screen, green, pygame.Rect(30, 85, 440, 335))
        background_pic.output()
        minute_pic.output()
        second_pic.output()
        center_pic.output()
        pause_button.draw(screen)
        previous_button.draw(screen)
        next_button.draw(screen)

        font = pygame.font.Font(None, 36)
        time_text = font.render(time_now.strftime("%H:%M:%S"), True, red)
        screen.blit(time_text, (10, 10))

        pygame.display.flip()

run()