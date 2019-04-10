print('...rock...')
print('...paper...')
print('...scissors...')

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

p1 = input('Player 1\'s choice: ')
p2 = input('Player 2\'s choice: ')

m1 = 'Player 1 wins!'
m2 = 'Player 2 wins!'

if p1 == p2:
  print('Match draw!')
elif p1 == ROCK and p2 == PAPER:
  print(m2)
elif p1 == ROCK and p2 == SCISSORS:
  print(m1)
elif p1 == PAPER and p2 == ROCK:
  print(m1)
elif p1 == PAPER and p2 == SCISSORS:
  print(m2)
elif p1 == SCISSORS and p2 == ROCK:
  print(m2)
elif p1 == SCISSORS and p2 == PAPER:
  print(m1)
else:
  print('Incorrect value found!')
