import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, -1, 0};
	private static final int[] dir_y = {1, 0, 0, -1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");

			int N = Integer.parseInt(br.readLine());
			char[][] board = new char[N][N];
			boolean[][] visited = new boolean[N][N];
			int[][] distance = new int[N][N];

			for (int i = 0; i < N; i++) {
				board[i] = br.readLine().toCharArray();
				Arrays.fill(distance[i], Integer.MAX_VALUE);
			}

			PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt((int[] i) -> i[0]));
			distance[0][0] = 0;
			queue.add(new int[] {0, 0, 0});

			while (!queue.isEmpty()) {
				int[] nPos = queue.poll();
				if (visited[nPos[1]][nPos[2]])
					continue;
				visited[nPos[1]][nPos[2]] = true;

				for (int i = 0; i < 4; i++) {
					int nx = nPos[1] + dir_x[i];
					int ny = nPos[2] + dir_y[i];
					if (nx < 0 || nx >= N || ny < 0 || ny >= N)
						continue;
					int newCost = (board[nx][ny] - '0') + nPos[0];
					if (distance[nx][ny] < newCost)
						continue;
					queue.add(new int[] {newCost, nx, ny});
					distance[nx][ny] = newCost;

				}
			}
			sb.append(distance[N-1][N-1]).append("\n");
		}
		System.out.println(sb);
	}
}


