
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static final List<Integer> visited = new LinkedList<>();
	private static int N;
	private static int M;
	private static int D;
	private static List<int[]>[] enemy;
	private static int answer = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		int[][] board = new int[N][M];

		enemy = new LinkedList[3];
		for (int i = 0; i < 3; i++) {
			enemy[i] = new LinkedList<>();
		}

		int num = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				if (board[i][j] == 1) {
					enemy[0].add(new int[] {i, j, num});
					enemy[1].add(new int[] {i, j, num});
					enemy[2].add(new int[] {i, j, num});
					num++;
				}
			}
		}
		solve(-1, M, 0, enemy[0].size());
		System.out.println(answer);
	}

	private static void solve(int now, int end, int cnt, int size) {
		if (cnt == 3) {
			Set<Integer> killed = new HashSet<>();
			for (int i = 0; i < 3; i++) {
				int t = i;
				enemy[i].sort(Comparator.comparingInt((int[] k) -> (N - k[0] + Math.abs(k[1] - visited.get(t))))
					.thenComparingInt((int[] k) -> k[1]));
			}

			int[] pos = new int[3];
			for (int t = 0; t <= N; t++) {
				Set<Integer> tmp = new HashSet<>();
				for (int j = 0; j < 3; j++) {
					if (pos[j] == size)
						continue;
					int[] e = enemy[j].get(pos[j]);
					int row = N - e[0];
					if (killed.contains(e[2]) || row <= t) {
						pos[j]++;
						j--;
						continue;
					}
					int dis = row + Math.abs(visited.get(j) - e[1]) - t;
					if (dis <= D) {
						tmp.add(e[2]);
						pos[j]++;
					}
				}
				killed.addAll(tmp);
			}
			answer = Math.max(answer, killed.size());
			return;
		}
		for (int i = now + 1; i < end; i++) {
			visited.add(i);
			solve(i, end, cnt + 1, size);
			visited.remove(Integer.valueOf(i));
		}
	}
}

