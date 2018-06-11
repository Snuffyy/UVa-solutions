while True:
  try:
    n = int(input())
  except EOFError:
    break

  dividend = 1
  ones = 1

  while True:

    if dividend % n == 0:
      break
    else:
      dividend = dividend * 10 + 1
      ones += 1

  print(ones)
