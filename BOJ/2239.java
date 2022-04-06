import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	private static final StringBuilder sb = new StringBuilder();

	private static final int[][] board = new int[9][9];
	private static final List<int[]> pos = new ArrayList<>();
	private static final boolean[][] rowCheck = new boolean[9][10];
	private static final boolean[][] colCheck = new boolean[9][10];
	private static final boolean[][][] boxCheck = new boolean[3][3][10];

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 9; i++) {
			String[] st = br.readLine().split("");
			for (int j = 0; j < 9; j++) {
				board[i][j] = Integer.parseInt(st[j]);
				if (board[i][j] == 0)
					pos.add(new int[] {i, j});
			}
		}

		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				rowCheck[i][board[i][j]] = true;
				boxCheck[i / 3][j / 3][board[i][j]] = true;
				colCheck[j][board[i][j]] = true;
			}
		}

		solve(0, pos.size());
	}

	private static void solve(int now, int end) {
		if (now == end) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					sb.append(board[i][j]);
				}
				sb.append("\n");
			}
			System.out.println(sb);
			System.exit(0);
		}

		for (int i = 1; i <= 9; i++) {
			int[] nowPos = pos.get(now);
			int r = nowPos[0];
			int c = nowPos[1];
			if (!rowCheck[r][i] && !colCheck[c][i] && !boxCheck[r / 3][c/ 3][i]) {
				rowCheck[r][i] = true;
				colCheck[c][i] = true;
				boxCheck[r/3][c/3][i] = true;
				board[r][c] = i;
				solve(now + 1, end);
				rowCheck[r][i] = false;
				colCheck[c][i] = false;
				boxCheck[r/3][c/3][i] = false;
				board[r][c] = 0;
			}
		}
	}
}
