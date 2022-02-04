
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();
	// private static final int[] dir_x = {0, 1, 0, -1};
	// private static final int[] dir_y = {1, 0, -1, 0};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(in.readLine());

		for (int tc = 1; tc <= testCase; tc++) {
			int size = Integer.parseInt(in.readLine());
			int l = size / 2;
			int r = size / 2;
			int ans = 0;

			for (int i = 0; i <= size / 2; i++) {
				String row = in.readLine();
				for (int j = l; j <= r; j++) {
					ans += row.charAt(j) - '0';
				}
				l--;
				r++;
			}
			l += 2;
			r -= 2;
			for (int i = size / 2 + 1; i < size; i++) {
				String row = in.readLine();
				for (int j = l; j <= r; j++) {
					ans += row.charAt(j) - '0';
				}
				l++;
				r--;
			}
			sb.append("#");
			sb.append(tc);
			sb.append(" ");
			sb.append(ans);
			sb.append("\n");
		}

		System.out.print(sb);
	}

}