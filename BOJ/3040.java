import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] list = new int[9];
	private static final List<Integer> answer = new LinkedList<>();
	private static final boolean[] visited = new boolean[9];

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		boolean[] visited = new boolean[9];
		for (int i = 0; i < 9; i++) {
			list[i] = Integer.parseInt(br.readLine());
		}
		combination(list, 0, 7, 0);
	}

	static void combination(int[] arr, int start, int r, int sum) {
		if (r == 0) {
			if (sum == 100) {
				for (int i = 0; i < 9; i++) {
					if (visited[i]) {
						System.out.println(arr[i]);
					}
				}
				System.exit(0);
			}
			return;
		}

		for (int i = start; i < 9; i++) {
			visited[i] = true;
			combination(arr, i + 1, r - 1, sum + arr[i]);
			visited[i] = false;
		}
	}
}