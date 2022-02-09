import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int[][] board = new int[Integer.parseInt(input[0])][Integer.parseInt(input[1])];

		for (int i = 0; i < Integer.parseInt(input[0]); i++) {
			board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}

		for (int i = 0; i < Integer.parseInt(input[2]); i++) {
			int[] lu = {0, 0};
			int[] rd = {Integer.parseInt(input[0]) - 1, Integer.parseInt(input[1]) - 1};
			while (true) {
				int[] edge = {board[lu[0]][lu[1]], board[rd[0]][lu[1]],
					board[rd[0]][rd[1]], board[lu[0]][rd[1]]};

				for (int j = 0; j < rd[0] - lu[0] - 1; j++) {
					board[rd[0] - j][lu[1]] = board[rd[0] - j - 1][lu[1]];
				}
				board[lu[0] + 1][lu[1]] = edge[0];

				for (int j = 0; j < rd[1] - lu[1] - 1; j++) {
					board[rd[0]][rd[1] - j] = board[rd[0]][rd[1] - j - 1];
				}
				board[rd[0]][lu[1] + 1] = edge[1];

				for (int j = 0; j < rd[0] - lu[0] - 1; j++) {
					board[lu[0] + j][rd[1]] = board[lu[0] + j + 1][rd[1]];
				}
				board[rd[0] - 1][rd[1]] = edge[2];

				for (int j = 0; j < rd[1] - lu[1] - 1; j++) {
					board[lu[0]][lu[1] + j] = board[lu[0]][lu[1] + j + 1];
				}
				board[lu[0]][rd[1] - 1] = edge[3];

				lu[0] += 1;
				lu[1] += 1;
				rd[0] -= 1;
				rd[1] -= 1;

				if (lu[0] >= rd[0] || lu[1] >= rd[1])
					break;
			}
		}
		for (int i = 0; i < Integer.parseInt(input[0]); i++) {
			Arrays.stream(board[i]).forEach(x -> sb.append(x).append(" "));
			sb.append("\n");
		}
		System.out.print(sb);
	}

}
//sb.append("#").append(tc).append(" ").append(answer).append("\n");