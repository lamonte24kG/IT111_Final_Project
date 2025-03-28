import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import random

# ----------------------- Global Variables ------------------
player1_score = 0
player2_score = 0
player_score = 0        # For single player (self)
computer_score = 0      # For single player (computer)
round_count = 0
current_mode = "menu"  # Tracks which mode is active

# ----------------------- Game Logic -----------------------
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a Tie!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 Wins!"
    else:
        return "Player 2 Wins!"

# ----------------------- GUI Setup -----------------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x600")
root.configure(bg='white')

rock_img = ImageTk.PhotoImage(Image.open("images/rock.png").resize((150, 150)))
paper_img = ImageTk.PhotoImage(Image.open("images/paper.png").resize((150, 150)))
scissors_img = ImageTk.PhotoImage(Image.open("images/scissors.png").resize((150, 150)))

image_map = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

player1_label = Label(root, text="Player 1", font=("Helvetica", 18, "bold"), bg="white")
player1_label.grid(row=0, column=0)

player2_label = Label(root, text="Player 2", font=("Helvetica", 18, "bold"), bg="white")
player2_label.grid(row=0, column=2)

player1_img = Label(root, image=rock_img, bg='white')
player1_img.grid(row=1, column=0)
player2_img = Label(root, image=paper_img, bg='white')
player2_img.grid(row=1, column=2)

result_label = Label(root, text="Choose a Mode to Start", font=("Helvetica", 18), bg='white', fg='blue')
result_label.grid(row=2, column=1, pady=10)

score_label = Label(root, text="Scoreboard", font=("Helvetica", 14), bg='white', fg='blue')
score_label.grid(row=3, column=1)

player1_score_label = Label(root, text="Player 1: 0", font=("Helvetica", 14), bg='white', fg='blue')
player1_score_label.grid(row=3, column=0)
player2_score_label = Label(root, text="Player 2: 0", font=("Helvetica", 14), bg='white', fg='blue')
player2_score_label.grid(row=3, column=2)

# ----------------------- Helpers -------------------------
def update_scores(winner):
    global player1_score, player2_score, player_score, computer_score
    if current_mode == "single":
        if "Player 1 Wins" in winner:
            player_score += 1
        elif "Player 2 Wins" in winner:
            computer_score += 1
        score_label.config(text=f"You: {player_score}  |  Computer: {computer_score}")
    elif current_mode == "multi":
        if "Player 1 Wins" in winner:
            player1_score += 1
        elif "Player 2 Wins" in winner:
            player2_score += 1
        player1_score_label.config(text=f"Player 1: {player1_score}")
        player2_score_label.config(text=f"Player 2: {player2_score}")

def clear_buttons(rows=[3, 4, 5]):
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) in rows and isinstance(widget, Button):
            widget.destroy()

def show_play_again_button():
    Button(root, text="Play Again", command=choose_mode, width=16, height=3).grid(row=5, column=1, pady=20)

# ----------------------- Game Logic -------------------------
def play_single(choice):
    global round_count, current_mode
    current_mode = "single"
    computer = random.choice(["rock", "paper", "scissors"])
    round_count += 1

    player1_img.config(image=image_map[choice])
    player2_img.config(image=image_map[computer])

    result = determine_winner(choice, computer).replace("Player 1", "You").replace("Player 2", "Computer")
    result_label.config(text=f"Computer: {computer.capitalize()} | {result}")
    update_scores(result.replace("You", "Player 1").replace("Computer", "Player 2"))

    # Prompt to keep playing
    result_label.after(1000, lambda: result_label.config(text="Choose Rock, Paper, or Scissors"))
    result_label.after(1000, show_play_again_button)

def play_multiplayer(player1_choice):
    global current_mode
    current_mode = "multi"

    def player2_choice_handler(player2_choice):
        player1_img.config(image=image_map[player1_choice])
        player2_img.config(image=image_map[player2_choice])

        result = determine_winner(player1_choice, player2_choice)
        result_label.config(text=f"Result: {result}")
        update_scores(result)

        result_label.after(1000, lambda: result_label.config(text="Player 1, make your choice!"))
        result_label.after(1000, show_player1_buttons)

    clear_buttons(rows=[3])
    result_label.config(text="Player 2, make your choice!")

    Button(root, text="Rock", command=lambda: player2_choice_handler("rock"), width=12, height=2).grid(row=4, column=0, pady=20)
    Button(root, text="Paper", command=lambda: player2_choice_handler("paper"), width=12, height=2).grid(row=4, column=1, pady=20)
    Button(root, text="Scissors", command=lambda: player2_choice_handler("scissors"), width=12, height=2).grid(row=4, column=2, pady=20)

def show_player1_buttons():
    clear_buttons(rows=[4])
    Button(root, text="Rock", command=lambda: play_multiplayer("rock"), width=12, height=2).grid(row=3, column=0, pady=20, padx=10)
    Button(root, text="Paper", command=lambda: play_multiplayer("paper"), width=12, height=2).grid(row=3, column=1, pady=20, padx=10)
    Button(root, text="Scissors", command=lambda: play_multiplayer("scissors"), width=12, height=2).grid(row=3, column=2, pady=20, padx=10)

# ----------------------- Mode Selection -------------------------
def choose_mode():
    clear_buttons()
    result_label.config(text="Choose a mode:")
    score_label.config(text="Scoreboard")

    def start_single_player():
        global player_score, computer_score, round_count
        clear_buttons()

        player1_label.grid_remove()
        player2_label.grid_remove()
        player1_score_label.grid_remove() # Hides Player 1 score in single player mode
        player2_score_label.grid_remove() # Hides Player 2 score in single player mode
        # Reset scores
        player_score = 0
        computer_score = 0
        round_count = 0


        result_label.config(text="Choose Rock, Paper, or Scissors")
        score_label.config(text=f"You: {player_score}  |  Computer:  {computer_score}")

        Button(root, text="Rock", command=lambda: play_single("rock"), width=12, height=2).grid(row=4, column=0, pady=20, padx=10)
        Button(root, text="Paper", command=lambda: play_single("paper"), width=12, height=2).grid(row=4, column=1, pady=20, padx=10)
        Button(root, text="Scissors", command=lambda: play_single("scissors"), width=12, height=2).grid(row=4, column=2, pady=20, padx=10)

    def start_multiplayer():
        global player1_score, player2_score
        clear_buttons()
        player1_label.grid()
        player2_label.grid()
        player1_score = 0
        player2_score = 0
        result_label.config(text="Player 1, make your choice!")
        player1_score_label.config(text=f"Player 1: {player1_score}")
        player2_score_label.config(text=f"Player 2: {player2_score}")

        show_player1_buttons()
        show_play_again_button()

    Button(root, text="Single Player", command=start_single_player, width=16, height=3).grid(row=3, column=0, pady=20, padx=10)
    Button(root, text="Multiplayer", command=start_multiplayer, width=16, height=3).grid(row=3, column=2, pady=20, padx=10)

choose_mode()
root.mainloop()
