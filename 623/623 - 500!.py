def pre_calc():
  arr = []
  arr.append(1)

  for i in range(1, 1001):
    arr.append(arr[i - 1] * i)

  return arr


if __name__ == '__main__':

  arr = pre_calc()

  while True:

    try:
      number = int(input())
    except EOFError:
      break

    print('{num}!\n{fact}'.format(num=number, fact=arr[number]))
