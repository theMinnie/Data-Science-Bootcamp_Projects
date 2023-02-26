from random import choice


def result(computer, player, player_result):
  print(f'{computer} vs {player}')
  if computer == player:
    print("Draw")
    player_result["Tie"] += 1

  elif (computer == 'Scissor' and player == 'Paper')\
    or (computer == 'Paper' and player == 'Rock')\
    or (computer == 'Rock' and player =='Scissor'):
    print("You Lose!")
    player_result['Lose'] += 1

  else:
    print("You Win!!")
    player_result['Win'] += 1

  return player_result


def play():
  paoyingchub = {1: 'Scissor', 2: 'Paper', 3: 'Rock'}
  computer = choice(list(range(1, 4)))

  try:
    player = int(input("1 : Scissor | 2 : Paper | 3 : Rock | 0 : Stop\n"))
  except:
    print('Please put only number between 0 and 3')
  if player == 0:
    return (None, player)
  elif player not in [1, 2, 3]:
    print('Please put only number between 1 and 3')
  else:
    return (paoyingchub[computer], paoyingchub[player])


def start():
  player_result = {'Win': 0, 'Lose': 0, 'Tie': 0}
  while True:
    try:
      computer, player = play()
    except:
      continue

    if player == 0:
      break
    else:
      player_result = result(computer, player, player_result)
      print(player_result)
      print("*" * 30)

  # Summarize the final result
  print(f"Total rounds = {sum(player_result.values())}")
  for key, value in player_result.items():
    if key == 'Win':
      print(f'You won : {value} times')
    elif key == 'Lose':
      print(f'You lost : {value} times')
    else:
      print(f'Tied : {value} times')
