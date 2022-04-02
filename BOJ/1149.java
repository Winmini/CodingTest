import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		int[][] dp = new int[N+1][3];
		String[] init = br.readLine().split(" ");
		dp[1][0] = Integer.parseInt(init[0]);
		dp[1][1] = Integer.parseInt(init[1]);
		dp[1][2] = Integer.parseInt(init[2]);

		for (int i = 2; i <= N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + Integer.parseInt(st.nextToken());
			dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + Integer.parseInt(st.nextToken());
			dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + Integer.parseInt(st.nextToken());
		}
		System.out.println(Math.min(Math.min(dp[N][0], dp[N][1]), dp[N][2]));
	}
}