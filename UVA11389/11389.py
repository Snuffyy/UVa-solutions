if __name__ == '__main__':
  while True:
    try:
      line = input()
    except EOFError:
      break

    nums = list(map(int, line.split(" ")))
    if len(nums) == 3:

      if nums[:3] == [0, 0, 0]:
        break

      num_of_drivers = nums[0]
      max_dist = nums[1]
      rate = nums[2]

      morning = sorted(map(int, input().split(" ")))
      afternoon = sorted(map(int, input().split(" ")), reverse=True)

      res = []

      for i in range(num_of_drivers):
        length = morning[i] + afternoon[i]
        if length > max_dist:
          res.append((morning[i] + afternoon[i]) - max_dist)

      print(sum(res) * rate)
