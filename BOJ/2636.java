import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, -1, 0};
	private static final int[] dir_y = {1, 0, 0, -1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int r = Integer.parseInt(input[0]);
		int c = Integer.parseInt(input[1]);
		int answer = 0;

		int[][] board = new int[r][c];
		boolean[][] visited = new boolean[r][c];

		for (int i = 0; i < r; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < c; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				if (board[i][j] == 1)
					answer++;
			}
		}

		Stack<int[]> stack = new Stack<>();
		stack.add(new int[] {0, 0});

		Stack<int[]> nextStack = new Stack<>();

		int day = 0;
		while (answer > 0) {
			day += 1;
			while (!stack.isEmpty()) {
				int[] pos = stack.pop();
				int x = pos[0];
				int y = pos[1];

				for (int i = 0; i < 4; i++) {
					int nx = x + dir_x[i];
					int ny = y + dir_y[i];
					if (nx < 0 || nx >= r || ny < 0 || ny >= c)
						continue;
					if (visited[nx][ny])
						continue;
					visited[nx][ny] = true;

					if (board[nx][ny] == 1) {
						nextStack.add(new int[]{nx, ny});
						board[nx][ny] = 0;
					} else {
						stack.add(new int[] {nx, ny});
					}
				}
			}
			answer -= nextStack.size();
			while (!nextStack.isEmpty())
				stack.add(nextStack.pop());
		}
		System.out.println(day);
		System.out.println(stack.size());
	}

}
