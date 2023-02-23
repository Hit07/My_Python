# # # #Let's go
# # #
# # # # Step 1
# # #
# # # word_list = ["aardvark", "baboon", "camel"]
# # #
# # # # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# # #
# # # # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# # #
# # # # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# # # import random
# # #
# # # word = random.choice(word_list)
# # # print(f"{word}")
# # # dash_word = " ".join(word).split()
# # # chosen_word = dash_word.copy()
# # # word_length = len(dash_word)
# # # for char in range(word_length):
# # #     dash_word[char] = "_"
# # # print(dash_word)
# # # final_list=dash_word
# # # while final_list!= "_":
# # #     letter = input("Guess a letter?").lower()
# # #     for n in range(0, len(chosen_word)):
# # #         if chosen_word[n] == letter:
# # #             final_list= dash_word.insert(n, letter)
# # #         else:
# # #             final_list=dash_word.insert(n, "_")
# # # print(final_list)
# # # print("you win!!")
# # #
# # #__________????????????//////////-----------------------
# # # ----====-----------Hangman Project-------====---------------
# #
# # stages = ['''
# #   +---+
# #   |   |
# #   O   |
# #  /|\  |
# #  / \  |
# #       |
# # =========
# # ''', '''
# #   +---+
# #   |   |
# #   O   |
# #  /|\  |
# #  /    |
# #       |
# # =========
# # ''', '''
# #   +---+
# #   |   |
# #   O   |
# #  /|\  |
# #       |
# #       |
# # =========
# # ''', '''
# #   +---+
# #   |   |
# #   O   |
# #  /|   |
# #       |
# #       |
# # =========''', '''
# #   +---+
# #   |   |
# #   O   |
# #   |   |
# #       |
# #       |
# # =========
# # ''', '''
# #   +---+
# #   |   |
# #   O   |
# #       |
# #       |
# #       |
# # =========
# # ''', '''
# #   +---+
# #   |   |
# #       |
# #       |
# #       |
# #       |
# # =========
# # ''']
# # import  random
# # end_of_game = False
# # word_list = ["ardvark", "baboon", "camel"]
# # chosen_word = random.choice(word_list)
# # word_length = len(chosen_word)
# # lives = 6
# # #Testing code
# # print(f'Pssst, the solution is {chosen_word}.')
# # #Create blanks
# # display = []
# # for _ in range(word_length):
# #     display += "_"
# # while not end_of_game:
# #     guess = input("Guess a letter: ").lower()
# #     print(f"Gussed letter:{guess}")
# #     #Check guessed letter
# #     for position in range(word_length):
# #         letter = chosen_word[position]
# #         if letter == guess:
# #             display[position] = letter
# #     print(f"{' '.join(display)}")
# #     if guess not in chosen_word:
# #         if lives == 0:
# #             print("Game over")
# #             break
# #         lives -= 1
# #         print(f"Remaining Lives: {lives}")
# #         print(stages[lives])
# # #Check if user has got all letters.
# #     if "_" not in display:
# #         end_of_game = True
# #         print("You win.")
# #___________
# # #-----------------------------------------------------------------------
# #Step 5
#
# import random
# import hangman_art
# import hangman_words
# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# print(hangman_art.logo)
# chosen_word = random.choice(hangman_words.word_list)
# word_length = len(chosen_word)
#
# end_of_game = False
# lives = 6
#
# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     print(f"Your guessed letter is: {guess}")
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     print(hangman_art.stages[lives])