import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int testCase = 10;
		for (int tc = 1; tc <= testCase; tc++) {
			br.readLine();
			int[][] board = new int[100][100];
			sb.append("#").append(tc).append(" ");
			for (int i = 0; i < 100; i++) {
				String[] input = br.readLine().split(" ");
				for (int j = 0; j < 100; j++) {
					board[i][j] = Integer.parseInt(input[j]);
				}
			}
			int cur_x = 99;
			int cur_y = 0;
			for (int i = 0; i < 100; i++) {
				if (board[99][i] == 2) {
					cur_y = i;
					break;
				}
			}
			while (cur_x != 0) {
				int tmp_l = cur_y - 1;
				int tmp_r = cur_y + 1;
				if (tmp_l > 0 && board[cur_x][tmp_l] == 1) {
					while (tmp_l > 0 && board[cur_x][tmp_l] == 1) {
						tmp_l -= 1;
					}
					cur_y = tmp_l + 1;
				} else if (tmp_r < 100 && board[cur_x][tmp_r] == 1) {
					while (tmp_r < 100 && board[cur_x][tmp_r] == 1) {
						tmp_r += 1;
					}
					cur_y = tmp_r - 1;
				}
				cur_x -= 1;
			}
			sb.append(cur_y).append("\n");
		}
		System.out.println(sb);
	}

}