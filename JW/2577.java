import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int[] eat = new int[d + 1];
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		int count = 0;
		int ans = 0;

		for (int i = 0; i < k; i++) {
			if (eat[arr[i]] == 0)
				count++;
			eat[arr[i]]++;
		}
		ans = count;
		for (int i = 1; i < N; i++) {
			if (ans <= count) {
				if (eat[c] == 0)
					ans = count + 1;
				else
					ans = count;
			}

			eat[arr[i - 1]]--;
			if (eat[arr[i - 1]] == 0)
				count--;
			int x = arr[(i + k - 1) % N];
			if (eat[x] == 0)
				count++;
			eat[x]++;
		}
		System.out.println(ans);
	}

}