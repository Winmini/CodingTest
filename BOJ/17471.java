import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	private static final StringBuilder sb = new StringBuilder();

	private static final List<int[]> graph = new ArrayList<>();
	private static int N;
	private static int[] people;
	private static boolean[] visited;
	private static int answer = Integer.MAX_VALUE;
	private static int total = 0;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		people = new int[N + 1];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			people[i] = Integer.parseInt(st.nextToken());
			total += people[i];
		}
		graph.add(new int[] {});
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int[] tmp = new int[k];
			for (int j = 0; j < k; j++) {
				tmp[j] = Integer.parseInt(st.nextToken());
			}
			graph.add(tmp);
		}

		visited = new boolean[N + 1];
		visited[0] = true;

		for (int i = 1; i <= N/2; i++) {
			solve(0, 0, i, N);
		}

		if (answer == Integer.MAX_VALUE)
			System.out.println(-1);
		else
			System.out.println(answer);
	}

	private static void solve(int start, int cnt, int n, int end) {
		if (cnt == n) {

			int a = canUnion(true);
			int b = canUnion(false);

			if (a + b == N) {
				int na = 0;
				for (int i = 1; i <= N; i++) {
					if(visited[i])
						na += people[i];
				}

				answer = Math.min(answer, Math.abs(total - 2*na));
			}
			return;
		}
		for (int i = start + 1; i <= end; i++) {
			visited[i] = true;
			solve(i, cnt + 1, n, end);
			visited[i] = false;
		}
	}

	private static int canUnion(boolean a) {
		int init = 0;
		for (int i = 1; i <= N; i++) {
			if (visited[i] == a)
				continue;
			init = i;
			break;
		}
		Stack<Integer> stack = new Stack<>();
		stack.add(init);
		boolean[] tmpVisited = visited.clone();
		tmpVisited[init] = a;
		int num = 0;

		while (!stack.isEmpty()) {
			int now = stack.pop();
			num++;
			for (int nxt : graph.get(now)) {
				if (visited[nxt] == a || tmpVisited[nxt] == a)
					continue;
				tmpVisited[nxt] = a;
				stack.add(nxt);
			}
		}
		return num;
	}

}
