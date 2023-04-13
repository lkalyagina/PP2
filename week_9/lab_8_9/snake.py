import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
purple = (152, 3, 252) #объявление цветов
 
dis_width = 600 
dis_height = 400 #размеры окна игры
 
dis = pygame.display.set_mode((dis_width, dis_height)) #вывод окна на экран
pygame.display.set_caption('Snake Game') #название приложения
 
clock = pygame.time.Clock()
 
snake_block = 10 #начальный размер змейки
snake_speed = 15 #скорость передвижения змейки
 
font_style = pygame.font.SysFont("times new roman", 25)
score_font = pygame.font.SysFont("times new roman", 35) #шрифты
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])  #
 
 
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])  #отрисовка змейки
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 7, dis_height /3])  #сообщение в конце игры. Выбор между выходом и началом заново
 
 
def gameLoop():
    game_over = False
    game_close = False  #условия невыключения игры
 
    x1 = dis_width / 2
    y1 = dis_height / 2  #начальное положение змейки
    
    x1_change = 0
    y1_change = 0
 
    snake_List = []  #лист с записью всех блоков змейки
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  #рандомный выбор координат еды
 
    while not game_over:
 
        while game_close == True:
            dis.fill(purple)
            message("You Lost! Press C-Play Again or Q-Quit", red)  #условия выхода из игры
            Your_score(Length_of_snake - 1)
            pygame.display.update()  #обновление экрана
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  #присвоение кнопкам условий выхода из игры и повтора игры
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0                   #перемещение змейки влево
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0                   #перемещение змейки вправо
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0                   #перемещение змейки вверх
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0                   #перемещение змейки вниз
        
        for block in snake_List[1 :]:
            if snake_List[0] == block[0] and snake_List[1] == block[1] :
                game_over = True                    #уловия выхода если змейка тронет сама себя


        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True #условие выхода за пределы экрана(выход из игры)
        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #отрисовка еды
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update() #обновление экрана 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  
            Length_of_snake += 1   #если змейка съела еду, длина увеличивается
 
        clock.tick(snake_speed) #скорость кадров в секунду
 
    pygame.quit()
    quit()
 
gameLoop()