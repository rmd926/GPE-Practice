// UVA / ZJ style: read integers until EOF, print "n!" and n! on next line.
// Uses BigInteger for arbitrary precision.

import java.io.*;
import java.math.BigInteger;

public class Main {
    static BigInteger factorial(int n) {
        BigInteger f = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            f = f.multiply(BigInteger.valueOf(i));
        }
        return f;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;       // 可省略，防空行
            int n = Integer.parseInt(line);
            out.append(n).append("!\n");
            out.append(factorial(n)).append('\n');
        }
        System.out.print(out.toString());
    }
}
