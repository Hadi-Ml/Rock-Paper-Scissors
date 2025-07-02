import random
class Rock_Paper_Scissors():
    def __init__(self, name, level):
        self.level = level.lower()
        self.choices = ['rock', 'paper', 'scissor', 'spock', 'lizard']
        self.name = name
        self.Legals = {"rock":["scissor", "lizard"], "scissor":["paper", "lizard"],"paper":["rock", "spock"], "lizard": ["spock", "paper"], "spock": ["scissor", "rock"]}

    def play(self):
        self.user_choice = self.user_choice_function()
        self.computer_choice = self.computer_choice_function()
        print(f"Your choice is {self.user_choice} and Computer choice is {self.computer_choice}")
        winner = self.decide_winner(self.user_choice, self.computer_choice)
        return winner

    def user_choice_function(self):
        while True:
            user_input = input('Enter Your Choice (Rock, Paper, Scissor, Spock, Lizard): ').lower()
            if user_input in self.choices:
                return user_input
            else:
                print("Invalid Input , Please Try Again!")

    def computer_choice_function(self):
        while True:
            if self.level == 'easy':
                computer_input = random.choice(self.choices)
                return computer_input

            elif self.level == 'hard':
                for i in range(2):
                    computer_input = random.choice(self.choices)
                    if self.user_choice in self.Legals[f"{computer_input}"]:
                        return computer_input
                return computer_input

    def decide_winner(self, user_choice, computer_choice):
        if user_choice in self.Legals[f"{computer_choice}"] :
            return "Computer"
        elif computer_choice in self.Legals[f"{user_choice}"] :
            return f"{self.name}"
        else :
            return "Draw"



if __name__ == "__main__":
    print("\n*** Wellcome to our Rock Paper Scissors Game ***\n")
    print("Legals of Game :\n-Scissor Cuts Lizard \t-Scissor Cuts Paper \n-Paper Covers Rock \t-Paper Covers Spock \n-Rock Destroys Scissors \t-Rock Destroys Lizard \n-Lizard Poisons Spock \t-Lizard Eats Paper \n-Spock Destroys Scissor \t-Spock Destroys Rock\n")
    name = input("Enter Your Name : ")

    while True:
        text = input("\nWanna Play Game (Yes or No) : ").lower()
        if text == "yes":
            level = input("Enter the Level of Game (Easy , Hard) : ")
            Game = Rock_Paper_Scissors(name, level)
            Winner = Game.play()
            print(f"Winner is : {Winner}\n")
        elif text == "no":
            print("*** Thanks for Playing , Hope you Best ***")
            break
        else:
            print("Invalid Input , Please try again")
