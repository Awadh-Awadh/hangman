import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

world_list = ['mouse', 'baboon', 'python', 'code']
choosen_word = list(random.choice(world_list))
print(choosen_word)

#  Tricks
# res = []
# val = input("Guess letter \n") 
# for letter in choosen_word:
#     if val == letter:
#         res.append(val)
#     else:
#       res.append("_,")


lives = 6

end_game = False

while not end_game:
    res = []
    for _ in range(len(choosen_word)):
      res += '_'
    print(res)
    val = input("Guess letter \n") 
    for position in range(len(choosen_word)):
       letter = choosen_word[position]
       if val == letter :
        res[position] = letter
    if val not in choosen_word:
        lives -=1
        if lives == 0:
            print("You lost")
            end_game = True

    if "_" in res:
        print("You won")
        end_game = True
        