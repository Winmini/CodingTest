import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {

	public static HashMap<Long, Long> dp = new HashMap<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] npq = br.readLine().split(" ");
		long n = Long.parseLong(npq[0]);
		long p = Long.parseLong(npq[1]);
		long q = Long.parseLong(npq[2]);
		dp.put(0L, 1L);
		System.out.println(recursive(n, p, q));
	}

	public static long recursive(long n, long p, long q) {
		if (dp.get(n) != null) {
			return dp.get(n);
		}
		dp.put(n, recursive(n / p, p, q) + recursive(n / q, p, q));
		return dp.get(n);
	}

}