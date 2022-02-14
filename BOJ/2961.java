
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static boolean[] visited;
	private static int N;
	private static String[][] ingredients;
	private static int ans = Integer.MAX_VALUE;
	private static int[][] flavor;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		visited = new boolean[1 << N];
		flavor = new int[1 << N][2];
		ingredients = new String[N][2];
		for (int i = 0; i < N; i++) {
			ingredients[i] = br.readLine().split(" ");
		}
		solve(0);

		for (int i = 1; i < 1 << N; i++) {
			if (flavor[i][0] != 0) {
				ans = Math.min(ans, Math.abs(flavor[i][0] - flavor[i][1]));
			}
		}
		System.out.println(ans);

	}

	private static void solve(int state) {
		if (visited[state])
			return;
		visited[state] = true;
		int num = 1;
		int num2 = 0;
		for (int i = 0; i < N; i++) {
			if ((state & (1 << i)) != 0) {
				num *= Integer.parseInt(ingredients[i][0]);
				num2 += Integer.parseInt(ingredients[i][1]);
			}
		}
		flavor[state][0] = num;
		flavor[state][1] = num2;
		for (int i = 0; i < N; i++) {
			if ((state & (1 << i)) == 0) {
				solve(state | (1 << i));
			}
		}

	}

}