import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	private static final int[] dir_x = {-1, 0, 1};
	private static int R;
	private static int C;
	private static char[][] board;
	static boolean[][] visited;
	static int answer = 0;
	static boolean chk;

	private static final StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		R = Integer.parseInt(input[0]);
		C = Integer.parseInt(input[1]);

		board = new char[R][C];
		visited = new boolean[R][C];

		for (int i = 0; i < R; i++) {
			board[i] = br.readLine().toCharArray();
		}
		for (int now_x = 0; now_x < R; now_x++) {
			int now_y = 0;
			chk = false;
			getAnswer(now_x, now_y);
			if (chk)
				answer++;
		}
		System.out.println(answer);
	}

	private static void getAnswer(int now_x, int now_y) {
		if(now_y == C-1){
			chk = true;
		}
		for (int i = 0; i < 3; i++) {
			if (chk)
				return;
			int nxt_x = now_x + dir_x[i];
			int nxt_y = now_y + 1;
			if (nxt_x < 0 || nxt_x >= R || nxt_y >= C)
				continue;
			if (visited[nxt_x][nxt_y] || board[nxt_x][nxt_y] == 'x')
				continue;
			visited[nxt_x][nxt_y] = true;
			getAnswer(nxt_x, nxt_y);
		}
	}
}