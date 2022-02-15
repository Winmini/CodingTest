
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<int[]> cs = new ArrayList<>(N);
		for (int i = 0; i < N; i++) {
			String[] input = br.readLine().split(" ");
			cs.add(new int[] {Integer.parseInt(input[0]), Integer.parseInt(input[1])});
		}
		cs.sort(Comparator.comparingInt((int[] i) -> i[1]).thenComparingInt((int[] i) -> i[0]));
		int ans = 0;
		int t = -271;
		for (int[] c : cs) {
			if (t < c[0]){
				ans += 1;
				t = c[1];
			}
		}
		System.out.println(ans);
	}
}