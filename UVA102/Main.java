package UVA102;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {


  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    String line;

    while (sc.hasNext()) {

      line = sc.nextLine();

      String[] bottles = line.split(" ");

      Bin first = new Bin(bottles[0], bottles[1], bottles[2]);
      Bin second = new Bin(bottles[3], bottles[4], bottles[5]);
      Bin third = new Bin(bottles[6], bottles[7], bottles[8]);

      Result bcg = new Result(Combination.BCG,
          second.getBrown() + third.getBrown() + first.getClear() + third.getClear() + first
              .getGreen() + second.getGreen());

      Result bgc = new Result(Combination.BGC,
          second.getBrown() + third.getBrown() + first.getGreen() + third.getGreen() + first
              .getClear() + second.getClear());
      Result cbg = new Result(Combination.CBG,
          second.getClear() + third.getClear() + first.getBrown() + third.getBrown() + first
              .getGreen() + second.getGreen());
      Result cgb = new Result(Combination.CGB,
          second.getClear() + third.getClear() + first.getGreen() + third.getGreen() + first
              .getBrown() + second.getBrown());
      Result gbc = new Result(Combination.GBC,
          second.getGreen() + third.getGreen() + first.getBrown() + third.getBrown() + first
              .getClear() + second.getClear());
      Result gcb = new Result(Combination.GCB,
          second.getGreen() + third.getGreen() + first.getClear() + third.getClear() + first
              .getBrown() + second.getBrown());

      List<Result> list = Arrays.asList(bcg, bgc, cbg, cgb, gbc, gcb);

      list.sort(Comparator.comparing(Result::getValue));

      Result res = list.stream().filter((result -> {
        return result.value == list.get(0).value;
      })).collect(Collectors.toList()).get(0);

      System.out.println(String.format("%s %d", res.combination.toString(), res.value));
    }

  }


  static class Bin {

    private long brown, green, clear;

    public Bin(String brown, String green, String clear) {
      this.brown = Integer.parseInt(brown);
      this.green = Integer.parseInt(green);
      this.clear = Integer.parseInt(clear);
    }

    public long getBrown() {
      return brown;
    }

    public long getClear() {
      return clear;
    }

    public long getGreen() {
      return green;
    }
  }


  static class Result {

    private byte priority;
    private long value;
    private Combination combination;


    public Result(Combination combination, long value) {
      this.combination = combination;
      this.value = value;

      switch (combination) {
        case BCG:
          priority = 0;
          break;
        case BGC:
          priority = 1;
          break;
        case CBG:
          priority = 2;
          break;
        case CGB:
          priority = 3;
          break;
        case GBC:
          priority = 4;
          break;
        case GCB:
          priority = 5;

      }
    }

    public long getValue() {
      return value;
    }
  }

  enum Combination {
    BCG, BGC, GBC, GCB, CBG, CGB;
  }

}
