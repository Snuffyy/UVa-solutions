# 487--3279

dictionary = {'A': '2', 'B': '2', 'C': '2',
              'D': '3', 'E': '3', 'F': '3',
              'G': '4', 'H': '4', 'I': '4',
              'J': '5', 'K': '5', 'L': '5',
              'M': '6', 'N': '6', 'O': '6',
              'P': '7', 'R': '7', 'S': '7',
              'T': '8', 'U': '8', 'V': '8',
              'W': '9', 'X': '9', 'Y': '9'}


def main():
  number_of_datasets = int(input())

  counter = 1

  for data_set_num in range(number_of_datasets):

    line = input()
    n = int(input())

    results = []
    d = {}

    for i in range(n):
      line = input().strip()

      decoded = []

      for char in line:
        if char.isdigit():
          decoded.append(char)
        elif char == '-':
          continue
        else:
          decoded.append(dictionary[char])

      results.append(''.join(decoded))

    results.sort()

    for number in results:
      if number not in d:
        d[number] = 1
      else:
        d[number] += 1

    printed = False

    for key, value in d.items():
      if value > 1:
        print("{}-{} {}".format(key[:3], key[3:], value))
        if not printed:
          printed = True

    if not printed:
      print("No duplicates.")

    if counter != number_of_datasets:
      print()

    counter += 1


main()
