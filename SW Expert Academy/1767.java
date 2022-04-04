import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, -1, 0};
	private static final int[] dir_y = {1, 0, 0, -1};
	private static int[][] board;
	private static boolean[][] visited;
	private static int[] answer;
	private static int N;
	private static List<int[]> core;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int testCase = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			answer = new int[] {0, Integer.MAX_VALUE};
			core = new ArrayList<>();
			N = Integer.parseInt(br.readLine().trim());
			board = new int[N][N];
			visited = new boolean[N][N];

			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					if (board[i][j] == 1) {
						core.add(new int[] {i, j});
						visited[i][j] = true;
					}
				}
			}
			solve(0, core.size(), 0, 0);
			sb.append(answer[1]).append("\n");
		}
		System.out.println(sb);
	}

	public static void solve(int start, int end, int num, int size) {
		if (start == end) {
			if (answer[0] < num){
				answer[0] = num;
				answer[1] = size;
				return;
			}
			if (answer[0] == num){
				answer[1] = Math.min(answer[1], size);
				return;
			}
		}
		if (num + end - start < answer[0])
			return;

		for (int i = 0; i < 4; i++) {
			int x = core.get(start)[0];
			int y = core.get(start)[1];
			boolean chk = false;
			List<int[]> tmpVisited = new ArrayList<>();
			while (true) {
				x += dir_x[i];
				y += dir_y[i];
				if (x < 0 || x >= N || y < 0 || y >= N) {
					chk = true;
					break;
				}
				if (visited[x][y])
					break;
				visited[x][y] = true;
				tmpVisited.add(new int[] {x, y});
			}
			if (chk) {
				solve(start + 1, end, num + 1, size + tmpVisited.size());
			}
			for (int[] ints : tmpVisited) {
				visited[ints[0]][ints[1]] = false;
			}
		}
		solve(start + 1, end, num, size);
	}
}
