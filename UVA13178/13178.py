if __name__ == '__main__':
  n = int(input())

  for i in range(n):

    number = int(input())

    half = number // 2

    if number % 2 == 0:
      sum = half * (1 + number)
    else:
      sum = half * (2 + number) + 1

    print("YES" if sum % 3 == 0 else "NO")
