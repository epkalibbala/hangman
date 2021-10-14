import random

word_list = ['mosquito', 'umbrella', 'bus']

choose_word = random.choice(word_list)

progress = ''
user_input = ''
correct_letts = ''
test = bool(1) 

for n in range(0,len(choose_word)):
  progress+='_'

print('Guess the word')
#print('mosquito'.index('t', 0))
#len(choose_word) > len(user_input) or len(choose_word) >= len(correct_letts)
while (1):
  print(progress)
  if len(choose_word) < len(user_input) or len(choose_word) <= len(correct_letts):
    print('Game Over')
    break

  guess = input("What's your guess? ")

  if guess.lower() in choose_word:
    correct_letts+=guess
  else:
    user_input+=guess

  for letter in correct_letts:
    if letter != '':
      p = list(progress)
      p[choose_word.index(letter, 0)] = letter
      progress = "".join(p)
