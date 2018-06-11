LIMIT = 5001
F0 = 0
F1 = 1


def pre_calculate():
  data = [0] * LIMIT
  data[0] = F0
  data[1] = F1

  for i in range(2, LIMIT):
    data[i] = data[i - 1] + data[i - 2]

  return data


if __name__ == '__main__':
  data = pre_calculate()

  while True:

    try:
      num = int(input())

    except EOFError:
      break

    print('The Fibonacci number for {num} is {answer}'.format(num=num, answer=data[num]))
