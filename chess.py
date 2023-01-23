import pygame
black_pawn=pygame.image.load("black_pawn.png")
black_rook=pygame.image.load("black_rook.png")
black_knight=pygame.image.load("black_knight.png")
black_bishop=pygame.image.load("black_bishop.png")
black_queen=pygame.image.load("black_queen.png")
black_king=pygame.image.load("black_king.png")



white_pawn=pygame.image.load("white_pawn.png")
white_rook=pygame.image.load("white_rook.png")
white_knight=pygame.image.load("white_knight.png")
white_bishop=pygame.image.load("white_bishop.png")
white_queen=pygame.image.load("white_queen.png")
white_king =pygame.image.load("white_king.png")

pygame.init()
chess_board=[["black_rook","black_knight","black_bishop","black_queen","black_king","black_bishop","black_knight","black_rook"],
            ["black_pawn"]*8,
            [""]*8,
            [""]*8,
            [""]*8,
            [""]*8,
            ["white_pawn"]*8,
            ["white_rook","white_knight","white_bishop","white_queen","white_king","white_bishop","white_knight","white_rook"]]

pygame.display.set_caption("chess")
black_square=(0,0,0)
light_square=(255,255,255)


screen = pygame.display.set_mode((800, 800))
for row in range(8):
    for col in range(8):
        if (row+col)%2==0:
            square_color=light_square
        else:
            square_color=black_square
        pygame.draw.rect(screen,square_color,(row*100,col*100,100,100))
        
for row in range(8):
    for col in range(8):
        if row==1:
            screen.blit(black_pawn,(col*100,100))
        if row==0:
            if col==0 or col==7:
                screen.blit(black_rook,(col*100,row*100))
            if col==1 or col==6:
                screen.blit(black_knight,(col*100,row*100))
            if col==2 or col==5:
                #bishop
               screen.blit(black_bishop,(col*100,row*100))
            if col==3:
                #queen
                screen.blit(black_queen,(col*100,row*100))
            if col==4:
                #king
                screen.blit(black_king,(col*100,row*100))
        if row==6:
            screen.blit(white_pawn,(col*100,row*100))
        if row==7:
                if col==0 or col==7:
                    screen.blit(white_rook,(col*100,row*100))
                if col==1 or col==6:
                    screen.blit(white_knight,(col*100,row*100))
                if col==2 or col==5:
               
                    screen.blit(white_bishop,(col*100,row*100))
                if col==3:
                
                    screen.blit(white_queen,(col*100,row*100))
                if col==4:
                    screen.blit(white_king,(col*100,row*100))

pygame.display.update()        
rows=-1
  
selected=False

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                new_x,new_y=event.pos
                if chess_board[int(new_y/100)][int(new_x/100)] != "" and selected==False:
                    selected=True
                    x,y=new_x,new_y
                elif selected==True:
                    
                    
                    if new_x != x and new_y!=y:
                        chess_board[int(new_y/100)][int(new_x/100)]=chess_board[int(y/100)][int(x/100)]
                        chess_board[int(y/100)][int(x/100)]=""
                        selected=False
                    for row in chess_board:
                        rows+=1
                        cols=-1
                        for col in row:
                            cols+=1
                            if col!="":
                                image=col+".png"
                                pieces=pygame.image.load(image)
                                screen.blit(pieces,(cols*100,rows*100))
                            else:
                                if(rows+cols)%2==0:
                                    square_color=light_square
                                else:
                                    square_color=black_square
                                pygame.draw.rect(screen,square_color,(cols*100,rows*100,100,100))            
                    rows=-1   
                print(chess_board[0][0][0])
    pygame.display.update()
pygame.quit()




    
    
    