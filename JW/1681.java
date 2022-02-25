import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[][] board;
	static int[][] dp;
	static int INF = 999999999;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine().trim());
		board = new int[N][N];
		dp = new int[N][1 << N];
		for (int i = 0; i < N; i++) {
			Arrays.fill(dp[i], INF);
		}

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		System.out.println(TSP(0, 1));
	}

	public static int TSP(int now, int flag) {
		if (flag == (1 << N) - 1) {
			if (board[now][0] == 0)
				return INF;
			return board[now][0];
		}

		if (dp[now][flag] != INF)
			return dp[now][flag];

		for (int i = 0; i < N; i++) {
			if ((flag & (1 << i)) != 0 || board[now][i] == 0)
				continue;
			dp[now][flag] = Math.min(dp[now][flag], TSP(i, flag | (1 << i)) + board[now][i]);
		}
		return dp[now][flag];

	}

}