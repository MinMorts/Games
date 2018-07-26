from Tkinter import *
import time
import random
root = Tk()

#size of window
w = 600
h = 450
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w)/2
y = (sh - h)/2
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#playing frame, with Canvas inside
canvframe = Frame(relief=SUNKEN, width=600, height = 350, background="black")
canvframe.pack()

canv = Canvas(canvframe, background="black", width=600, height = 350)
canv.pack(fill=NONE)

# Objects in canvas           
ball = canv.create_oval(295,170,305,180, outline="white", fill="white", width=2, tags=('ball'))
paddle1 = canv.create_rectangle(0,215,10,135, outline="white", fill="white", width=2, tags=('paddle1'))
paddle2 = canv.create_rectangle(590,215,600,135, outline="white", fill="white", width=2)
line = canv.create_line(300, 0, 300, 350, fill = "grey", width=2)
centre = canv.create_oval(270, 145, 330, 205, outline="grey", fill="")
canv.tag_raise(ball)
        
#Paddle movement      
def moveUp1(*args):
    canv.move(paddle1, 0, -15)        
def moveUp2(*args):
    canv.move(paddle2, 0, -15)        
def moveDown1(*args):
    canv.move(paddle1, 0, 15)        
def moveDown2(*args):
    canv.move(paddle2, 0, 15)    
def NoMove(*args):    
    canv.move(paddle2, 0, 0) 

#InitialVelocity
dx = 0
dy = 0

#initial score
Player1score = 0
Player2score = 0
Scorer = "First to 3 goals wins!"
#gameover state
gameover = True

#start game - what happens when you push start button (reset velocity and scores)
def startgame(*args):
    global dy, dx, Player1score, Player2score, gameover
    if gameover==False:
        gameover=True
        root.after(15, startgame)
    else:
        canv.coords(ball, 295,170,305,180)
        canv.coords(paddle1, 0,215,10,135)
        canv.coords(paddle2, 590,215,600,135)
        randomStart = random.randint(1, 2)    
        if randomStart == 1:
            dx = 6
            dy = 0
        else:
            dx = -6
            dy = 0
        Player1score = 0
        Player2score = 0
        Player1scoreLabel.configure(text="Player 1 score: "+ str(Player1score))
        Player2scoreLabel.configure(text="Player 2 score: "+ str(Player2score))
        gameover = False
        moveBall()
    
#Ball Movement
def moveBall():
    global dy, dx, Player1score, Player2score, gameover
#    to make ball bounce off paddle 1
    if canv.coords(ball)[0]<=canv.coords(paddle1)[2] and canv.coords(paddle1)[1]<= canv.coords(ball)[1] <= canv.coords(paddle1)[3]:        
        dx = -dx
        if canv.coords(paddle1)[1] <= canv.coords(ball)[1] <= (int((canv.coords(paddle1)[1] + canv.coords(paddle1)[3])) / 2 ):
            dy -=1
            canv.move(ball, dx, dy)
        elif (int(canv.coords(paddle1)[1] + canv.coords(paddle1)[3]) / 2 ) <= canv.coords(ball)[3] <= canv.coords(paddle1)[3]:
            dy += 1
            canv.move(ball, dx, dy)
        else:
            canv.move(ball, dx, dy)
#to make ball bounce off paddle 2
    elif canv.coords(ball)[2]>=canv.coords(paddle2)[0] and canv.coords(paddle2)[1]<= canv.coords(ball)[3] <= canv.coords(paddle2)[3]:
        dx = -dx
        if canv.coords(paddle2)[1] <= canv.coords(ball)[1] <= (int((canv.coords(paddle2)[1] + canv.coords(paddle2)[3])) / 2 ):
            dy -= 1
            canv.move(ball, dx, dy)
        elif (int(canv.coords(paddle2)[1] + canv.coords(paddle2)[3])/ 2 ) <= canv.coords(ball)[3] <= canv.coords(paddle2)[3]:
            dy += 1
            canv.move(ball, dx, dy)
        else:
            canv.move(ball, dx, dy)
#to make ball bounce off roof
    elif canv.coords(ball)[1]<=0:
        dy = -dy
        canv.move(ball, dx, dy)
#to make ball bounce of floor
    elif canv.coords(ball)[3]>=350:
        dy = -dy
        canv.move(ball, dx, dy)
#if player 2 scores
    elif canv.coords(ball)[2]<=0:
        Scorer = "GOOOALLL!!!! Player 2 scored!"
        ScoreLabel.configure(text=Scorer)
        Player2score += 1
        Player2scoreLabel.configure(text="Player 2: score"+ str(Player2score))
        canv.coords(ball, 295,170,305,180)
        canv.coords(paddle1, 0,215,10,135)
        canv.coords(paddle2, 590,215,600,135)
        dx=6
        dy=0
        time.sleep(0.5)
#if player1 scores
    elif canv.coords(ball)[0]>=600:
        Scorer = "GOOOALLL!!!! Player 1 scored!"
        ScoreLabel.configure(text=Scorer)
        Player1score += 1
        Player1scoreLabel.configure(text="Player 1 score: "+ str(Player1score))
        canv.coords(ball, 295,170,305,180)
        canv.coords(paddle1, 0,200,10,120)
        canv.coords(paddle2, 590,200,600,120)
        dx=-6
        dy=0
        time.sleep(0.5)
#end game if player 1 or 2 wins
    elif Player1score==3 or Player2score==3:
        dx=0
        dy=0
        if Player1score==3:
            Scorer = "Player 1 is the winner! Press start to play again or quit to leave!"
            ScoreLabel.configure(text=Scorer)
        elif Player2score==3:
            Scorer = "Player 2 is the winner! Press start to play again or quit to leave!"
            ScoreLabel.configure(text=Scorer)
        gameover = True
#move ball if nothing happens
    else:        
        canv.move(ball, dx, dy)
    if not gameover:
#        AIPlayer()
        canv.after(10, moveBall)
        
def exitGame(*args):
    root.destroy()

#def AIPlayer():
#    if (canv.coords(paddle2)[1] + canv.coords(paddle2)[3]) / 2 <= (canv.coords(ball)[1] + canv.coords(ball)[3])/2:
#        moveDown2()
#    elif (canv.coords(paddle2)[1] + canv.coords(paddle2)[3]) / 2 >= ((canv.coords(ball)[1] + canv.coords(ball)[3])/2):
#        moveUp2()
    
#buttons
Butframe = Frame(relief=SUNKEN, width=200, height = 150, background="white")
Butframe.pack(fill=X)
startButton = Button(Butframe, text="Start", command = startgame)
startButton.pack(side = TOP)
quitButton = Button(Butframe, text="Quit", command = exitGame)
quitButton.pack(side = TOP)
ScoreLabel = Label(Butframe, text = Scorer, background = "red", font = ("Arial", "12", "bold"))
ScoreLabel.pack(side=BOTTOM, fill = X)

#scores
Player1scoreLabel = Label(Butframe, text="Player 1 score: "+ str(Player1score), background="green", font = ("Arial", "11", "bold"))
Player1scoreLabel.pack(side = LEFT, fill = X)
Player2scoreLabel = Label(Butframe, text="Computer score: "+ str(Player2score), background="green", font = ("Arial", "11", "bold"))
Player2scoreLabel.pack(side = RIGHT, fill = X)

#binding of movement keys    
root.bind("<Up>", moveUp2)
root.bind("<w>", moveUp1)
root.bind("<Down>", moveDown2)
root.bind("<s>", moveDown1)
root.bind("<space>", startgame)
root.bind("<Escape>", exitGame)
root.mainloop()