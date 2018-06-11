if __name__ == '__main__':

  while True:
    try:
      m, n = map(int, input().split(" "))
    except EOFError:
      break

    print(m * n - 1)
