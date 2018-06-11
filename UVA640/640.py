LIMIT = 1000000


def get_digits(n):
  digits = []

  while True:

    if n < 10:
      digits.append(n)
      break

    digits.append(n % 10)
    n = int(n / 10)

  return digits


def pre_calculate():
  data = [True] * (LIMIT + 1)
  data[0] = False

  for i in range(1, LIMIT + 1):
    index = i + sum(get_digits(i))

    if index < LIMIT:
      data[index] = False

  return data


if __name__ == '__main__':
  data = pre_calculate()

  print(data[LIMIT])

  for num, bool in enumerate(data):
    if (bool):
      print(num)
