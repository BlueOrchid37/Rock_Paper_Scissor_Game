import random

CHOICES = ["rock", "paper", "scissor"]


def get_user_choice():
    choice = int(input("\n1 Rock\n2 Paper\n3 Scissor\nChoose: "))
    if choice in [1, 2, 3]:
        return CHOICES[choice - 1]
    print("Invalid input")
    return None


def decide_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == "rock" and computer == "scissor") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissor" and computer == "paper"):
        return "user"
    return "computer"


def play_series(rounds=5):
    user_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice = get_user_choice()
        if not user_choice:
            continue

        computer_choice = random.choice(CHOICES)
        print("Your Choice:", user_choice)
        print("Computer Choice:", computer_choice)

        result = decide_winner(user_choice, computer_choice)

        if result == "user":
            print("You won this round\n")
            user_score += 1
        elif result == "computer":
            print("Computer won this round\n")
            computer_score += 1
        else:
            print("Round tied\n")
            user_score += 1
            computer_score += 1

    return user_score, computer_score


def main():
    while True:
        play = int(input("\n1 Play Game\n2 Exit\nChoose: "))
        if play != 1:
            print("Exit")
            break

        user, computer = play_series()

        print("\nFinal Score")
        print("You:", user)
        print("Computer:", computer)

        if user > computer:
            print("You won the series!")
        elif computer > user:
            print("Computer won the series!")
        else:
            print("Series Draw!")


if __name__ == "__main__":
    main()
