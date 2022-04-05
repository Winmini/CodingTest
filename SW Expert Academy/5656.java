
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {
	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, -1, 0};
	private static final int[] dir_y = {1, 0, 0, -1};
	private static int[][] board;
	private static int answer = Integer.MAX_VALUE;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			answer = Integer.MAX_VALUE;

			String[] input = br.readLine().split(" ");
			int N = Integer.parseInt(input[0]);
			int W = Integer.parseInt(input[1]);
			int H = Integer.parseInt(input[2]);
			board = new int[H][W];
			for (int i = 0; i < H; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < W; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			solve(0, N, W, H, board);

			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}

	public static void solve(int start, int end, int wide, int height, int[][] nextBoard) {
		if (start == end) {
			int ans = 0;
			for (int i = 0; i < height; i++) {
				for (int j = 0; j < wide; j++) {
					if (nextBoard[i][j] != 0) {
						ans++;
					}
				}
			}

			answer = Math.min(answer, ans);
			return;
		}

		boolean next = false;

		for (int i = 0; i < wide; i++) {
			int[][] tmpBoard = new int[height][wide];

			for (int t1 = 0; t1 < height; t1++) {
				System.arraycopy(nextBoard[t1], 0, tmpBoard[t1], 0, wide);
			}
			int[] init = null;
			for (int j = 0; j < height; j++) {
				if (tmpBoard[j][i] != 0) {
					init = new int[] {j, i, tmpBoard[j][i] - 1};
					tmpBoard[j][i] = 0;
					break;
				}
			}
			if (init == null)
				continue;

			Stack<int[]> stack = new Stack<>();
			stack.add(init);
			while (!stack.isEmpty()) {
				int[] pos = stack.pop();
				int x = pos[0];
				int y = pos[1];
				int c = pos[2];
				for (int j = 0; j < 4; j++) {
					int tx = x;
					int ty = y;
					for (int k = 0; k < c; k++) {
						tx += dir_x[j];
						ty += dir_y[j];
						if (tx < 0 || tx >= height || ty < 0 || ty >= wide)
							break;
						if (tmpBoard[tx][ty] == 1) {
							tmpBoard[tx][ty] = 0;
						} else if (tmpBoard[tx][ty] >= 2) {
							stack.add(new int[] {tx, ty, tmpBoard[tx][ty] - 1});
							tmpBoard[tx][ty] = 0;
						}
					}
				}
			}

			for (int t1 = wide - 1; t1 >= 0; t1--) {
				for (int t2 = height - 1; t2 >= 0; t2--) {
					if (tmpBoard[t2][t1] != 0)
						continue;
					int[] tmp = null;
					for (int t3 = t2 - 1; t3 >= 0; t3--) {
						if (tmpBoard[t3][t1] != 0) {
							tmp = new int[] {t3, t1};
							break;
						}
					}
					if (tmp != null) {
						tmpBoard[t2][t1] = tmpBoard[tmp[0]][tmp[1]];
						tmpBoard[tmp[0]][tmp[1]] = 0;
					} else {
						break;
					}
				}
			}

			next = true;
			solve(start + 1, end, wide, height, tmpBoard);
		}
		if (!next)
			answer = 0;
	}
}
