if __name__ == '__main__':

    dictionary = {}

    while True:

      line = input()

      if line == '':
        break

      english, foreign = line.split()

      dictionary[foreign] = english

    while True:
      try:
        line = input()
      except EOFError:
        break

      if line in dictionary:
        print(dictionary[line])
      else:
        print('eh')
