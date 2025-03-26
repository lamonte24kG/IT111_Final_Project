import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import random

# ----------------------- Game Logic -----------------------
def determine_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You Win!"
    else:
        return "You Lose!"

# ----------------------- GUI Setup -----------------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x500")
root.configure(bg='white')

# Load images
rock_img = ImageTk.PhotoImage(Image.open("images/rock.png").resize((150, 150)))
print("rock.png loaded")
paper_img = ImageTk.PhotoImage(Image.open("images/paper.png").resize((150, 150)))
print("paper.png loaded")
scissors_img = ImageTk.PhotoImage(Image.open("images/scissors.png").resize((150, 150)))
print("scissors.png loaded")

# Image map for cleaner code
image_map = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}

# Layout configuration
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Labels
Label(root, text="Your Choice", font=("Helvetica", 18, "bold"), bg='white').grid(row=0, column=1, pady=10)
player_img = Label(root, image=rock_img, bg='white')
player_img.grid(row=1, column=0, padx=30)
computer_img = Label(root, image=paper_img, bg='white')
computer_img.grid(row=1, column=2, padx=30)
result_label = Label(root, text="Computer: ", font=("Helvetica", 18), bg='white', fg='blue')
result_label.grid(row=2, column=1, pady=20)

# ----------------------- Game Function -----------------------
def play(choice):
    computer = random.choice(["rock", "paper", "scissors"])
    self.round_count += 1

    player_img.config(image=image_map[choice])
    computer_img.config(image=image_map[computer])

    result = determine_winner(choice, computer)
    result_label.config(text=f"Computer: {computer.capitalize()} | {result}")

 # Score and Round Labels
        self.score_label = Label(self.root, text=f"You: {self.player_score}  |  Computer: {self.computer_score}", 
                                 font=("Helvetica", 16), bg='white')
        self.score_label.grid(row=4, column=1, pady=10
# Buttons
Button(root, text="Rock", command=lambda: play("rock"), width=12, height=2).grid(row=3, column=0, pady=20, padx=10)
Button(root, text="Paper", command=lambda: play("paper"), width=12, height=2).grid(row=3, column=1, pady=20, padx=10)
Button(root, text="Scissors", command=lambda: play("scissors"), width=12, height=2).grid(row=3, column=2, pady=20, padx=10)


 # Reset Button
        self.reset_button = Button(root, text="Reset Game", command=self.reset_game, width=12, height=2, state=tk.DISABLED)
        self.reset_button.grid(row=3, column=0, pady=20)

# Start the app
root.mainloop()
