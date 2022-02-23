import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int M;
	static int answer = Integer.MAX_VALUE;
	static List<int[]> house;
	static List<int[]> kfc;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		house = new ArrayList<>();
		kfc = new ArrayList<>();
		N = Integer.parseInt(input[0]);
		M = Integer.parseInt(input[1]);

		int total = 0;
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int tmp = Integer.parseInt(st.nextToken());
				if (tmp == 1)
					house.add(new int[] {i, j});
				else if (tmp == 2) {
					kfc.add(new int[] {i, j});
					total++;
				}
			}
		}
		solve(0, 0, total, 0);
		System.out.println(answer);
	}

	public static void solve(int n, int cnt, int total, int flag) {
		if (cnt == M) {
			int t_ans = 0;
			for (int[] h : house) {
				int dis = Integer.MAX_VALUE;
				for (int i = 0; i < total; i ++) {
					if ((flag & (1 << i)) != 0) {
						dis = Math.min(dis, Math.abs(h[0] - kfc.get(i)[0]) + Math.abs(h[1] - kfc.get(i)[1]));
					}
				}
				t_ans += dis;
			}
			answer = Math.min(answer, t_ans);
			return;
		}

		for (int i = n; i < total; i++) {
			solve(i+1, cnt + 1, total ,flag | (1 << i));
		}
	}
}