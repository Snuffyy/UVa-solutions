if __name__ == '__main__':

  while True:
    n, m, c = map(int, input().split(" "))

    if n == 0 and m == 0:
      break

    if c == 1:
      print(int(((n - 7) * (m - 7) + 1) / 2))
    else:
      print(int((n - 7) * (m - 7) / 2))
