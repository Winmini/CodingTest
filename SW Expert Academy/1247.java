import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	private static int N;
	static boolean[] visited;
	static int answer;
	static List<int[]> list;
	static int com_x;
	static int com_y;

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			answer = Integer.MAX_VALUE;
			sb.append("#").append(tc).append(" ");
			N = Integer.parseInt(br.readLine());
			list = new ArrayList<>(N);
			visited = new boolean[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			com_x = Integer.parseInt(st.nextToken());
			com_y = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			for (int j = 0; j < N; j++) {
				int t_x = Integer.parseInt(st.nextToken());
				int t_y = Integer.parseInt(st.nextToken());
				list.add(new int[] {t_x, t_y});
			}
			solve(0, 0, x, y);
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}

	public static void solve(int n, int dis, int c_x, int c_y) {
		if (n == N) {
			dis += Math.abs(com_x - c_x) + Math.abs(com_y - c_y);
			answer = Math.min(answer, dis);
			return;
		}
		for (int i = 0; i < N; i++) {
			if (visited[i])
				continue;
			int[] pos = list.get(i);
			int n_x = pos[0];
			int n_y = pos[1];
			int n_dis = dis + Math.abs(n_x - c_x) + Math.abs(n_y - c_y);
			if (n_dis > answer)
				continue;
			visited[i] = true;
			solve(n + 1, n_dis, n_x, n_y);
			visited[i] = false;
		}
	}
}