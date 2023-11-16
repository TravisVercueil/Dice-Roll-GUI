#Imports we use
from tkinter import *
import secrets
from  PIL import ImageTk, Image
import os
#Initialize our Window
root = Tk()
root.geometry("500x600")

#Title of Window
root.title("Dice Roller")

dice_total = StringVar()
output_dice1 = StringVar()
output_dice2 = StringVar()



def RollDice():
    dice1 = secrets.randbelow(6) +1
    dice2 = secrets.randbelow(6) +1
    total = dice1 + dice2
    dice_total.set(total)
    output_dice1.set(dice1)
    output_dice2.set(dice2)
    UpdateImage(dice1,dice2)

def UpdateImage(dice1,dice2):
    rolled_dice = [dice1,dice2]
    
    new_first_image_path = os.path.join(os.path.dirname(__file__), "./{}.png".format(rolled_dice[0])) 
    new_second_image_path = os.path.join(os.path.dirname(__file__), "./{}.png".format(rolled_dice[1])) 

    new_first_dice_image =ImageTk.PhotoImage(Image.open(new_first_image_path))
    new_second_dice_image =ImageTk.PhotoImage(Image.open(new_second_image_path))

    first_dice_label.configure(image = new_first_dice_image)
    second_dice_label.configure(image = new_second_dice_image)

    first_dice_label.image = new_first_dice_image
    second_dice_label.image = new_second_dice_image
    
dice_heading = Label(root, text= 'Dice Roller', font = 'arial 14 bold').pack(pady=15)
Button(root, text="Roll Dice", command= RollDice, font="arial 12 bold", bg='white', fg='Black', activebackground="teal", padx=5, pady=5 ).pack(pady=20)

dice_label = Label(root, text='Randomly Rolled Die', font='arial 14 bold').pack(pady="30 10")
Entry(root, textvariable= dice_total, width=24,font='arial 16').pack()

first_image_path = os.path.join(os.path.dirname(__file__), "./0.png")
second_image_path = os.path.join(os.path.dirname(__file__), "./0.png")

first_dice_image = ImageTk.PhotoImage(Image.open(first_image_path))
first_dice_label = Label(root, image = first_dice_image)
first_dice_label.pack()

second_dice_image = ImageTk.PhotoImage(Image.open(second_image_path))
second_dice_label = Label(root, image = second_dice_image)
second_dice_label.pack()



root.mainloop()

