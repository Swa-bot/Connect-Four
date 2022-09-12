import pygame
pygame.init()
#Note: red is player and green is computer
class pieces:
    def __init__(self,xPos,yPos,red,green):
        self.x = xPos
        self.y = yPos
        self.xPos = self.x*100+100
        self.yPos = self.y*100+100
        self.red = red
        self.green = green
        self.avoid = False
   
    def win(self):
        count = 0
        for x in range(4):
            if board[self.y][x].red == 255:
                count = count+1
       
        if count == 4:
            return True
 
        count = 0
        for y in range(4):
            if board[y][self.x].red==255:
                count = count+1
 
        if count == 4:
            return True
        count = 0
        for pos in range(4):
            if board[pos][pos].red == 255:
                count = count+1
        if count ==4:    
            return True
        count = 0
        for pos in range(4):
            if board[3-pos][pos].red == 255:
                count = count + 1
        if count ==4:
            return True
        return False
 
    def accessible(self):
        if self.y == 3:
            return True
        if board[self.y+1][self.x].red == 255 or board[self.y+1][self.x].green == 255:
            return True
        return False
 
def get_input(mx):
    if mx>100 and mx<200:
        for y in range(4):
            if board[3-y][0].red == 0 and board[3-y][0].green == 0:
                board[3-y][0].red = 255
                Y = 3-y
                X = 0
                return Y,X;
 
    if mx>=200 and mx<300:
        for y in range(4):
            if board[3-y][1].red == 0 and board[3-y][1].green == 0:
                board[3-y][1].red = 255
                Y = 3-y
                X = 1
                return Y,X;
 
    if mx>=300 and mx<400:
        for y in range(4):
            if board[3-y][2].red == 0 and board[3-y][2].green == 0:
                board[3-y][2].red = 255
                Y = 3-y
                X = 2
                return Y,X;
 
    if mx>=400 and mx<500:
        for y in range(4):
            if board[3-y][3].red == 0 and board[3-y][3].green == 0:
                board[3-y][3].red = 255
                Y = 3-y
                X = 3
                return Y,X;
 
    return -1,-1;
 
def comp_win():
    for x in range(4):
        count = 0
        for y in range(4):
            if board[y][x].green == 255:
                count = count +1
            if board[y][x].red == 255:
                count-=1
        if count == 3:
            board[y][x].green = 255
            return True
    return False
 
    for y in range(4):
        count = 0
        pVals = []
        for x in range(4):
            if board[y][x].green == 255:
                count = count +1
            elif board[y][x].red == 0:
                pVals.append(y)
                pVals.append(x)
        if len(pVals)>0 and count ==3 and board[pVals[0]][pVals[1]].accessible():
             board[pVals[0]][pVals[1]].green =255
             return True;
   
    for pos in range(4):
        count = 0
        pVals = []
        if board[pos][pos].green == 255:
            count = count+1
        elif board[pos][pos].red == 0:
            pVals.append(pos)
        if len(pVals)>0 and count==3 and board[pVals[0]][pVals[0]].accessible():
            board[pVals[0]][pVals[0]].green = 255
            return True;
 
   
    for pos in range(4):
        count = 0
        pVals = []
        if board[3-pos][pos].green == 255:
            count = count+1
        elif board[3-pos][pos].red == 0:
            pVals.append(3-pos)
            pVals.append(pos)
        if len(pVals)>0 and count==3 and board[pVals[0]][pVals[1]].accessible():
            board[pVals[0]][pVals[1]]
            return True;
    return False;
   ###
