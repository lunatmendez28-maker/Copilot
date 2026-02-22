"""print("Program started 🚀")
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import tkinter as tk
from tkinter import font, messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors 🎮")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")
        
        # Variables
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.emojis = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        self.choices = ['rock', 'paper', 'scissors']
        
        # Fonts
        self.title_font = font.Font(family="Arial", size=20, weight="bold")
        self.button_font = font.Font(family="Arial", size=16, weight="bold")
        self.info_font = font.Font(family="Arial", size=14)
        
        # Title
        title = tk.Label(self.root, text="Rock, Paper, Scissors", font=self.title_font, bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=20)
        
        # Scoreboard frame
        scoreboard_frame = tk.Frame(self.root, bg="#34495e", relief=tk.RIDGE, bd=2)
        scoreboard_frame.pack(pady=15, padx=20, fill=tk.BOTH)
        
        # Scoreboard title
        scoreboard_title = tk.Label(scoreboard_frame, text="📊 SCOREBOARD", font=font.Font(family="Arial", size=12, weight="bold"), bg="#34495e", fg="#f39c12")
        scoreboard_title.pack(pady=5)
        
        # Score details frame
        score_details_frame = tk.Frame(scoreboard_frame, bg="#34495e")
        score_details_frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        # Player wins
        player_frame = tk.Frame(score_details_frame, bg="#34495e")
        player_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10)
        tk.Label(player_frame, text="You Win", font=font.Font(family="Arial", size=10), bg="#34495e", fg="#3498db").pack()
        self.player_wins_label = tk.Label(player_frame, text="0", font=font.Font(family="Arial", size=18, weight="bold"), bg="#34495e", fg="#3498db")
        self.player_wins_label.pack()
        
        # Ties
        ties_frame = tk.Frame(score_details_frame, bg="#34495e")
        ties_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10)
        tk.Label(ties_frame, text="Ties", font=font.Font(family="Arial", size=10), bg="#34495e", fg="#f39c12").pack()
        self.ties_label = tk.Label(ties_frame, text="0", font=font.Font(family="Arial", size=18, weight="bold"), bg="#34495e", fg="#f39c12")
        self.ties_label.pack()
        
        # Computer wins
        computer_frame = tk.Frame(score_details_frame, bg="#34495e")
        computer_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10)
        tk.Label(computer_frame, text="Machine Wins", font=font.Font(family="Arial", size=10), bg="#34495e", fg="#e74c3c").pack()
        self.computer_wins_label = tk.Label(computer_frame, text="0", font=font.Font(family="Arial", size=18, weight="bold"), bg="#34495e", fg="#e74c3c")
        self.computer_wins_label.pack()
        
        # Score summary line
        self.score_label = tk.Label(scoreboard_frame, text="Total rounds: 0", font=font.Font(family="Arial", size=9), bg="#34495e", fg="#95a5a6")
        self.score_label.pack(pady=5)
        
        # Result frame
        result_frame = tk.Frame(self.root, bg="#2c3e50")
        result_frame.pack(pady=15)
        
        self.result_label = tk.Label(result_frame, text="Choose an option", font=self.info_font, bg="#2c3e50", fg="#ecf0f1")
        self.result_label.pack()
        
        # Choices display
        choices_display_frame = tk.Frame(self.root, bg="#2c3e50")
        choices_display_frame.pack(pady=15)
        
        tk.Label(choices_display_frame, text="You:", font=self.info_font, bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=10)
        self.player_choice_label = tk.Label(choices_display_frame, text="-", font=("Arial", 40), bg="#2c3e50", fg="#f39c12")
        self.player_choice_label.pack(side=tk.LEFT, padx=10)
        
        tk.Label(choices_display_frame, text="Machine:", font=self.info_font, bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=10)
        self.computer_choice_label = tk.Label(choices_display_frame, text="-", font=("Arial", 40), bg="#2c3e50", fg="#e74c3c")
        self.computer_choice_label.pack(side=tk.LEFT, padx=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        buttons_frame.pack(pady=20)
        
        # Rock button
        rock_btn = tk.Button(buttons_frame, text="🪨 Rock", font=self.button_font, bg="#3498db", fg="white", command=lambda: self.play('rock'), width=12)
        rock_btn.pack(pady=10)
        
        # Paper button
        paper_btn = tk.Button(buttons_frame, text="📄 Paper", font=self.button_font, bg="#2ecc71", fg="white", command=lambda: self.play('paper'), width=12)
        paper_btn.pack(pady=10)
        
        # Scissors button
        scissors_btn = tk.Button(buttons_frame, text="✂️ Scissors", font=self.button_font, bg="#e74c3c", fg="white", command=lambda: self.play('scissors'), width=12)
        scissors_btn.pack(pady=10)
        
        # Reset button
        reset_btn = tk.Button(buttons_frame, text="🔄 Reset", font=self.button_font, bg="#95a5a6", fg="white", command=self.reset_scores, width=12)
        reset_btn.pack(pady=10)
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a Tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            return "You Won! 🎉"
        else:
            return "Machine Won 🤖"
    
    def play(self, player_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update score
        if result == "You Won! 🎉":
            self.player_score += 1
        elif result == "Machine Won 🤖":
            self.computer_score += 1
        elif result == "It's a Tie!":
            self.ties += 1
        
        # Update labels
        self.player_choice_label.config(text=self.emojis[player_choice])
        self.computer_choice_label.config(text=self.emojis[computer_choice])
        self.result_label.config(text=result)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Update the scoreboard display"""
        self.player_wins_label.config(text=str(self.player_score))
        self.computer_wins_label.config(text=str(self.computer_score))
        self.ties_label.config(text=str(self.ties))
        total_rounds = self.player_score + self.computer_score + self.ties
        self.score_label.config(text=f"Total rounds: {total_rounds}")
        
        # Check for victory (10 wins)
        if self.player_score >= 10:
            self.show_victory_celebration("Congratulations! You won the game!")
            self.reset_scores()
        elif self.computer_score >= 10:
            self.show_victory_celebration("The machine has won the game!")
            self.reset_scores()
    
    def show_victory_celebration(self, winner_message):
        """Show celebration with falling balloons when someone reaches 10 wins"""
        # Create celebration window
        celebration_window = tk.Toplevel(self.root)
        celebration_window.title("VICTORY! 🏆")
        celebration_window.geometry("800x600")
        celebration_window.configure(bg="#2c3e50")
        
        # Canvas for balloons
        canvas = tk.Canvas(celebration_window, bg="#2c3e50", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Victory message
        message_label = tk.Label(celebration_window, text=winner_message, font=font.Font(family="Arial", size=24, weight="bold"), bg="#2c3e50", fg="#f39c12")
        message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Balloon emojis
        balloon_emojis = ['🎈', '🎊', '🎉', '🎁', '✨']
        balloons = []
        
        # Create initial balloons
        import random as rnd
        for i in range(30):
            x = rnd.randint(0, 800)
            y = rnd.randint(-100, 0)
            emoji = rnd.choice(balloon_emojis)
            balloon_id = canvas.create_text(x, y, text=emoji, font=("Arial", 60), fill="white")
            balloons.append({'id': balloon_id, 'x': x, 'y': y, 'emoji': emoji})
        
        # Falling animation
        def animate_balloons():
            for balloon in balloons:
                balloon['y'] += rnd.randint(2, 5)  # Variable speed
                balloon['x'] += rnd.randint(-2, 2)  # Random horizontal movement
                
                # If balloon falls off screen, reset it to the top
                if balloon['y'] > 600:
                    balloon['y'] = -100
                    balloon['x'] = rnd.randint(0, 800)
                
                canvas.coords(balloon['id'], balloon['x'], balloon['y'])
            
            # Continue animation
            celebration_window.after(50, animate_balloons)
        
        # Start animation
        animate_balloons()
        
        # Close window after 5 seconds
        celebration_window.after(5000, celebration_window.destroy)
    
    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.player_choice_label.config(text="-")
        self.computer_choice_label.config(text="-")
        self.result_label.config(text="Choose an option")
        self.update_scoreboard()

if __name__ == "__main__":
    root = tk.Tk()
    gui = RockPaperScissorsGUI(root)
    root.mainloop()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def get_emoji(choice):
    emojis = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
    return emojis.get(choice, '')
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!" 
def main():
    player_score = 0
    computer_score = 0
    print("Welcome to Rock Paper Scissors! Type 'quit' to exit.")
    while True:
        player_choice = input("Enter your choice (r/rock, p/paper, s/scissors): ").lower().strip()
        # Map shortcuts and common variants to full names
        choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'scissor': 'scissors'}
        player_choice = choice_map.get(player_choice, player_choice)
# ...existing code...
# filepath: c:\Users\lunat\Pictures\CODE\Nueva\COPILOT\piedra_papel_tijera.py
        # Map shortcuts to full names
        choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        player_choice = choice_map.get(player_choice, player_choice)
        if player_choice == 'quit':
            print("Thanks for playing! Final score - You: {}, Computer: {}".format(player_score, computer_score))
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print("Computer chose: {}".format(computer_choice))
        player_emoji = get_emoji(player_choice)
        computer_emoji = get_emoji(computer_choice)
        print("You chose: {} {} | Computer chose: {} {}".format(player_choice, player_emoji, computer_choice, computer_emoji))
        result: str = determine_winner(player_choice, computer_choice)
        print(result)
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
if __name__ == "__main__":
    main()