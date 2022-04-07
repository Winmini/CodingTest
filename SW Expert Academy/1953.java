import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, -1, 0};
	private static final int[] dir_y = {1, 0, 0, -1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Map<Integer, int[]> tunnel = new HashMap<>();
		tunnel.put(1, new int[] {0, 1, 2, 3});
		tunnel.put(2, new int[] {1, 2});
		tunnel.put(3, new int[] {0, 3});
		tunnel.put(4, new int[] {0, 2});
		tunnel.put(5, new int[] {0, 1});
		tunnel.put(6, new int[] {1, 3});
		tunnel.put(7, new int[] {2, 3});

		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			int answer = 0;

			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int R = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());

			int[][] board = new int[N][M];
			boolean[][] visited = new boolean[N][M];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < M; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			Queue<int[]> queue = new LinkedList<>();
			queue.add(new int[] {R, C, 1});
			visited[R][C] = true;

			while (!queue.isEmpty()) {
				int[] nextPos = queue.poll();
				answer++;
				if (nextPos[2] == L)
					continue;
				for (int i : tunnel.get(board[nextPos[0]][nextPos[1]])) {
					int nx = nextPos[0] + dir_x[i];
					int ny = nextPos[1] + dir_y[i];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M)
						continue;
					if (visited[nx][ny])
						continue;
					if (board[nx][ny] != 0) {
						boolean possible = false;
						for (int j : tunnel.get(board[nx][ny])) {
							if (nx + dir_x[j] == nextPos[0] && ny + dir_y[j] == nextPos[1]) {
								possible = true;
								break;
							}
						}
						if (possible) {
							queue.add(new int[] {nx, ny, nextPos[2] + 1});
							visited[nx][ny] = true;
						}
					}
				}
			}

			sb.append(answer).append("\n");

		}
		System.out.println(sb);
	}
}


