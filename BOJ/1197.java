import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	private static final StringBuilder sb = new StringBuilder();
	public static int[] parent;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		long answer = 0;
		List<int[]> arr = new ArrayList<>();
		String[] input = br.readLine().split(" ");
		int V = Integer.parseInt(input[0]);
		int E = Integer.parseInt(input[1]);
		parent = new int[V + 1];
		Arrays.setAll(parent, i -> i);

		for (int i = 0; i < E; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());

			arr.add(new int[] {C, A, B});
		}

		arr.sort(Comparator.comparingInt(i -> i[0]));

		for (int i = 0; V > 1; i++) {
			if (find(arr.get(i)[1]) != find(arr.get(i)[2])){
				V--;
				union(arr.get(i)[1], arr.get(i)[2]);
				answer += arr.get(i)[0];
			}
		}
		System.out.println(answer);
	}

	public static int find(int x) {
		if (x == parent[x])
			return x;
		return parent[x] = find(parent[x]);
	}

	public static void union(int x, int y) {
		x = find(x);
		y = find(y);

		if (x != y)
			parent[y] = x;
	}

}
