
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb.append("<");
		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]);
		int K = Integer.parseInt(input[1]);
		List<Integer> arr = new LinkedList<>();
		int[] ans = new int[N];
		for (int i = 1; i <= N; i++) {
			arr.add(i);
		}
		int loc = 0;
		for (int i = 0; i < N; i++) {
			loc += K - 1;
			loc %= arr.size();
			ans[i] = arr.remove(loc);
		}
		sb.append(ans[0]);
		for (int i = 0; i < N - 1; i++) {
			sb.append(",").append(" ").append(ans[i+1]);
		}
		sb.append(">");
		System.out.print(sb);
	}
}