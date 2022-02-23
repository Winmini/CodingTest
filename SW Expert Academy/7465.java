import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int[] parents;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int testCase = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			String[] input = br.readLine().split(" ");
			int N = Integer.parseInt(input[0]);
			parents = new int[N + 1];
			Arrays.setAll(parents, i -> i);

			for (int i = 0; i < Integer.parseInt(input[1]); i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				union(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			}

			int answer = 0;
			for (int i = 1; i <N + 1; i++){
				if (i == find(i))
					answer++;
			}
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}

	public static int find(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find(parents[x]);
	}

	public static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b)
			return;
		parents[b] = a;
	}
}