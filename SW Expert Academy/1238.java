import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int testCase = 10;
		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			String[] input = br.readLine().split(" ");
			ArrayList<ArrayList<Integer>> list = new ArrayList<>();
			for (int i = 0; i < 101; i++) {
				list.add(i, new ArrayList<>());
			}
			int N = Integer.parseInt(input[0]) / 2;
			int start = Integer.parseInt(input[1]);
			boolean[] visited = new boolean[101];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				list.get(from).add(to);
			}

			Queue<int[]> queue = new LinkedList<>();
			queue.add(new int[] {start, 0});
			visited[start] = true;
			int answer = start;
			int dis = 0;

			while (!queue.isEmpty()) {
				int[] now = queue.poll();

				if (now[1] > dis) {
					answer = now[0];
					dis = now[1];
				} else if (now[1] == dis && answer < now[0]) {
					answer = now[0];
				}

				for (int nxt : list.get(now[0])) {
					if (visited[nxt])
						continue;
					visited[nxt] = true;
					queue.add(new int[] {nxt, now[1] + 1});
				}
			}
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}
}