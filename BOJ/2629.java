import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Algo2_서울_10반_임승민 {
	private static final StringBuilder sb = new StringBuilder();
	public static int[] parent;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		boolean[] dp = new boolean[1200001];
		// 가능한지 체크하는 배열

		Set<Integer> can = new HashSet<>();
		// 무게 재는게 가능한지 확인하는 셋

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int t = Integer.parseInt(st.nextToken());
			Set<Integer> tmp = new HashSet<>();
			tmp.add(t);
			// 주어진 추 무게는 잴 수 있음
			for (int j : can) {
				tmp.add(j); // 기존 가진 것과
				tmp.add(j + t); // 가진 것에 현재 추를 더한것도 잴 수 있음
			}
			can.addAll(tmp);
		}
		int max = 0;
		for (int i : can) {
			dp[i] = true;
			max = Math.max(i, max); // 그냥 최적화를위해 MAX값 가져옴
		}

		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int t = Integer.parseInt(st.nextToken());
			if(dp[t]){ // 해당 무게 자체가 있거나
				sb.append("Y ");
				continue;
			}
			boolean chk = false;
			for (int j = 0; j <= max; j++) {
				if (dp[j] && dp[j+t]){ // 특정 무게를 잴 수 있을 때 내가 재려하는 무게를 더한 값 역시 잴 수 있는 경우
					sb.append("Y ");
					chk	= true;
					break;
				}
			}
			if (!chk)
				sb.append("N "); // 아무것도 해당이 안됨
		}

		System.out.println(sb);
	}

}
