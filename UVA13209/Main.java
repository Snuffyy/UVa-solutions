package UVA13209;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static void calculate(int prime){

        int remainder = 10 % prime;

        StringBuilder sb = new StringBuilder("0.");

        do {
            sb.append(remainder / prime);
            remainder = 10 * (remainder % prime);
        }
        while (remainder != 10);

        System.out.println(sb.toString());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0; i < cases; i++) {

            calculate(Integer.parseInt(br.readLine()));
        }
    }

}
