import java.util.EmptyStackException;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.util.Stack;

public class Main {


  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = Integer.parseInt(sc.nextLine());

    String line;
    String result;
    Stack<Character> stack;

    for (int i = 0; i < n; i++) {

      result = null;
      stack = new Stack<>();

      line = sc.nextLine();

      for (int j = 0; j < line.length(); j++) {
        char chr = line.charAt(j);

        try {
          if (chr == '(' || chr == '[') {
            stack.push(chr);
          } else if (chr == ')') {
            if (stack.lastElement() == '(') {
              stack.pop();
            } else {
              result = "No";
            }
          } else if (chr == ']') {
            if (stack.lastElement() == '[') {
              stack.pop();
            } else {
              result = "No";
            }
          }
        } catch (EmptyStackException | NoSuchElementException e) {
          result = "No";
        }
      }

      if (result != null) {
        System.out.println(result);
        continue;
      }

      System.out.println(stack.size() == 0 ? "Yes" : "No");
    }
    sc.close();
  }
}