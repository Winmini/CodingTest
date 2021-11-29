import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	private static int[] node;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int numberOfUnion = Integer.parseInt(br.readLine());
		node = new int[numberOfUnion + 1];
		Arrays.fill(node, -1);
		int row = Integer.parseInt(br.readLine());
		for (int i = 0; i < numberOfUnion; i++) {
			String[] col = br.readLine().split(" ");
			for (int j = i + 1; j < numberOfUnion; j++) {
				if (col[j].equals("1")) {
					merge(i + 1, j + 1);
				}
			}
		}
		String[] island = br.readLine().split(" ");
		String answer = "NO";
		for (int i = 0; i < row - 1; i++) {
			if (find(Integer.parseInt(island[i])) != find(Integer.parseInt(island[i + 1]))) {
				break;
			}
			if (i == row - 2) {
				answer = "YES";
			}
		}
		System.out.println(answer);
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