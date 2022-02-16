
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Solution {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, -1, 0, 1, 0};
	private static final int[] dir_y = {0, 0, 1, 0, -1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= testCase; tc++) {
			sb.append("#").append(tc).append(" ");
			int ans = 0;
			String[] input = br.readLine().split(" ");
			int M = Integer.parseInt(input[0]);
			int BC = Integer.parseInt(input[1]);
			int[][] bcs = new int[BC][4];

			StringTokenizer st = new StringTokenizer(br.readLine());
			int[] moveA = new int[M + 1];
			for (int i = 1; i <= M; i++) {
				moveA[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			int[] moveB = new int[M + 1];
			for (int i = 1; i <= M; i++) {
				moveB[i] = Integer.parseInt(st.nextToken());
			}

			for (int i = 0; i < BC; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 4; j++) {
					bcs[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			Arrays.sort(bcs, Comparator.comparingInt((int[] i) -> i[3]).reversed());

			int a_x = 1;
			int a_y = 1;
			int b_x = 10;
			int b_y = 10;

			for (int i = 0; i <= M; i++) {
				boolean[] usedA = new boolean[9];
				boolean[] usedB = new boolean[9];

				a_x += dir_x[moveA[i]];
				a_y += dir_y[moveA[i]];
				b_x += dir_x[moveB[i]];
				b_y += dir_y[moveB[i]];
				for (int j = 0; j < BC; j++) {
					if (Math.abs(a_x - bcs[j][1]) + Math.abs(a_y - bcs[j][0]) <= bcs[j][2]) {
						usedA[j] = true;
					}
					if (Math.abs(b_x - bcs[j][1]) + Math.abs(b_y - bcs[j][0]) <= bcs[j][2]) {
						usedB[j] = true;
					}
				}
				int cnt = 0;
				for (int j = 0; j < BC; j++) {
					if (usedA[j] && usedB[j]) {
						cnt++;
						ans += bcs[j][3];
						usedA[j] = false;
						usedB[j] = false;
					} else if (usedA[j] && !usedB[j]) {
						cnt++;
						ans += bcs[j][3];
						usedA = new boolean[9];
					} else if (!usedA[j] && usedB[j]) {
						cnt++;
						ans += bcs[j][3];
						usedB = new boolean[9];
					}
					if (cnt == 2)
						break;
				}
			}
			sb.append(ans).append("\n");
		}
		System.out.println(sb);
	}

}