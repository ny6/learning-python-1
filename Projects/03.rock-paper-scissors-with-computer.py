from random import randint

print('...rock...')
print('...paper...')
print('...scissors...')
print('...with computer...')

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

player = input('Your choice: ').upper()
ai_option = randint(0, 2)

computer = SCISSORS
if ai_option == 0:
  computer = ROCK
elif ai_option == 1:
  computer = PAPER

print(f'Computer plays: {computer}')

m1 = 'You won!'
m2 = 'Computer won!'

if player == computer:
  print('It is a tie!')
elif player == ROCK:
  if computer == PAPER:
    print(m2)
  else:
    print(m1)
elif player == PAPER:
  if computer == ROCK:
    print(m1)
  else:
    print(m2)
elif player == SCISSORS:
  if computer == ROCK:
    print(m2)
  else:
    print(m1)
else:
  print('Invalid option!')
