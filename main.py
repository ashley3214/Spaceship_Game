import pygame
import os

# Display settings
WIDTH, HEIGHT=900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('First Game')

#Background color
WHITE =(255,255,255)
BLACK =(0,0,0)

BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

#Speed it should load
FPS = 60
VEL =5
BULLET_VEL=7
MAX_BULLETS=3
SPACESHIP_WIDTH , SPACESHIP_HEIGHT= 55 , 40

YELLOW_SPACESHIP_IMAGE= pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE =pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE= pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)


def draw_window(red,yellow):
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, BLACK, BORDER)
        WIN.blit(YELLOW_SPACESHIP_IMAGE,(yellow.x,yellow.y))
        WIN.blit(RED_SPACESHIP_IMAGE,(red.x,red.y))

        pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    # moving left and right
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:# A KEY PRESSED ,moves left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:# D KEY PRESSED ,moves right
        yellow.x += VEL
    # moving up and down
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:# W KEY PRESSED ,moves up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:# S KEY PRESSED ,moves down
        yellow.y += VEL
          
def red_handle_movement(keys_pressed,red):
     # moving left and right
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:# LEFT PRESSED ,moves left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH +15:# RIGHT KEY PRESSED ,moves right
        red.x += VEL
    # moving up and down
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:# UP ARROW KEY PRESSED ,moves up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:# DOWN ARROW KEY PRESSED ,moves down
        red.y += VEL
     
     
def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets=[]
    yellow_bullets=[]


    clock = pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        # code thats been run
         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10 ,5 )
                    yellow_bullets.append(bullet)
                    

                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 - 2, 10 ,5 )
                    red_bullets.append(bullet)
        
        print(red_bullets,yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        
        draw_window(red,yellow)
    
    pygame.quit()

if __name__ == '__main__':
    main()