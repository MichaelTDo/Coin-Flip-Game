import tkinter as tk
import random

# Coin Flipping Function
# Guessing correctly increases Score by 1 and gives message
# Guessing incorrectly does nothing and also gives message
def flip_coin(x):
    global score
    result = random.choice(["Heads", "Tails"])
# Logs results into coin_flip_logs.txt file
    with open("coin_flip_logs.txt", "a") as log_file:
        log_file.write(f"Guess: {x}, Result: {result}\n")

    if x == result:
        score += 1
        outcome_label.config(text= "You Guessed It Right! Congrats!")
    else:
        outcome_label.config(text= "You Guessed It Wrong. Try Again.")

    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score: {score}")
# Wins the game if the score is 10
    if score == 10:
        program_destroy()
        winner_screen()
# def flip_coin(x) end

# Destroys the program when function called
def program_destroy():
    root.destroy()

# Pop-up Screen that informs the user that they won
def winner_screen():
    popup = tk.Toplevel()
    popup.title("Winner")
    winner_label = tk.Label(popup, text= "Congrats, you won!")
    winner_label.pack(padx=20, pady=20)

# Main Window
root = tk.Tk()
root.title("Coin Flipping Game")

# Score
score = 0

# Label
label = tk.Label(root, text = "Flip a Coin!")
label.pack()

# UI for heads or tails
buttonL = tk.Button(root, text= "Heads", command=lambda: flip_coin("Heads"))
buttonL.pack(side= tk.LEFT, padx= 10)

buttonR = tk.Button(root, text= "Tails", command=lambda: flip_coin("Tails"))
buttonR.pack(side= tk.RIGHT, padx = 10)

# Score + Outcome + Result Label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

outcome_label = tk.Label(root, text="")
outcome_label.pack()

score_label = tk.Label(root, text="Score: ")
score_label.pack()

# Exits the program by destroying it
exitButton = tk.Button(root, text = "Exit.", bg="red", fg="white", font=("Arial", 10),
                   relief=tk.RAISED, width=10, height=2, command = program_destroy)
exitButton.pack()

root.mainloop()