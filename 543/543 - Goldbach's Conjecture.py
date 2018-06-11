UPPER_BOUND = 1000000


def generate_primes():
  table = {boolean: True for boolean in range(UPPER_BOUND)}

  root = int(UPPER_BOUND ** 0.5)

  for i in range(2, root):

    index = i * 2

    while True:

      if index > UPPER_BOUND:
        break

      table[index] = False

      index += i

  return table


if __name__ == '__main__':
  table = generate_primes()

  while True:
    n = int(input())

    if n == 0:
      break

    found = False

    for index in range(3, UPPER_BOUND):
      a = table[index]
      if a:
        b = n - index

        if table[b]:
          print(f"{n} = {index} + {b}")
          found = True
          break

    if not found:
      print("Goldbach's conjecture is wrong.")
