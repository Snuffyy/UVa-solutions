package UVA10226;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class PR10226 {

    private static BufferedReader getFile()  {
        return new BufferedReader(new InputStreamReader(System.in));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = getFile();

        int numOfCases = Integer.parseInt(br.readLine());
        br.readLine();

        for (int i = 0; i < numOfCases; i++) {

            if (i > 0){
                System.out.println();
            }

            Map<String, Integer> map = new HashMap<>();
            List<String> species = new LinkedList<>();

            int total = 0;

            String line;

            while ((line = br.readLine()) != null) {

                if (line.isEmpty()) {
                    break;
                }

                if (map.containsKey(line)) {
                    map.put(line, map.get(line) + 1);
                } else {
                    map.put(line, 1);
                    species.add(line);
                }

                total++;
            }

            Collections.sort(species);

            float finalTotal = total;

            species.forEach((item) ->System.out.printf("%s %.04f\n", item, map.get(item) * 100 / finalTotal));
        }
    }

}
