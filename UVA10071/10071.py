def main():
  lines = []

  while True:

    try:
      inp = input()
    except EOFError:
      break

    if inp:
      lines.append(inp)
    else:
      break

  for line in lines:
    v, t = line.split(" ")
    v = int(v)
    t = int(t)

    print(v * t * 2)


main()