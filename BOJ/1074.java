
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static int N;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		int r = Integer.parseInt(input[1]);
		int c = Integer.parseInt(input[2]);
		System.out.println((int)bc(r, c, 0));
	}

	public static double bc(double r, double c, int n) {
		if (n == N - 1)
			return r * 2 + c;
		double mp = Math.pow(2, N - n - 1);
		if (r >= mp && c >= mp)
			return bc(r  - mp, c - mp, n + 1) + mp * mp * 3;
		else if (r >= Math.pow(2, N - n - 1))
			return bc(r  - mp, c, n + 1) + mp * mp * 2;
		else if (c >= Math.pow(2, N - n - 1))
			return bc(r, c - mp, n + 1) + mp * mp;
		else
			return bc(r, c, n + 1);
	}
}