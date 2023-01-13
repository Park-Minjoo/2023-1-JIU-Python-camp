import pygame

pygame.init()

# making display
screen_width = 480 #
screen_height = 640 #
screen = pygame.display.set_mode((screen_width, screen_height))

# Title of the game
pygame.display.set_caption("Euijin Ahn")

# FPS
clock = pygame.time.Clock()

# background
background = pygame.image.load("/Users/ahn_euijin/Desktop/python_workspace/pygame_basic/background.png")

# character
character = pygame.image.load("/Users/ahn_euijin/Desktop/python_workspace/pygame_basic/character.png")
character_size = character.get_rect().size # get a size of the image
character_width = character_size[0] #  width
character_height = character_size[1] # hight

#where to put my character
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# moving coordinates
to_x = 0
to_y = 0

# moving speed
character_speed = 0.6

# # enemy
# enemy = pygame.image.load("/users/ahn_euijin/desktop/python_workspace/pygame_basic/enemy.png")
# enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
# enemy_width = enemy_size[0] # 캐릭터의 가로 크기
# enemy_height = enemy_size[1] # 캐릭터의 세로 크기
# enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
# enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
# # 겹치지 않게 하기 위해서 적을 올린다.
# # 그 다음에 그려줘야 한다. blit


# event loop
running = True
while running:
    dt = clock.tick(60) # frame per second
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # key event
            if event.key == pygame.K_LEFT:
                to_x -= character_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # released the key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    #update the position
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # width boundary
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #  height boundary
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # # crash information for character
    # character_rect = character.get_rect()
    # character_rect.left = character_x_pos
    # character_rect.top = character_y_pos
    # # crash informarion for enemy
    # enemy_rect = enemy.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos
    #
    # # crashed check
    # if character_rect.colliderect(enemy_rect): #colliderect를 하면 괄호 안에 있는 것과 충돌을 하는가를 확인
    #     print("It has been crashed")
    #     running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    # screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()