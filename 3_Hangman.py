import random

display_1 = """
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
"""
display_2 = """
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
"""
display_3 = """
      _______
     |/      |
     |      (_)
     |      \|
     |      
     |      
     |
    _|___
"""
display_4 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
"""
display_5 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
"""
display_6 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
"""

display_list = [display_6, display_5, display_4, display_3, display_2, display_1]
word_list = ["aardvark", "baboon", "camel"]
game_over = False
life_left = 5

word_choice = random.choice(word_list)
word_answer = []
for letter in word_choice:
    word_answer.append("_")

print("You are now playing hangman!")

while not game_over:
    print(display_list[life_left])
    print(word_answer)
    player_letter = input("Pick a letter: ").lower()
    if len(player_letter) != 1 or not player_letter.isalpha():
        print("Invalid input")
        continue

    if player_letter not in word_choice:
        life_left -= 1
        if life_left <= 0:
            game_over = True
            print(display_list[0])
            print("Your stickman has died! You lost")
        continue

    if player_letter in word_answer:
        print(f"You already guessed {player_letter}!")
        continue

    for i in range(len(word_choice)):
        if player_letter == word_choice[i]:
            word_answer[i] = player_letter

    if "_" not in word_answer:
        print("The stickman lives! You win")
        game_over = True
