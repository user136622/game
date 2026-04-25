import pygame

width = 800
height = 600
pad_width = 15
pad_height = 90
ball_size = 20
FPS = 60
score = 0

black = (0, 0, 0)
blue = (173, 216, 34)
green = (34, 139, 34)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

ball = pygame.Rect(width//2, height//2, ball_size, ball_size)
ball_speed_x = 5
ball_speed_y = 5
player1 = pygame.Rect(50, height//2 - pad_height//2, pad_width, pad_height)
player2 = pygame.Rect(width - 50 - pad_width, height//2 - pad_height//2, pad_width, pad_height)
pad_speed = 7

#cycle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w] and player1.top > 0: 
        player1.y -= pad_speed
    if keys[pygame.K_s] and player1.bottom < height: 
        player1.y +- pad_speed
    if keys[pygame.K_UP] and player2.top > 0: 
        player2.y -= pad_speed
    if keys[pygame.K_DOWN] and player2.bottom < height: 
        player2.y +- pad_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        score += 1

    if ball.left <= 0 or ball.right >= width:
        print(f'Game over, score: {score}')
        pygame.quit()
        
        screen.fill(blue)
        pygame.draw.rect(screen, black, player1)
        pygame.draw.rect(screen, black, player2)
        pygame.draw.ellipse(screen, (green), ball)

        score_text = font.render(f'Score: {score}', True, black)
        screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(FPS)