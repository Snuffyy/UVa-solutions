import math

while True:

  try:
    bulbs = int(input())
  except EOFError:
    break

  if bulbs == 0:
    break

  if math.sqrt(bulbs) % 1 == 0:
    print('yes')
  else:
    print('no')
