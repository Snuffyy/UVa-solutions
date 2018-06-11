def get_Xll(R1Xll, R2Xll):
  return max(R1Xll, R2Xll)


def get_Yll(R1Yll, R2Yll):
  return max(R1Yll, R2Yll)


def get_Xur(R1Xur, R2Xur):
  return min(R1Xur, R2Xur)


def get_Yur(R1Yur, R2Yur):
  return min(R1Yur, R2Yur)


if __name__ == '__main__':

  cases = int(input())

  for case in range(cases):
    input()

    R1Xll, R1Yll, R1Xur, R1Yur = map(int, input().split())
    R2Xll, R2Yll, R2Xur, R2Yur = map(int, input().split())

    Xll = get_Xll(R1Xll, R2Xll)
    Yll = get_Yll(R1Yll, R2Yll)
    Xur = get_Xur(R1Xur, R2Xur)
    Yur = get_Yur(R1Yur, R2Yur)

    if Xur <= Xll or Yur <= Yll:
      print("No Overlap")
    else:
      print("{} {} {} {}".format(Xll, Yll, Xur, Yur))

    if case + 1 != cases:
      print()
