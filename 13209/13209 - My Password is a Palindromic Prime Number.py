def calculate(prime):

  remainder = 10 % prime

  lst = []

  while True:
    lst.append(remainder // prime)

    remainder = 10 * (remainder % prime)

    if remainder == 10:
      break

  print('0.' + ''.join(map(str, lst)))

if __name__ == '__main__':

    cases = int(input())

    for c in range(cases):
      pprime = int(input())

      calculate(pprime)
