import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class Main {

	static Map<Character, Boolean> alpha;
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static boolean[] visited;
	static int N;
	static int M;

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);
		int V = Integer.parseInt(input[2]);
		visited = new boolean[N + 1];
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		for (int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>(N + 1));
		}

		for (int i = 0; i < M; i++) {
			String[] tmp = br.readLine().split(" ");
			graph.get(Integer.parseInt(tmp[0])).add(Integer.parseInt(tmp[1]));
			graph.get(Integer.parseInt(tmp[1])).add(Integer.parseInt(tmp[0]));
		}

		for (int i = 1; i <= N; i++) {
			graph.get(i).sort(Comparator.naturalOrder());
		}

		sb.append(V).append(" ");
		visited[V] = true;
		dfs(graph, V);

		Arrays.fill(visited, false);
		sb.append("\n");
		visited[V] = true;
		Queue<Integer> queue = new LinkedList<>();
		queue.add(V);
		while (!queue.isEmpty()) {
			int now = queue.poll();
			sb.append(now).append(" ");
			for (int i : graph.get(now)) {
				if(visited[i])
					continue;
				visited[i] = true;
				queue.add(i);
			}
		}

		System.out.println(sb);
	}

	public static void dfs(ArrayList<ArrayList<Integer>> graph, int now) {
		for (int i : graph.get(now)) {
			if (visited[i])
				continue;
			visited[i] = true;
			sb.append(i).append(" ");
			dfs(graph, i);
		}

	}
}
