import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, 0, -1};
	private static final int[] dir_y = {1, 0, -1, 0};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(in.readLine());
		Map<Character, Integer> dir = new HashMap<Character, Integer>() {{
			put('>', 0);
			put('v', 1);
			put('<', 2);
			put('^', 3);
			put('R', 0);
			put('D', 1);
			put('L', 2);
			put('U', 3);
		}};
		Map<Integer,Character> rDir = new HashMap<Integer,Character>() {{
			put(0, '>');
			put(1, 'v');
			put(2, '<');
			put(3, '^');
		}};

		for (int tc = 1; tc <= testCase; tc++) {
			String[] input = in.readLine().split(" ");
			int H = Integer.parseInt(input[0]);
			int W = Integer.parseInt(input[1]);
			char[][] board = new char[H][W];
			for (int i = 0; i < H; i++) {
				board[i] = in.readLine().toCharArray();
			}
			in.readLine();
			char[] commands = in.readLine().toCharArray();
			Pos tank = null;
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					if (board[i][j] == '^' || board[i][j] == 'v' || board[i][j] == '<' || board[i][j] == '>') {
						tank = new Pos(i, j, dir.get(board[i][j]));
						board[i][j] = '.';
					}
				}
			}

			for (char cmd : commands) {
				if (cmd == 'S') {
					int cur_x = tank.getX();
					int cur_y = tank.getY();
					while (true) {
						cur_x += dir_x[tank.getD()];
						cur_y += dir_y[tank.getD()];
						if (cur_x < 0 || cur_y < 0 || cur_x >= H || cur_y >= W)
							break;
						if (board[cur_x][cur_y] == '#')
							break;
						if (board[cur_x][cur_y] == '*') {
							board[cur_x][cur_y] = '.';
							break;
						}
					}
				} else {
					tank.setD(dir.get(cmd));
					int move_x = tank.getX() + dir_x[tank.getD()];
					int move_y = tank.getY() + dir_y[tank.getD()];
					if (move_x < 0 || move_y < 0 || move_x >= H || move_y >= W)
						continue;
					if (board[move_x][move_y] == '.') {
						tank.setX(move_x);
						tank.setY(move_y);
					}
				}
			}
			board[tank.getX()][tank.getY()] = rDir.get(tank.getD());
			sb.append("#");
			sb.append(tc);
			sb.append(" ");
			Arrays.stream(board)
				.forEach(arr -> {
					sb.append(String.valueOf(arr));
					sb.append("\n");});
		}

		System.out.print(sb);
	}

	static class Pos {
		private int x;
		private int y;
		private int d;

		Pos(int x, int y, int d) {
			this.x = x;
			this.y = y;
			this.d = d;
		}

		public int getY() {
			return y;
		}

		public void setY(int y) {
			this.y = y;
		}

		public int getX() {
			return x;
		}

		public void setX(int x) {
			this.x = x;
		}

		public int getD() {
			return d;
		}

		public void setD(int d) {
			this.d = d;
		}
	}

}