import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

	static class Node {
		int to, cost;
		Node link;

		public Node(int to, int cost, Node link) {
			this.to = to;
			this.cost = cost;
			this.link = link;
		}
	}

	static class Vertex implements Comparable<Vertex> {
		int no, distance;

		public Vertex(int no, int distance) {
			this.no = no;
			this.distance = distance;
		}

		@Override
		public int compareTo(Vertex o) {
			return this.distance - o.distance;
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String[] input = br.readLine().split(" ");
		int V = Integer.parseInt(input[0]);
		boolean[] visited = new boolean[V + 1];
		int[] dist = new int[V + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		int start = Integer.parseInt(br.readLine());

		Node[] graph = new Node[V + 1];

		for (int i = 0; i < Integer.parseInt(input[1]); i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			graph[u] = new Node(v, w, graph[u]);
		}
		dist[start] = 0;
		PriorityQueue<Vertex> queue = new PriorityQueue<>();
		queue.offer(new Vertex(start, 0));

		Vertex now;

		while (!queue.isEmpty()){
			now = queue.poll();
			if (visited[now.no])
				continue;
			visited[now.no] = true;
			for (Node node = graph[now.no]; node != null; node= node.link){
				int update = node.cost + now.distance;
				if (dist[node.to] > update){
					queue.offer(new Vertex(node.to, update));
					dist[node.to] = update;
				}
			}
		}

		for (int i = 1; i <= V; i++) {
			if (dist[i] == Integer.MAX_VALUE)
				sb.append("INF\n");
			else
				sb.append(dist[i]).append("\n");
		}
		System.out.println(sb);
	}
}