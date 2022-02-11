
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {1, 0, -1, 0};
	private static final int[] dir_y = {0, -1, 0, 1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			int N = Integer.parseInt(br.readLine());

			int[][] board = new int[N][N];
			for (int i = 0; i < N; i++) {
				String[] input = br.readLine().split(" ");
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(input[j]);
				}
			}

			Queue<int[]> queue = new LinkedList<>();
			int[] answer = {0, 0};
			boolean[][] visited = new boolean[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (visited[i][j])
						continue;
					visited[i][j] = true;
					queue.add(new int[] {i, j, 1});
					queue.add(new int[] {i, j, -1});
					int minValue = board[i][j];
					int size = -1;
					while (!queue.isEmpty()) {
						int[] pos = queue.poll();
						size += 1;
						for (int k = 0; k < 4; k++) {
							int cur_x = pos[0] + dir_x[k];
							int cur_y = pos[1] + dir_y[k];
							if (cur_x < 0 || cur_y < 0 || cur_x >= N || cur_y >= N)
								continue;
							if (visited[cur_x][cur_y])
								continue;
							if (board[pos[0]][pos[1]] + pos[2] == board[cur_x][cur_y]) {
								visited[cur_x][cur_y] = true;
								queue.add(new int[] {cur_x, cur_y, pos[2]});
								if (pos[2] == -1)
									minValue =  board[cur_x][cur_y];
							}
						}
					}
					if (answer[1] < size) {
						answer[1] = size;
						answer[0] = minValue;
					} else if (answer[1] == size && answer[0] > board[i][j]) {
						answer[0] = minValue;
					}
				}
			}

			sb.append(answer[0]).append(" ").append(answer[1]).append("\n");
		}
		System.out.print(sb);
	}
}