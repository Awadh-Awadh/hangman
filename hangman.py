import random

world_list = ['mouse', 'baboon', 'python', 'code']
choosen_word = list(random.choice(world_list))
print("-" * len(choosen_word))
val = input("Guess letter \n") 
for letter in choosen_word:
    if val == letter:
        print("Right")
    else:
        print("false")
