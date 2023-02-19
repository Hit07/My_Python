# # #Let's go
# #
# # # Step 1
# #
# # word_list = ["aardvark", "baboon", "camel"]
# #
# # # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# #
# # # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# #
# # # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# # import random
# #
# # word = random.choice(word_list)
# # print(f"{word}")
# # dash_word = " ".join(word).split()
# # chosen_word = dash_word.copy()
# # word_length = len(dash_word)
# # for char in range(word_length):
# #     dash_word[char] = "_"
# # print(dash_word)
# # final_list=dash_word
# # while final_list!= "_":
# #     letter = input("Guess a letter?").lower()
# #     for n in range(0, len(chosen_word)):
# #         if chosen_word[n] == letter:
# #             final_list= dash_word.insert(n, letter)
# #         else:
# #             final_list=dash_word.insert(n, "_")
# # print(final_list)
# # print("you win!!")
# #
# #__________????????????//////////-----------------------
# # ----====-----------Hangman Project-------====---------------
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# import  random
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# lives = 6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     print(f"Gussed letter:{guess}")
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(f"{' '.join(display)}")
#     if guess not in chosen_word:
#         if lives == 0:
#             print("Game over")
#             break
#         lives -= 1
#         print(f"Remaining Lives: {lives}")
#         print(stages[lives])
# #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#___________
# #-----------------------------------------------------------------------
#
#
#
#
#
