import pygame
pygame.init()
monitor=pygame.display.set_mode((500,300))
pygame.display.set_caption("Music Player")
#pygame.display.set_icon(pygame.image.load(""))
songs = ['Imagine Dragons - Believer.mp3', 'Imagine Dragons - Birds.mp3', 
         'Imagine Dragons - Natural.mp3', 'Imagine Dragons - Sharks.mp3']
current_song = 0

pygame.mixer.music.load(songs[current_song])

playing = True

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False


            if event.key == pygame.K_RIGHT:
                current_song+=1
 
            if event.key == pygame.K_LEFT:
                current_song-=1                
            
            if current_song >= len(songs):
                current_song = 0 

            pygame.mixer.music.load(songs[current_song])
            pygame.mixer.music.play()   

    font = pygame.font.Font(None, 36)
    text = font.render('Playing' if playing else 'Paused', True, (250, 250, 250))
    monitor.blit(text, (50, 50))
    pygame.display.update()
    