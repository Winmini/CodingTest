import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			int N = Integer.parseInt(br.readLine());
			String[] input = br.readLine().split(" ");
			if (N % 2 == 0) {
				for (int i = 0; i < N / 2; i++) {
					sb.append(input[i]).append(" ").append(input[N / 2 + i]).append(" ");
				}
			} else {
				for (int i = 0; i < N / 2; i++) {
					sb.append(input[i]).append(" ").append(input[N / 2 + i + 1]).append(" ");
				}
				sb.append(input[N / 2]);
			}
			sb.append("\n");
		}
		System.out.print(sb);
	}
}