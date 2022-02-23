import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	static int[] dir_x = {0, 1, -1, 0};
	static int[] dir_y = {1, 0, 0, -1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		char[][] board = new char[N][N];
		for (int i = 0; i < N; i++) {
			board[i] = br.readLine().toCharArray();
		}

		Stack<int[]> stack = new Stack<>();
		boolean[][] visited = new boolean[N][N];
		int n_ans = solve(N, board, visited, stack);

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == 'R')
					board[i][j] = 'G';
			}
		}

		visited = new boolean[N][N];
		int s_ans = solve(N, board, visited, stack);

		System.out.println(n_ans + " " + s_ans);

	}

	private static int solve(int N, char[][] board, boolean[][] visited, Stack<int[]> stack) {
		int ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (visited[i][j])
					continue;
				visited[i][j] = true;
				ans++;
				stack.add(new int[] {i, j});
				while (!stack.isEmpty()) {
					int[] pos = stack.pop();
					int x = pos[0];
					int y = pos[1];
					for (int k = 0; k < 4; k++) {
						int cur_x = x + dir_x[k];
						int cur_y = y + dir_y[k];
						if (cur_x < 0 || cur_y < 0 || cur_x >= N || cur_y >= N)
							continue;
						if (visited[cur_x][cur_y] || board[cur_x][cur_y] != board[x][y])
							continue;
						visited[cur_x][cur_y] = true;
						stack.add(new int[] {cur_x, cur_y});
					}
				}
			}
		}
		return ans;
	}
}