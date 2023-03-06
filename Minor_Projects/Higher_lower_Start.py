from Higher_lower_Start_art import list_people
from Higher_lower_Start_art import logo_1
from Higher_lower_Start_art import logo_vs
from random import choice
print("--------------------------------------\n"+logo_1+"-----------------------------------------\n")

def play_game():
    def compare(choose_a,choose_b,guess):
        global score
        if guess =='A':
            if list_people[choose_a]>list_people[choose_b]:
                score += 1
                return print(f"Good Job!,Right answer....Final Score: {score}")
            elif list_people[choose_a] == list_people[choose_b]:
                score+=1
                return print(f"Draw match!,Try Again...Final Score:{score}")
            else:
                return print(f"Sorry,that's wrong answer.Final Score: {score}")

        if guess == 'B':
            if list_people[choose_a]<list_people[choose_b]:
                score += 1
                return print(f"Good Job!,Right answer....Final Score: {score}")
            elif list_people[choose_a] == list_people[choose_b]:
                 score+=1
                 return print(f"Draw match!,Try Again...Final Score:{score}")
            else:
                return print(f"Sorry,that's wrong answer.Final Score: {score}")

    choose_a = choice(list(list_people.keys()))
    choose_b = choice(list(list_people.keys()))
    print(list_people[choose_a],list_people[choose_b])
    print(f"Compare A: {choose_a}")
    print(logo_vs)
    print(f"Against B: {choose_b}")
    guess = input("Who has more followers Type 'A' or 'B':")
    compare(choose_a, choose_b, guess)


score = 0
play = True
while play:
    play_game()
    to_continue = input("Do you wanna continue?\nType 'yes' or 'no':").lower()
    if to_continue == 'yes':
        continue
    else:
        play = False
print('Game over!!👋')

