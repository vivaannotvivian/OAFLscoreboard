
import pygame


pygame.init()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
 

X = 800
Y = 150
 

display_surface = pygame.display.set_mode((X, Y))
 

pygame.display.set_caption('OAFL Scoreboard')
 
font = pygame.font.Font('freesansbold.ttf', 100)
font_small = pygame.font.Font('freesansbold.ttf', 50)


text = font.render("AYO  ", True, white, green)
josh_text = font.render("JOSH", True, white, green)

textRect = text.get_rect()
josh_textRect = text.get_rect()

down_select = 0
down_text = ["1st Down", "2nd Down", "3rd Down", "4th Down", ""]
down_font = font_small.render(down_text[down_select], True, white, green)
down_font_Rect = down_font.get_rect()
down_font_Rect.center = (385,25)

textRect.center = (132, 100)
josh_textRect.center = (650,100)
josh_score= 1
score_text = 1
score = font.render(str(score_text), True, white, blue)
josh_score_text = font.render(str(josh_score), True, white, blue)
josh_score_text_Rect = text.get_rect()
josh_score_text_Rect.center = (525,100)
scoreRect = text.get_rect()
scoreRect.center = (400, 100)
print(X // 2 +200)
print(Y // 2)
#AYO X and Y = 132, 50
#AYO Score  = 400, 500


while True:
 

    display_surface.fill(blue)
    down_font = font_small.render(down_text[down_select], True, white, green)

    display_surface.blit(down_font, down_font_Rect)
    score = font.render(str(score_text), True, white, blue)
    josh_score_text = font.render(str(josh_score), True, white, blue)
    display_surface.blit(text, textRect)
    display_surface.blit(score, scoreRect)
    display_surface.blit(josh_text, josh_textRect)
    display_surface.blit(josh_score_text,josh_score_text_Rect)
    
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_e:
                score_text = score_text + 1 
                print(score_text)
            if event.key == pygame.K_w:
                score_text = score_text - 1
                print(score_text)
            if event.key == pygame.K_p:
                josh_score = josh_score + 1
                print(josh_score)
            if event.key == pygame.K_o:
                josh_score = josh_score - 1
                print(score_text)
            if event.key == pygame.K_b:
                down_select = down_select + 1
                print(down_select)
                if down_select >= 5:
                    down_select = 0

        if event.type == pygame.QUIT:
 

            pygame.quit()
 

            quit()
 
        pygame.display.update()
