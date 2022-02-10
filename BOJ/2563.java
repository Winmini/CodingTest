import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] board = new int[100][100];
		int N = Integer.parseInt(br.readLine());
		for (int k = 0; k < N; k++) {
			String[] input = br.readLine().split(" ");
			int r = Integer.parseInt(input[0]);
			int c = Integer.parseInt(input[1]);
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					board[r + i][c + j] = 1;
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (board[i][j] == 1)
					ans++;
			}
		}
		System.out.print(ans);
	}
}