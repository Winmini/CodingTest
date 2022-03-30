
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {1, 1, -1, -1, 2, 2, -2, -2, 0, 1, -1, 0};
	private static final int[] dir_y = {2, -2, 2, -2, 1, -1, 1, -1, 1, 0, 0, -1};
	// private static final int[] horse_x = {1, 1, -1, -1, 2, 2, -2, -2};
	// private static final int[] horse_y = {2, -2, 2, -2, 1, -1, 1, -1};
	private static int[][] board;
	private static boolean[][][] visited;
	private static int answer = -1;
	private static int R;
	private static int C;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int K = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split(" ");
		C = Integer.parseInt(input[0]);
		R = Integer.parseInt(input[1]);

		board = new int[R][C];
		visited = new boolean[R][C][K+1];
		visited[0][0][0] = true;
		for (int i = 0; i < R; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < C; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {0, 0, 0, 0});

		while (!queue.isEmpty()){
			int[] pos = queue.poll();
			if (pos[0] == R-1 && pos[1] == C-1){
				answer = pos[3];
				break;
			}
			int p;
			if (pos[2] < K)
				p = 0;
			else
				p = 8;
			for (int i = p; i < 12; i++) {
				int nx = pos[0] + dir_x[i];
				int ny = pos[1] + dir_y[i];
				if (nx < 0 || nx >= R || ny < 0 || ny >= C)
					continue;
				if (board[nx][ny] == 1)
					continue;
				if (i < 8 && visited[nx][ny][pos[2] + 1])
					continue;
				if (i >= 8 && visited[nx][ny][pos[2]])
					continue;
				if (i < 8) {
					visited[nx][ny][pos[2]+1]= true;
					queue.add(new int[] {nx, ny, pos[2] + 1, pos[3] + 1});
				} else {
					visited[nx][ny][pos[2]] = true;
					queue.add(new int[] {nx, ny, pos[2], pos[3] + 1});
				}
			}
		}
		System.out.println(answer);
	}

}
