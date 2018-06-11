def is_equal(string, i, j):
  string = string[min(i, j):max(i, j) + 1]
  return string.count(string[0]) == len(string)


if __name__ == '__main__':

  counter = 1

  while True:
    try:
      line = input()
    except EOFError:
      break

    print(f"Case {counter}:")

    count = int(input())

    for index in range(count):
      i, j = map(int, input().split(" "))
      print(f"{'Yes' if is_equal(line, i, j) else 'No'}")

    counter += 1
