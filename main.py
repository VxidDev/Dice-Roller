import tkinter as tk 
from random import randint

# window setup
window = tk.Tk()
window.geometry("300x400")
window.resizable(width=False , height=False)
window.title("Dice Roller")

# loading images
# dice_list
dice_list = []

for i in range(1, 7):
    img = tk.PhotoImage(file=f"Assets/dice_{i}.png").subsample(5, 5)
    dice_list.append(img)

# GUI
dice_label = tk.Label()
dice_label.place(x=95 , y=50)

random_button = tk.Button(width=10 , height=3 , text="Roll" , font=("arial" , 10 , "bold") , command=lambda: roll_dice() , activebackground="gray")
random_button.place(x=105 , y=250)

# App logic
def roll_dice():
    dice = dice_list[randint(0 , 5)]
    dice_label.config(image=dice)

roll_dice()  # initial roll

window.mainloop()
