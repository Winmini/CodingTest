import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Stack;

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

			int N = Integer.parseInt(br.readLine());
			int M = Integer.parseInt(br.readLine());
			LinkedList<Integer>[] up = new LinkedList[N + 1];
			LinkedList<Integer>[] down = new LinkedList[N + 1];
			for (int i = 0; i <= N; i++) {
				up[i] = new LinkedList<>();
				down[i] = new LinkedList<>();
			}

			for (int i = 0; i < M; i++) {
				String[] input = br.readLine().split(" ");
				int a = Integer.parseInt(input[0]);
				int b = Integer.parseInt(input[1]);

				up[a].add(b);
				down[b].add(a);
			}

			for (int i = 1; i <= N; i++) {
				int upNum = extracted(N, up, i);
				int downNum = extracted(N, down, i);
				if (upNum + downNum == N-1)
					answer++;
			}

			sb.append(answer).append("\n");

		}
		System.out.println(sb);
	}

	private static int extracted(int N, LinkedList<Integer>[] data, int i) {
		boolean[] visited = new boolean[N + 1];
		Stack<Integer> stack = new Stack();
		for (int u : data[i]) {
			stack.add(u);
			visited[u] = true;
		}
		while (!stack.isEmpty()) {
			int nxt = stack.pop();
			for(int u : data[nxt]){
				if(visited[u])
					continue;
				visited[u] = true;
				stack.add(u);
			}
		}
		int result = 0;
		for (int k = 1; k <= N; k++) {
			if (visited[k])
				result++;
		}
		return result;
	}
}

