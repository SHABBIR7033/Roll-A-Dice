import tkinter as tk
import random
from PIL import Image, ImageTk


root = tk.Tk()
root.title("🎲 Dice Roller")
root.geometry("400x400")
root.configure(bg="#f8f9fa")


dice_images = [
    "dice1.png",
    "dice2.png",
    "dice3.png",
    "dice4.png",
    "dice5.png",
    "dice6.png"
]


dice_img = ImageTk.PhotoImage(Image.open(random.choice(dice_images)).resize((100, 100)))
dice_label = tk.Label(root, image=dice_img, bg="#f8f9fa")
dice_label.pack(pady=40)


def roll_dice():
    new_img = ImageTk.PhotoImage(Image.open(random.choice(dice_images)).resize((100, 100)))
    dice_label.configure(image=new_img)
    dice_label.image = new_img  


title_label = tk.Label(root, text="Click the Button to Roll the Dice!", 
                       font=("Helvetica", 16, "bold"), bg="#f8f9fa", fg="#333")
title_label.pack(pady=10)


roll_button = tk.Button(root, text="Roll Dice 🎲", command=roll_dice, 
                        font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", 
                        padx=15, pady=8, relief="raised", cursor="hand2")
roll_button.pack(pady=20)


root.mainloop()
