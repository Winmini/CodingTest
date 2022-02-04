
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			String[] input = br.readLine().split(" ");
			int N = Integer.parseInt(input[0]);
			int M = Integer.parseInt(input[1]);

			Integer[][] board = new Integer[N][N];
			for (int i = 0; i < N; i++) {
				board[i] = Arrays.stream(br.readLine().split(" "))
					.map(Integer::parseInt)
					.toArray(Integer[]::new);
			}

			int ans = 0;
			for (int i = 0; i < N - M + 1; i++) {
				for (int j = 0; j < N - M + 1; j++) {
					int tmp = 0;
					for (int x = 0; x < M; x++) {
						for (int y = 0; y < M; y++) {
							tmp += board[i+x][j+y];
						}
					}
					ans = Math.max(ans, tmp);
				}
			}

			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}

		System.out.print(sb);
	}

}