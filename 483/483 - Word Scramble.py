def main():
  lines = []

  while True:
    try:
      line = input()
    except EOFError:
      break

    if line:
      lines.append(line)
    else:
      break

  result = []

  for line in lines:
    reversed_words = []
    for word in line.split(" "):
      reversed_words.append(word[::-1])

    result.append(" ".join(reversed_words))

  print("\n".join(result))


main()
