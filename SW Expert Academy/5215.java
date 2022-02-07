
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			String[] input = br.readLine().split(" ");
			int N = Integer.parseInt(input[0]);
			int L = Integer.parseInt(input[1]);
			int[][] burger = new int[N + 1][L + 1];
			for (int i = 1; i < N + 1; i++) {
				String[] in = br.readLine().split(" ");
				for (int j = 1; j < L + 1; j++) {
					int taste = Integer.parseInt(in[0]);
					int cal = Integer.parseInt(in[1]);
					if (j < cal)
						burger[i][j] = burger[i-1][j];
					else
						burger[i][j] = Math.max(burger[i-1][j], burger[i-1][j-cal] + taste);
				}
			}
			sb.append("#").append(tc).append(" ").append(burger[N][L]).append("\n");
		}

		System.out.print(sb);
	}

}