def threeRow():
    for x in range(4):
        count = 0
        for y in range(4):
            if board[y][x].red == 255:
                count+=1
            elif board[y][x].green == 255:
                count-=1
        if count == 3:
            board[0][x].green = 255
            return True;
 
    for y in range(4):
        count = 0
        pVals = []
        for x in range(4):
            if board[y][x].red == 255:
                count +=1
            elif board[y][x].green == 0:
                pVals.append(y)
                pVals.append(x)
        if len(pVals)>0 and count ==3 and board[pVals[0]][pVals[1]].accessible():
            board[pVals[0]][pVals[1]].green = 255
            return True;
        if len(pVals)>0 and not board[pVals[0]][pVals[1]].accessible() and count ==3:
            board[pVals[0]+1][pVals[1]].avoid = True

    count = 0

    for pos in range(4):
        pVals = []
        if board[pos][pos].red == 255:
            count = count+1
        elif board[pos][pos].green == 0:
            pVals.append(pos)
        if len(pVals)>0 and count==3 and board[pVals[0]][pVals[0]].accessible():
            board[pVals[0]][pVals[0]].green = 255
            return True;
        if len(pVals)>0 and not board[pVals[0]][pVals[0]].accessible() and count ==3:
            board[pVals[0]+1][pVals[0]].avoid = True
    count = 0

    for pos in range(4):
        pVals = []
        print(count)
        if board[3-pos][pos].red == 255:
            count = count+1
        elif board[3-pos][pos].green == 0:
            pVals.append(3-pos)
            pVals.append(pos)
        if len(pVals)>0 and count==3 and board[pVals[0]][pVals[1]].accessible():
            board[pVals[0]][pVals[1]].green = 255
            return True;
        if len(pVals)>0 and not board[pVals[0]][pVals[1]].accessible() and count ==3:
            board[pVals[0]+1][pVals[1]].avoid = True
    return False;
 
def twoRow():
    for y in range(4):
        count = 0
        pVals = []
        for x in range(4):
            if board[y][x].red == 255:
                count = count +1
            elif board[y][x].green == 0:
                pVals.append(y)
                pVals.append(x)
        if len(pVals)>0 and count ==2 and board[pVals[0]][pVals[1]].accessible() and board[pVals[0]][pVals[1]].avoid == False:
            board[pVals[0]][pVals[1]].green = 255
            return True
   
    for pos in range(4):
        count = 0
        pVals = []
        if board[pos][pos].red == 255:
            count = count+1
        elif board[pos][pos].green == 0:
            pVals.append(pos)
        if len(pVals)>0 and count==2 and board[pVals[0]][pVals[0]].accessible() and board[pVals[0]][pVals[1]].avoid == False:
            board[pVals[0]][pVals[0]].green = 255
            return True;
   
    for pos in range(4):
        count = 0
        pVals = []
        if board[3-pos][3-pos].red == 255:
            count = count+1
        elif board[3-pos][pos].green == 0:
            pVals.append(3-pos)
        if len(pVals)>0 and count==2 and board[pVals[0]][pVals[1]].accessible() and board[pVals[0]][pVals[1]].avoid == False:
            board[pVals[0]][pVals[1]].green = 255
            return True
    for x in range(4):
        count = 0
        for y in range(4):
            if board[y][x].red == 255:
                count = count +1
            elif board[y][x].green == 255:
                count-=1
        if  len(pVals)>0 and count == 2 and board[pVals[0]][pVals[1]].avoid == False:
            board[y][x].green = 255
            return True;
    return False;
 
def comp_play():
    pVals = []
    for y in range(4):
        for x in range(4):
            if board[3-y][x].red == 0 and board[3-y][x].green ==0  and board[3-y][x].accessible():
                if len(pVals)<1:
                    pVals.append(3-y)
                    pVals.append(x)
                if board[3-y][x].avoid ==False:
                    board[3-y][x].green = 255
                    return
    if len(pVals)>0:
        board[pVals[0]][pVals[1]].green = 255

board = []
for yPos in range(4):
    row = []
    for xPos in range(4):
        row.append(pieces(xPos,yPos,0,0))
    board.append(row)
 
pygame.display.set_caption("Connect Four")
 
pieceX=pieceY = 0
 
run = True

event_occur = False
while run:
    win = pygame.display.set_mode((500,500))
    pygame.time.delay(100)
   
    pygame.draw.rect(win,(0,0,255),(50,50,400,400))
 
    for x in range(4):
        for y in range(4):
            pygame.draw.circle(win,(board[x][y].red,board[x][y].green,0),(board[x][y].xPos,board[x][y].yPos),30)
 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            event_occur = True
            mx, my = pygame.mouse.get_pos()
            pieceY,pieceX = get_input(mx)
 
    if pieceY!= -1 and event_occur == True:
        if board[pieceY][pieceX].win():
            print("You WIN!!!")
            pygame.quit()
       
        if comp_win():
            print("You Lose!")
            pygame.quit()
        if not threeRow():
            if not twoRow():
                comp_play()
        event_occur = False

 
    pygame.display.update()
 
