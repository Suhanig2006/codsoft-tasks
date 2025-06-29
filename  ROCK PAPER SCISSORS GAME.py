# ROCK PAPER SCISSORS GAME
import tkinter as tk
import random

# Initialize scores
user_score = 0
comp_score = 0

# Main game logic
def play(choice):
    global user_score, comp_score
    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)

    user_label.config(text=f"You chose: {choice}")
    comp_label.config(text=f"Computer chose: {computer}")

    if choice == computer:
        result_label.config(text="It's a Draw!", fg="orange")
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Scissors" and computer == "Paper") or \
         (choice == "Paper" and computer == "Rock"):
        result_label.config(text="You Win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="You Lose!", fg="red")
        comp_score += 1

    update_score()

# Function to update score display
def update_score():
    score_label.config(text=f"Score: You {user_score} - {comp_score} Computer")

# Reset game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="You chose:")
    comp_label.config(text="Computer chose:")
    result_label.config(text="", fg="black")
    update_score()

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.configure(bg="#FAEE68")  # Light background

# Title
tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"), fg="#2E86AB", bg="#F193D0").pack(pady=20)

# Choice labels
user_label = tk.Label(root, text="You chose:", font=("Arial", 12), bg="#F2A55D")
user_label.pack()

comp_label = tk.Label(root, text="Computer chose:", font=("Arial", 12), bg="#7BC4E4")
comp_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#9AED74")
result_label.pack(pady=10)

# Score tracker
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12, "bold"), bg="#FFFBE7", fg="black")
score_label.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="#FFFBE7")
button_frame.pack(pady=20)

tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 12), bg="#6DBDF1", command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 12), bg="#5FE6A2", command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 12), bg="#EE7E9C", command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Restart and Exit buttons
tk.Button(root, text="🔄 Restart", width=15, font=("Arial", 12), bg="#F7DC6F", command=reset_game).pack(pady=5)
tk.Button(root, text="❌ Exit", width=15, font=("Arial", 12), bg="#AAB7B8", command=root.destroy).pack(pady=5)

# Start the application
root.mainloop()
