import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

	static final int[] dir_x = {0, 1, -1, 0};
	static final int[] dir_y = {1, 0, 0, -1};
	static Map<Character, Boolean> alpha;
	static int answer = 1;
	static char[][] board;
	static int R;
	static int C;

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		alpha = new HashMap<>();
		for (int i = 0; i <= 26; i++) {
			alpha.put((char)(i + 'A'), false);
		}

		String[] input = br.readLine().split(" ");
		R = Integer.parseInt(input[0]);
		C = Integer.parseInt(input[1]);
		board = new char[R][C];
		for (int i = 0; i < R; i++) {
			board[i] = br.readLine().toCharArray();
		}
		alpha.put(board[0][0], true);
		solve(0, 0, 1);
		System.out.println(answer);
	}

	public static void solve(int r, int c, int cnt) {
		for (int i = 0; i < 4; i++) {
			int cur_x = r + dir_x[i];
			int cur_y = c + dir_y[i];
			if (cur_x < 0 || cur_y < 0 || cur_x >= R || cur_y >= C)
				continue;
			if (alpha.get(board[cur_x][cur_y]))
				continue;
			alpha.put(board[cur_x][cur_y], true);
			answer = Math.max(answer, cnt + 1);
			solve(cur_x, cur_y, cnt + 1);
			alpha.put(board[cur_x][cur_y], false);
		}
	}
}