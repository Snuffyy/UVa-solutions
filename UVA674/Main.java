package UVA674;

import java.util.Scanner;

public class Main {

  private static final int MAX = 7489 + 1;
  private static final int[] results = new int[MAX];

  private static void compute() {
    byte[] coins = new byte[]{1, 5, 10, 25, 50};

    results[0] = 1;

    int counter = 0;

    while (true) {
      if (counter == 5) {
        break;
      }

      for (int index = coins[counter]; index < MAX; index++) {
        results[index] = results[index] + results[index - coins[counter]];
      }

      counter++;
    }
  }

  private static int get(int n) {
    return results[n];
  }

  public static void main(String[] args) {
    compute();

    Scanner sc = new Scanner(System.in);

    while (sc.hasNext()) {
      System.out.println(get(sc.nextInt()));
    }
  }
}
