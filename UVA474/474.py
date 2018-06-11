import math

log_5_2 = math.log(5, 2)


def calc(n):
  b = math.ceil(n / (1 + log_5_2))

  a = math.pow(2, (b * (1 + log_5_2) - n))

  return a, b


if __name__ == '__main__':

  while True:

    try:
      line = input()
    except EOFError:
      break

    n = int(line)
    a, b = calc(n)

    print(f"2^-{n} = {format(a, '.3f')}e-{b}")
