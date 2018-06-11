num_of_cases = int(input())

for case_num in range(num_of_cases):
  case = input().split(" ")
  length = int(case[0])
  houses = list(map(int, case[1:]))
  houses.sort()

  if length % 2 == 0:
    center = int(length / 2 - 1)
  else:
    center = int(length / 2)

  closest_house = houses[center]

  houses.remove(closest_house)

  counter = 0

  for house in houses:
    counter += abs(house - closest_house)

  print(counter)
