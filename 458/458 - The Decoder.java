import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.util.ArrayList;

public class Main {


  public static void main(String[] args) throws IOException{

    ArrayList<Character> list = new ArrayList<>();
    DataInputStream in = new DataInputStream(System.in);
    DataOutputStream out = new DataOutputStream(System.out);

    int value;

    while ((value = in.read()) != -1){

      if (value == 10){
        // new line
        out.write(10);
      }

      if (value < 256 && value > 31){
        out.write(value - 7);
      }

      out.flush();
    }
  }

}
