import random
from hangword import *
from hangart import *

print(logo)




world_list = ['mouse', 'baboon', 'python', 'code']

# Gets a random word and creates a list out of the letters

choosen_word = list(random.choice(world_list))

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

# creating a list of randomly choosen word replaced with dashes

res = []
for _ in range(len(choosen_word)):
  res += '_'

#Iteration as long as the game has not ended
while not end_game:    
    val = input("Guess letter \n")    
    if val in res:
      print(f"{val} already exist Please try another letter")
    for position in range(len(choosen_word)):
       letter = choosen_word[position]
       if val == letter :
        res[position] = letter
    print(" ".join(res))
    if val not in choosen_word:
        print(f"You have chosen {val} that's not in the word. You loose a life")
        lives -=1
        if lives == 0:
            print("You lost")
            end_game = True
    # The conditions checks that all the letters guesed match with the letters in the word and ends the game
    if "_" not in res:
        print("You won")
        end_game = True
    print(stages[lives])
        