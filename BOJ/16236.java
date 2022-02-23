import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int[] dir_x = {0, 1, 0, -1};
	static int[] dir_y = {1, 0, -1, 0};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] pos = new int[2];
		int[][] board = new int[N][N];
		boolean[][] visited = new boolean[N][N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				if (board[i][j] == 9) {
					pos = new int[] {i, j};
					board[i][j] = 0;
				}
			}
		}
		visited[pos[0]][pos[1]] = true;
		int answer = 0;
		int size = 2;
		int eat = 0;

		// 상어가 먹을 수 있는 물고기를 담은 우선순위 큐
		PriorityQueue<int[]> nextQueue = new PriorityQueue<>(Comparator
			.comparingInt((int[] i) -> i[2]) // 거리가 우선
			.thenComparing((int[] i) -> i[0]) // 행이 그 다음
			.thenComparing((int[] i) -> i[1])); // 열이 그 다음

		Queue<int[]> queue = new LinkedList<>();
		nextQueue.add(new int[] {pos[0], pos[1], 0});

		while (!nextQueue.isEmpty()) {
			int[] n_pos = nextQueue.poll();
			queue.add(new int[] {n_pos[0], n_pos[1], 0});
			nextQueue.clear();

			while (!queue.isEmpty()) {
				int[] t_pos = queue.poll();
				int x = t_pos[0];
				int y = t_pos[1];
				for (int i = 0; i < 4; i++) {
					int cur_x = x + dir_x[i];
					int cur_y = y + dir_y[i];
					if (cur_x < 0 || cur_y < 0 || cur_x >= N || cur_y >= N)
						continue;
					if (size < board[cur_x][cur_y] || visited[cur_x][cur_y])
						continue;
					if (board[cur_x][cur_y] != 0 && board[cur_x][cur_y] != size) {
						nextQueue.add(new int[] {cur_x, cur_y, t_pos[2] + 1});
					} else {
						visited[cur_x][cur_y] = true;
						queue.add(new int[] {cur_x, cur_y, t_pos[2] + 1}); // 못 먹으면 마저 탐색
					}
				}
			}

			if (!nextQueue.isEmpty()) { // 먹을 게 있다면 먹고 사이즈 조정
				int[] tmp = nextQueue.peek();
				board[tmp[0]][tmp[1]] = 0;
				answer += tmp[2];
				visited = new boolean[N][N];
				visited[tmp[0]][tmp[1]] = true;
				eat++;
				if (eat == size) {
					size++;
					eat = 0;
				}
			}
		}
		System.out.println(answer);
	}
}