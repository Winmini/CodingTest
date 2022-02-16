
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static int[][] board;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		board = new int[N][N];
		for (int i = 0; i < N; i++) {
			String[] input = br.readLine().split("");
			for (int j = 0; j < N; j++){
				board[i][j] = Integer.parseInt(input[j]);
			}
		}
		sc(0, 0, N);
		System.out.println(sb);
	}

	private static void sc(int x, int y, int size) {

		if (size == 0) {
			return;
		}
		int sum = 0;
		for (int i = x; i < x + size; i++) {
			for (int j = y; j < y + size; j++) {
				sum += board[i][j];
			}
		}
		if (sum == 0) {
			sb.append(0);
		} else if (sum == size * size) {
			sb.append(1);
		} else {
			sb.append("(");
			sc(x, y, size / 2);
			sc(x, y + size / 2, size / 2);
			sc(x + size / 2, y, size / 2);
			sc(x + size / 2, y + size / 2, size / 2);
			sb.append(")");
		}

	}

}