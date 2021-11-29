import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	private static int[] node;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int numberOfUnion = Integer.parseInt(input[0]);
		node = new int[numberOfUnion + 1];
		Arrays.fill(node, -1);
		int testCase = Integer.parseInt(input[1]);
		for (int i = 0; i < testCase; i++) {
			String[] orderInfo = br.readLine().split(" ");
			int order = Integer.parseInt(orderInfo[0]);
			int first = Integer.parseInt(orderInfo[1]);
			int second = Integer.parseInt(orderInfo[2]);
			if (order == 1) {
				if (find(first) == find(second)) {
					System.out.println("YES");
				} else {
					System.out.println("NO");
				}
			}
			if (order == 0) {
				merge(first, second);
			}
		}
	}

	private static int find(int number) {
		if (node[number] == -1) {
			return number;
		}
		node[number] = find(node[number]);
		return node[number];
	}

	private static void merge(int first, int second) {
		first = find(first);
		second = find(second);
		if (first == second) {
			return;
		}
		node[first] = second;
	}
}