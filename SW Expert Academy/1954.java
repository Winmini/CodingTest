import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final StringBuilder sb = new StringBuilder();
	private static final int[] dir_x = {0, 1, 0, -1};
	private static final int[] dir_y = {1, 0, -1, 0};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(in.readLine());
		for (int t = 1; t <= testCase; t++) {
			int size = Integer.parseInt(in.readLine());
			int[][] snail = new int[size][size];
			int k = 2;
			int x = 0;
			int y = 0;
			snail[0][0] = 1;
			while (k <= size * size) {
				for (int i = 0; i < 4; i++) {
					while (true){
						x += dir_x[i];
						y += dir_y[i];
						if (x < 0 || y < 0 || x >= size || y >= size) {
							x -= dir_x[i];
							y -= dir_y[i];
							break;
						}
						if (snail[x][y] != 0) {
							x -= dir_x[i];
							y -= dir_y[i];
							break;
						}
						snail[x][y] = k;
						k++;
					}
				}
			}
			sb.append("#");
			sb.append(t);
			sb.append("\n");
			for (int i = 0; i < size; i++) {
				for (int j = 0; j < size; j++) {
					sb.append(snail[i][j]);
					sb.append(" ");
				}
				sb.append("\n");
			}
		}
		System.out.print(sb);
	}

}