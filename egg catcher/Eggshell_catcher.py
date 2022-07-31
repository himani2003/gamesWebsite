#Eggs of different colours falling down
#eggs falling from fiff. positions
#bowl to be moved left right using arrow keys
#calculate lives left as eggs are dropped on ground
#calculate score when eggs are catched successfully
#show the final score

from itertools import cycle         #for colors in eggs
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
from tkinter.ttk import Style
from turtle import width

screen_width=800
screen_height=500

#creating window
window=Tk()
s=Canvas(window, width=screen_width, height=screen_height, background='sky blue')
s.create_rectangle(-10, screen_height-100, screen_width+10, screen_height+10, fill='sea green', width=0)
s.pack()

#egg parameters
color_cycle=cycle(['purple','white','hot pink','orange','maroon','black','brown'])
egg_width=50
egg_height=70
egg_score=10
egg_speed=500
egg_interval=4000
difficulty_factor=0.95

#catcher making
catcher_color='red'
catcher_width=140
catcher_height=100
catcher_start_x1=screen_width/2 - catcher_width/2
catcher_start_y1= screen_height-catcher_height-30
catcher_start_x2=catcher_start_x1+catcher_width
catcher_start_y2=catcher_start_y1+ catcher_height
catcher=s.create_arc(catcher_start_x1,catcher_start_y1,catcher_start_x2,catcher_start_y2, start=200, extent=140, style='arc', outline=catcher_color, width=5)

score = 0
score_text = s.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='black',text='Score : ' + str(score))

lives_remaning = 3
lives_text = s.create_text(screen_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='black',text='Lives : ' + str(lives_remaning))

eggs=[]

def create_eggs():
    x=randrange(10,720)
    y=40
    new_egg=s.create_oval(x,y,x+egg_width,y+egg_height, fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    window.after(egg_interval,create_eggs)

def motion_of_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = s.coords(egg)
        s.move(egg,0,15)
        if egg_y2 > screen_height:
            egg_dropped(egg)
    window.after(egg_speed,motion_of_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    s.delete(egg)
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        window.destroy()

def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    s.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))
  
def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = s.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = s.coords(egg)
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            s.delete(egg)
            increase_score(egg_score)
    window.after(100,catch_check)

def increase_score(points):
    global score , egg_speed , egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    s.itemconfigure(score_text , text='Score : ' + str(score))

def move_left(event):
    (x1,y1,x2,y2) = s.coords(catcher)
    if x1 > 0:
        s.move(catcher,-20,0)

def move_right(event):
    (x1,y1,x2,y2) = s.coords(catcher)
    if x2 < screen_width:
        s.move(catcher,20,0)

s.bind('<Left>' , move_left)
s.bind('<Right>' , move_right)
s.focus_set()

window.after(1000,create_eggs)
window.after(1000,motion_of_eggs)
window.after(1000,catch_check)

window.mainloop()